# ARGUS Red-Team: Adversarial Testing and AI Assurance Harness

Structured adversarial testing of [ARGUS](https://vanessamiranda.github.io/kyc-onboarding-agent/),
a multi-agent Know Your Customer / Customer Due Diligence review agent,
conducted as a repeatable assurance exercise. I built the agent; this
repository is me independently attacking it and publishing the results.

## What this demonstrates

- AI red teaming against a live agent: prompt injection (direct and
  indirect), jailbreak, system prompt extraction, sensitive data
  leakage, and excessive agency tests.
- Framework-mapped assurance: every test case is classified against
  MITRE ATLAS technique identifiers, the OWASP Top 10 for Large
  Language Model Applications (2025), and NIST AI Risk Management
  Framework functions, with ISO/IEC 42001 control themes referenced in
  the methodology.
- Second-line discipline: pre-defined pass criteria, verbatim evidence
  retention, automated judging with mandatory human verification of
  failures, severity ratings, and remediation tracking with retest.

## Repository structure

```
attacks/attack_library.yaml    14 adversarial test cases across 6 categories
runner/redteam_runner.py       Executes tests against the target agent layer
report/report_generator.py     Builds the assurance report from verified results
governance/methodology.md      Threat model, severity scale, evidence standard
```

## Running it

```bash
pip install pyyaml
export ANTHROPIC_API_KEY=your-key

# 1. Validate the library
python runner/redteam_runner.py --dry-run

# 2. Execute against the agent's system prompt + model layer
python runner/redteam_runner.py --target-system-prompt path/to/argus_system_prompt.txt

# 3. Human-verify every FAIL transcript in the results JSON
#    (set "human_confirmed": true where upheld)

# 4. Generate the assurance report
python report/report_generator.py report/results_<run_id>.json
```

## Honesty rules baked into the tooling

- The report generator refuses to publish an unverified failure: judge
  verdicts are candidate findings until a human confirms the transcript.
- A run without the agent's system prompt is labelled a bare-model test
  and the report scopes the claim accordingly.
- Every published report carries its limitations: point-in-time,
  conversational surface only, self-assessment by the system author.

## Author

Vanessa Miranda - AI governance and digital transformation,
Singapore. Related work: ARGUS (MAS FEAT and NIST AI RMF mapped KYC
agent), peer-reviewed retrieval-augmented generation publication
(PubMed PMID 40776301).
