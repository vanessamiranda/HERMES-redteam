# HERMES: Adversarial Testing and AI Assurance Harness for ARGUS

HERMES is a structured adversarial testing and assurance exercise against
[ARGUS](https://vanessamiranda.github.io/kyc-onboarding-agent/), a
multi-agent Know Your Customer / Customer Due Diligence review agent
design. In mythology, Argus was the all-seeing watchman and Hermes the
one who got past him. I built the watchman; this repository is me
independently attacking it and publishing the evidence.

## Scope, stated plainly

HERMES tests the ARGUS agent's instruction layer: the governance system
prompt (published in this repo as `argus_system_prompt.txt`) running on
the production-intended model. The public ARGUS demo is a front-end
simulation, so this exercise tests the agent specification rather than a
deployed service, and that scoping is stated in every report. All test
prompts are standard published-technique strings for defensive
evaluation of systems you own or are authorised to test.

## Executed assessment

First full run executed on 3 September 2026: 14 adversarial test cases,
14 passed, zero human-confirmed failures. Evidence and report:

- [Assurance report](report/ASSURANCE_REPORT.md)
- [Raw evidence transcripts](report/results_20260903T011051Z.json)

A clean sweep is reported as exactly that, a point-in-time result
against a well-specified instruction layer, not proof the agent is
unbreakable. A negative-control run against a deliberately weakened
system prompt is the planned next step, to demonstrate the test suite
can detect failures.

## What this demonstrates

- AI red teaming of an agent instruction layer: direct and indirect
  prompt injection, jailbreak, system prompt extraction, sensitive data
  leakage, and excessive agency tests.
- Framework-mapped assurance: every test case is classified against
  MITRE ATLAS technique identifiers, the OWASP Top 10 for Large
  Language Model Applications (2025), and NIST AI Risk Management
  Framework functions, with ISO/IEC 42001 control themes referenced in
  the methodology.
- Second-line discipline: pre-defined pass criteria, verbatim evidence
  retention, automated judging with mandatory human verification of
  failures, severity ratings, and remediation tracking with retest.
  This is a self-assessment by the system's author, adopting
  second-line standards; the independence limitation is documented in
  the methodology.

## Repository structure
