# Evaluation playbook

## Match method to question

| Question | Preferred method | Useful measures |
|---|---|---|
| Can users complete the task? | Moderated or unmoderated usability test | task success, critical errors, time, assistance |
| Why do users fail? | Moderated test, contextual inquiry, interview after observed behavior | breakdown sequence, mental model, recovery |
| How often does it happen? | Product analytics, representative survey, support coding | prevalence, funnel loss, recurrence |
| Is the structure understandable? | Tree test, first-click test, card sort plus follow-up | findability, path directness, label comprehension |
| Is it accessible? | Automated scan plus manual keyboard, screen reader, zoom/reflow, and affected-user testing | WCAG findings, task success by access need |
| Is the new design better? | Counterbalanced comparative test or experiment | paired task outcomes, preference after use |
| Is trust calibrated? | Scenario study with varied system correctness and consequence | reliance, override, verification, error detection |
| Does it work over time? | Field study, diary, longitudinal telemetry | adoption, retention, workarounds, reliance drift |

## Study design minimum

Specify population and relevant variation, realistic tasks, environment, prototype fidelity, success definition, critical-error definition, measures, analysis approach, and stopping rule. Do not prescribe a sample size solely from convention. Small formative studies can expose severe breakdowns; they do not estimate population prevalence.

## Core behavioral measures

- task completion and quality
- time on task, interpreted with task quality
- critical and noncritical errors
- assistance, retries, reversals, and abandonment
- path deviation and unnecessary steps
- comprehension and recall when those are product goals
- accessibility barriers by interaction mode
- verification behavior and reliance for AI systems

Questionnaires such as SUS, UMUX-LITE, SUPR-Q, NASA-TLX, and single ease questions are supporting measures. They do not replace behavioral evidence and should not be mixed into an unvalidated composite without justification.

## Acceptance criteria pattern

Write criteria as observable outcomes:

`Given <user/context>, when <task>, the user can <outcome> without <critical failure>, and the system provides <evidence/recovery>.`

Attach thresholds only when baseline, risk, or decision needs justify them. Otherwise define the measurement plan before inventing a number.
