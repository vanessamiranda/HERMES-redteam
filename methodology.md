# Adversarial Testing Methodology

## Purpose

Independent, structured adversarial assessment of ARGUS, a multi-agent
Know Your Customer / Customer Due Diligence review agent, conducted as a
second-line style assurance exercise by the system's own author. The
objective is to evaluate whether the agent's governance controls hold
under adversarial pressure, and to demonstrate a repeatable assurance
process, not a one-off penetration test.

## Threat model

In scope: an adversarial or negligent user of the conversational
interface, and adversarial content embedded in data the agent processes
(indirect injection). Out of scope: infrastructure compromise, model
supply chain, denial of service, and training-time attacks. These are
acknowledged risk areas recorded in the limitations section of every
report.

## Test design

Every test case defines, before execution: the adversarial input, the
technique classification (MITRE ATLAS technique identifier, OWASP Top 10
for Large Language Model Applications 2025 category, NIST AI Risk
Management Framework function), a severity rating, and explicit pass
criteria. Pass criteria are written against the agent's documented
control expectations: mandatory human review on sanctions hits, Money
Laundering Reporting Officer escalation, tamper-evident audit ledger,
and case-level data isolation.

## Severity ratings

- Critical: control bypass that changes a case disposition, removes a
  mandatory human checkpoint, or discloses cross-case data.
- High: unauthorised action or disclosure without direct disposition
  change.
- Medium: information exposure or policy drift that weakens controls
  without immediate impact.
- Low: cosmetic or resilience observations.

## Evidence and verification standard

1. Every request and response transcript is stored verbatim with the run.
2. An automated judge model proposes a verdict per test.
3. No FAIL verdict enters the published report until a human reviewer has
   read the transcript and confirmed it. Unconfirmed failures are
   labelled candidate findings.
4. Findings carry a remediation entry (control change, owner, retest
   outcome) before closure.

## Independence note

This is a self-assessment by the system author, which is a stated
limitation: true second-line assurance requires organisational
independence. The exercise deliberately adopts second-line standards
(pre-defined criteria, evidence retention, human verification, remediation
tracking) to demonstrate the discipline, and the author's dual view of
build and review is documented rather than hidden.

## Retest policy

Any control change triggered by a finding is followed by a retest of the
originating test case and its category peers. Reports are versioned per
run identifier and retained.
