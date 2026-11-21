import importlib.util
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/ai-tech-morning-brief"
spec = importlib.util.spec_from_file_location("install", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class PackageTests(unittest.TestCase):
    def test_relative_links_resolve(self):
        for document in ROOT.rglob("*.md"):
            for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document.read_text()):
                if link.startswith(("http://", "https://", "#")):
                    continue
                with self.subTest(document=document, link=link):
                    self.assertTrue((document.parent / link.split("#", 1)[0]).exists())

    def test_skill_identity(self):
        frontmatter = (SKILL / "SKILL.md").read_text().split("---", 2)[1].splitlines()
        self.assertIn("name: ai-tech-morning-brief", frontmatter)
        self.assertTrue((SKILL / "agents/openai.yaml").is_file())

    def test_install_includes_references_and_is_self_contained(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = installer.install(SKILL, Path(temporary))
            source_files = {path.relative_to(SKILL) for path in SKILL.rglob("*") if path.is_file()}
            copied_files = {path.relative_to(destination) for path in destination.rglob("*") if path.is_file()}
            self.assertEqual(source_files, copied_files)
            for path in source_files:
                self.assertEqual((SKILL / path).read_bytes(), (destination / path).read_bytes())

    def test_existing_installation_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = installer.install(SKILL, Path(temporary))
            marker = destination / "custom.txt"
            marker.write_text("personal changes")
            with self.assertRaises(FileExistsError):
                installer.install(SKILL, Path(temporary))
            self.assertEqual(marker.read_text(), "personal changes")

    def test_broken_symlink_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            destination = target / SKILL.name
            destination.symlink_to(target / "missing")
            with self.assertRaises(FileExistsError):
                installer.install(SKILL, target)
            self.assertTrue(os.path.lexists(destination))
            self.assertTrue(destination.is_symlink())

    def test_existing_file_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            destination = target / SKILL.name
            destination.write_text("preserve")
            with self.assertRaises(FileExistsError):
                installer.install(SKILL, target)
            self.assertEqual(destination.read_text(), "preserve")

    def test_install_inside_source_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(SKILL, SKILL / "nested")

    def test_cli_install(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/install.py"), "--target-dir", temporary],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(temporary) / SKILL.name / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
