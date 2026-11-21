# AI Tech Morning Brief

A portable skill for a useful AI and technology briefing: what changed, what the
evidence supports, what might be worth trying and what can wait. Works with Codex
and Claude Code, using the same skill files. No separate briefing service or paid
subscription is provided by this project.

## Start Here

Ask your assistant:

```text
Help me install AI Tech Morning Brief from
https://github.com/mathemagica/ai-tech-morning-brief.
Read the skill and installer first. Don't overwrite existing skills or set up a
schedule. Then give me a short brief focused on [my interests].
```

Or use a local checkout without installing:

```text
Read /absolute/path/to/ai-tech-morning-brief/skills/ai-tech-morning-brief/SKILL.md
and its source guide. Create a concise AI/tech brief for today focused on
[my interests], using current public sources. Distinguish claims from evidence.
```

You need an assistant with live public research access for a current brief.
Without it, the skill should disclose the limitation rather than invent news.
No email, calendar, CRM connection or credentials are required.

## Install From The Terminal

Requires Git and Python 3.10+. Review the files before running the installer.

```sh
git clone https://github.com/mathemagica/ai-tech-morning-brief.git
cd ai-tech-morning-brief
# Choose the directory for your assistant:
python3 scripts/install.py --target-dir ~/.agents/skills
# Or Claude Code:
python3 scripts/install.py --target-dir ~/.claude/skills
```

The installer copies this one self-contained skill, including its source guide.
It never overwrites an existing installation, connects accounts or schedules a
job. Restart the assistant if skill discovery needs refreshing. Invoke
`$ai-tech-morning-brief` in Codex or `/ai-tech-morning-brief` in Claude Code.

To update an existing installation, ask your assistant to compare it with this
checkout, preserve personal customizations, back it up, and replace it only with
your approval. The installer intentionally refuses automatic replacement.

## What You Get

- Up to three important developments, not three stories just to fill a quota.
- Optional, bounded experiments and practical Try/Track/Review decisions.
- Practitioner pain points and possible business opportunities, labeled as signals.
- Relevant provider/open-model changes, economic evidence and public-interest news.
- Current event opportunities or useful outcomes, without stale deadline alerts.

Default length is roughly 500-700 words or less, with empty sections omitted.
Ask for a shorter brief, a weekly window or a particular focus. The skill does
not assume your employer, company, technical background or speaking experience.
Give it previous briefs if you want deduplication; no private archive is created
automatically.

The [source guide](skills/ai-tech-morning-brief/references/sources.md) explains the
standing pool and evidence limits. Named authors are sources to discover from,
not daily featured guests. Primary announcements establish what was announced;
they do not independently prove performance, adoption or safety.

## Recurring Briefs

Installing a skill does not make it run on a schedule. Ask your assistant to use
your host's supported scheduler, confirm time/timezone and destination, and check
for an existing job before saving anything. Runtime/computer availability depends
on the scheduler. A brief can suggest tools, experiments and events; it does not
authorize installations, registrations, spending, outbound messages or submissions.

## Moving From The Engineering Library

This skill previously lived in `mathemagica/skills` under
`market_intelligence/ai-tech-morning-brief/`. Its discovery name is unchanged.
Use this repository for future updates; do not install two copies with the same
name. If an existing copy or symlink is found, compare and back it up before an
approved replacement. Update any scheduled job's old skill path to
`skills/ai-tech-morning-brief/SKILL.md` within this checkout, preserving its other
settings. Do not duplicate or reschedule the job just because the skill moved.

The engineering library is now focused on
[product development and software architecture](https://github.com/mathemagica/skills).
This repository starts with a clean, generalized snapshot rather than importing
the former repository's commit history. Historical commits in the original
repository are not rewritten by this migration.

## Privacy And Validation

Use public sources by default. Any local notes remain under your control, but
local files do not imply offline AI processing. Do not put personal briefing
profiles, account identifiers, API keys or private correspondence in this repo.

```sh
python3 -m unittest discover -s tests -v
```

Tests check package integrity, source links and non-overwriting installation.
The [behavioral scenarios](evaluations/scenarios.md) describe forward tests;
they are not a claim that live briefing quality has been independently validated.
