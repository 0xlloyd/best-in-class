# Best in Class

**Research the standard. Apply it. Keep the knowledge.**

An AI skill for researching relevant expert standards, applying them to a task, checking the result and retaining reusable knowledge.

## Files

- [SKILL.md](SKILL.md) — the full original workflow, research guide and knowledge-note template, together in one file.
- [agents/openai.yaml](agents/openai.yaml) — optional display metadata and a suggested prompt.
- [README.md](README.md) — usage and licence.

## Use

Install with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add 0xlloyd/best-in-class --skill best-in-class
```

For manual installation, use this repository root as the skill folder in your host's documented custom-skills location. You can also attach or paste [SKILL.md](SKILL.md) into a conversation and explicitly ask your AI tool to follow it.

> Use Best in Class to improve this draft. Research the relevant standard, apply the important changes, and save what is reusable.

The workflow supports researching an approach, creating work, reviewing an existing result, and capturing best practices. It respects planning-only and critique-only requests.

Fresh research requires source access. Tell your agent where it may save and retrieve knowledge notes; keep private notes outside this public repository. Without persistent storage, the instructions call for returning a note you can save yourself. Installation and behaviour depend on the host and model; the skill does not establish automatic memory or cross-tool synchronization.

Created by [Lloyd Bizaoui](https://github.com/0xlloyd).

<details>
<summary>MIT License</summary>

```text
MIT License

Copyright (c) 2026 Lloyd Bizaoui

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

</details>
