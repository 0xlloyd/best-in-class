# Compatibility and installation

## Standard, model and host

Agent Skills is an open packaging format. A model reads the instructions; its host supplies installation, discovery, browsing, files and permissions. Conformance to the format does not prove that every model will follow the workflow or that every chat application can install it.

The canonical package is `skills/best-in-class/`. `agents/openai.yaml` is optional UI metadata for hosts that understand it; other hosts can ignore it. The core does not require that file or any specific provider.

## Install

The Skills CLI supports GitHub repositories and selection by skill name:

```bash
npx skills add 0xlloyd/best-in-class --skill best-in-class
```

Use the installer's host selection. For a manual install, copy the complete `skills/best-in-class/` folder into the custom-skills directory documented by your host. Consult its current documentation for scope and path; do not assume one global path works everywhere.

For hosts that accept an uploaded skill archive, ZIP the `best-in-class/` package folder with `SKILL.md` at the appropriate package root for that host. GitHub's repository ZIP includes documentation and is not necessarily a directly uploadable skill archive.

## Use without installation

Attach or paste `SKILL.md`, `references/research-and-evidence.md` and `assets/knowledge-note.md`, then ask the model to use Best in Class for a specific task. If only the main file can be supplied, the core workflow remains readable but referenced details are unavailable. Tell the model that limitation. Do not describe this as persistent installation.

## Capabilities

| Available capability | Intended operation | Fallback |
| --- | --- | --- |
| Read supplied text or files | Inspect the task and any actual original | Ask for the missing material; do not invent it |
| Browse or retrieve credible sources | Verify current standards and compare alternatives | Label research unverified in this run; use supplied evidence provisionally |
| Authorized persistent file storage | Create, update and retrieve topic notes | Return Markdown for the user to save |
| History/version safeguards | Preserve previous knowledge and handle conflicts | Keep a separate previous version; do not silently overwrite |
| Execution or measurement tools | Check outcomes appropriate to the task | Label those outcomes not assessed |

The skill grants no additional access. It does not configure cross-tool synchronization, background memory, scheduled research or automatic retrieval in a different session.

## Verified versus intended support

Check `evals/RESULTS.md` for the actual tested environment and cases. Other host/model combinations are intended targets pending reported tests. Community reports should include versions, prompt, available tools and the observed outcome.

Sources checked 15 October 2026:
- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills overview](https://agentskills.io/home)
- [Skills CLI](https://github.com/vercel-labs/skills)
