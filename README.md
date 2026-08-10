# Amplifier UX Ergonomist Bundle

An evidence-led human factors and UX expert for digital products and AI-agent experiences.

## Why this bundle

`amplifier-bundle-design-intelligence` covers visual and component craft. This bundle covers the upstream and evaluative layer: user tasks, cognitive ergonomics, accessibility, information architecture, human-AI control, evidence quality, and UX validation.

## What it provides

- `ux-ergonomist:ux-ergonomist`, the lead context-sink expert
- `ux-ergonomist:evidence-researcher`, for source-graded UX and human-factors research
- `ux-ergonomist:accessibility-auditor`, for inclusive interaction and conformance analysis
- `ux-ergonomist:human-agent-designer`, for autonomy, authority, trust, intervention, and recovery
- a thin composable behavior
- ergonomic diagnostic lenses
- a UX evaluation playbook
- a source and freshness policy
- three reusable recipes for ergonomic review, agent-experience review, and research-to-decision synthesis
- an adversarial benchmark suite
- an evidence-backed design brief

## Use

Run directly:

```bash
amplifier run --bundle ./bundle.md "Review this agent workflow for user control, recovery, and measurable UX outcomes"
```

Compose only the behavior into another bundle:

```yaml
includes:
  - bundle: git+https://github.com/YOUR-ORG/amplifier-bundle-ux-ergonomist@main#subdirectory=behaviors/ux-ergonomist.yaml
```

Typical requests:

- Review this onboarding flow and tell me what evidence we still need.
- Design the human approval and recovery model for this autonomous agent.
- Turn these support complaints into ranked UX hypotheses and a study plan.
- Audit this workflow for cognitive and accessibility barriers.
- Write measurable UX acceptance criteria for this feature.

## Recipes

The included recipes use the Amplifier Recipes schema and require the Recipes capability to be installed in the running Amplifier application.

```bash
amplifier tool invoke recipes operation=execute \
  recipe_path=recipes/ergonomic-review.yaml \
  context='{"target":"./prototype","user_and_task":"Operations analyst resolves a failed job"}'
```

Available recipes:

- `recipes/ergonomic-review.yaml`
- `recipes/agent-experience-review.yaml`
- `recipes/research-to-decision.yaml`

## Composition

Pair it with Microsoft's design-intelligence bundle when the task needs both ergonomic judgment and visual execution. Delegate to UX Ergonomist first for problem framing and acceptance criteria, then to visual specialists for production.

## Status

Version 0.1.0 is a research-backed initial design. Validate against real cases before treating its severity ratings or recommendations as calibrated.
