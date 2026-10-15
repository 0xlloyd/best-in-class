# Best in Class

**Research the standard. Apply it. Keep the knowledge.**

Best in Class is a portable AI skill for turning a request into work assessed against relevant expert standards. It asks the agent to research what excellence means for your goal, apply that standard, check the result, and retain sourced knowledge for the next task.

Use it for a product brief, a recipe, a research plan, a presentation or another task where the quality of the approach matters.

## Try it

Install with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add 0xlloyd/best-in-class --skill best-in-class
```

Then ask:

> Use Best in Class to improve this draft. Research the relevant standard, apply the important changes, and save what is reusable.

**No skill installer?** Attach or paste [SKILL.md](skills/best-in-class/SKILL.md) into your AI tool and explicitly ask it to follow the workflow. Include the referenced files if it cannot open them. This supplies instructions for that conversation; it does not grant tools or establish persistent installation.

For manual installation and capability requirements, see [Compatibility](docs/compatibility.md).

## What it does

| Stage | What you get |
| --- | --- |
| Define | A clear meaning of “best” for your goal, quality tier and constraints |
| Research | Relevant standards, expert methods, exemplars and alternatives |
| Apply | The requested work, using the selected approach |
| Check | An evidence-based review and material improvements |
| Retain | Reusable knowledge with sources, scope and uncertainty attached |

The main deliverable stays central. The rubric and research should support the work, not overwhelm it.

## Four ways to use it

| When | Example prompt |
| --- | --- |
| Before starting | “Before we build, use Best in Class to research the strongest approach and define the criteria.” |
| Creating something | “Use Best in Class to create a product brief for this problem. We have one engineer and two weeks.” |
| Reviewing work | “Is this the best? Review this draft against relevant standards and return the improved version.” |
| Building knowledge | “Capture the best-supported practices for this topic in a reusable note.” |

It respects requests for planning or critique only. When revision is requested, it calls for the complete improved result, not just a list of suggested changes.

## Keep what you learn

The skill is the method. Your knowledge collection contains the practices discovered while using it.

A topic note records the applicable standard, concrete practices, source links, trade-offs, uncertainty and checks. On later use, the agent should read and reassess the note before researching gaps. If nothing material changed, it reuses the note instead of making a duplicate.

Tell your agent where to save and retrieve your notes. Access and persistence depend on your host. Keep private notes outside this public repository. See the [note template](skills/best-in-class/assets/knowledge-note.md).

## What “portable” means

The core follows the open [Agent Skills format](https://agentskills.io/specification): a `SKILL.md` file with YAML metadata and Markdown instructions, plus optional supporting files. It contains no required vendor API, executable dependency or API key.

A compatible host still needs the capabilities for the task. Fresh research requires source access; automatic knowledge capture requires authorized persistent storage. Without those, the workflow calls for a provisional result or a note you can save yourself.

This release does **not** claim identical behavior across models, universal installation support, or guaranteed improvement. See the [evaluation record](evals/RESULTS.md) for what has actually been checked.

## Why I built it

I wanted a repeatable way to ask: what standard should this work meet, what evidence supports that standard, and how do I keep the useful knowledge for next time?

Best in Class makes those questions part of the task.

## Contribute

Useful contributions include a reproducible failure, a clearer instruction, a sourced example, or a compatibility result with your model and host recorded. See [CONTRIBUTING.md](CONTRIBUTING.md).

Read [the evaluation scenarios](evals/scenarios.md) to help test the workflow. Report failures as well as successes.

Created by [Lloyd Bizaoui](https://github.com/0xlloyd). Released under the [MIT License](LICENSE).
