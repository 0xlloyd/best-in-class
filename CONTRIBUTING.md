# Contributing

Keep the skill concise, portable and grounded in observable outcomes.

For a proposed change:

1. Describe the actual problem and the prompt that exposes it. Remove private information.
2. Record the host/model, date, available tools and whether the skill was activated.
3. Include the relevant input, output and expected behavior. Explain what the evidence supports.
4. Make the smallest useful change and rerun the affected scenario. Compare with the prior version where practical.
5. Update compatibility or evaluation notes only with results you actually observed.

Do not add unsupported performance claims, provider-specific requirements to the core, fabricated sources, private knowledge notes or credentials. Preserve user constraints and avoid turning short requests into lengthy audits.

Run the local package checks from the repository root:

```bash
python3 scripts/check_package.py
```

For behavior checks, use `evals/scenarios.md`. Package validation is not an evaluation of model performance.
