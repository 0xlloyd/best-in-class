# Best in Class

**Research the standard. Apply it. Keep the knowledge.**

Best in Class is an AI skill for researching relevant expert standards, applying them to a task, checking the result and retaining reusable knowledge.

Use it for a product brief, recipe, research plan, presentation or another task where the quality of the approach matters.

## Install and use

Install with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add 0xlloyd/best-in-class --skill best-in-class
```

Then ask:

> Use Best in Class to improve this draft. Research the relevant standard, apply the important changes, and save what is reusable.

The complete installable skill has just two files:

| File | Purpose |
| --- | --- |
| [SKILL.md](skills/best-in-class/SKILL.md) | The workflow, research rules and compact knowledge-note format |
| [agents/openai.yaml](skills/best-in-class/agents/openai.yaml) | Optional display name, description and suggested prompt for compatible hosts |

For manual installation, copy `skills/best-in-class/` into your host's documented custom-skills location. For archive uploads, ZIP that package folder using the layout your host requires; the full repository ZIP also includes documentation and checks.

Without an installer, attach or paste [SKILL.md](skills/best-in-class/SKILL.md) and ask your AI tool to follow it. All task instructions are in that file. This supplies instructions for the conversation; it does not establish persistent installation.

## What it does

**Define → Research → Apply → Check → Retain**

The workflow supports four scopes:

| Mode | Example |
| --- | --- |
| Discover | "Research the strongest approach before we begin." |
| Build | "Create a product brief. We have one engineer and two weeks." |
| Review | "Is this the best? Improve this draft." |
| Capture | "Save the best-supported practices for this topic." |

It calls for respect for planning-only and critique-only requests. When revision is authorized, it asks for the complete improved work. Research and assessment should support the deliverable without overwhelming it.

## Knowledge and capabilities

Tell your agent where to save and retrieve topic notes. The note format is included in [SKILL.md](skills/best-in-class/SKILL.md#topic-note-format); it records practices, sources, applicability, alternatives, uncertainty and revision history. Existing notes should be reassessed and updated rather than duplicated.

The core uses the [Agent Skills format](https://agentskills.io/specification) and has no required vendor API, executable dependency or API key. Your host supplies tools, storage and permissions:

- **Source access:** needed for fresh research; otherwise the result must be labelled provisional.
- **Persistent storage:** needed to save notes; otherwise the agent returns a note for you to save.
- **Version safeguards:** needed to preserve history and handle conflicting edits.
- **Execution or measurement:** needed to verify outcomes; unavailable tests remain unassessed.

Keep private notes outside this public repository. The skill does not configure background memory, cross-tool synchronization or automatic retrieval in later sessions. Installation and behaviour depend on the host and model.

## Evaluation and contributions

Read the [evaluation record](evals/RESULTS.md) for the narrow checks performed and their limitations, and the [behaviour scenarios](evals/scenarios.md) for proposed tests. This project does not claim universal compatibility or demonstrated improvement over a no-skill baseline.

For contributions, provide a reproducible prompt, relevant input/output, expected behaviour, skill revision, host/model, date and available tools. Remove private information. Make the smallest useful change, rerun the affected scenario and report failures as well as successes. Add compatibility or performance claims only when supported by observed results; keep provider-specific requirements out of the core.

Run the local package check:

```bash
python3 scripts/check_package.py
```

GitHub runs the same check on pushes and pull requests. It checks package structure and local documentation links, not model performance.

Created by [Lloyd Bizaoui](https://github.com/0xlloyd). Released under the [MIT License](LICENSE).
