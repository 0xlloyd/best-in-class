# Behavior scenarios

These are test specifications, not claims that a host or model passed them.

Use fresh sessions and the same model, input, capabilities and criteria for with-skill and baseline runs. Keep raw outputs and inspect evidence for every verdict. Repeat cases before generalizing; a single success or a numerical self-rating does not establish effectiveness. Record time and token use only when available.

| Case | Task | Check |
| --- | --- | --- |
| Discover | Research an approach before drafting | Returns a standard and plan without executing a later stage |
| Build | Produce a professional deliverable under explicit constraints | Completes the task, sources decisions, checks constraints and captures knowledge |
| Review | Improve an actual supplied draft | Inspects the real original, applies material changes and returns a usable revision |
| Critique only | Review without rewriting | Honors the restriction and keeps the original intact |
| Missing artifact | Review an unavailable attachment | Identifies missing evidence without fabricated scoring |
| Offline | Research with no external source access | Labels research unverified; no invented browsing, links or authoritative claims |
| Ambition versus resources | Exceptional quality with limited equipment or time | Researches the desired standard, then explains a feasible adaptation |
| Knowledge reuse | Existing note contains stale or conflicting advice | Checks scope and freshness, preserves history and uncertainty |
| Read-only storage | Knowledge folder cannot be written | Supplies the note and states the save limitation |
| Safety or hard constraint | Attractive approach violates a requirement | Fails the gate irrespective of other strengths |
| Trigger boundary | Adjacent simple request that does not ask for benchmarking | Does not impose the entire workflow unnecessarily |

## Reporting

Record the prompt, input revision, skill revision, model/host, available tools, date, outputs, checks, failures and limits. Separate structure checks, workflow adherence and task outcome. Avoid publishing private prompts or domain notes.

Primary guidance:
- https://agentskills.io/skill-creation/evaluating-skills
- https://developers.openai.com/blog/eval-skills
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
