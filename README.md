# Amplifier UX Ergonomist Bundle

An evidence-led human factors and UX expert for digital products and AI-agent experiences.

Version 0.2.0 adds an automatic six-mode workflow, reusable procedural skills, lifecycle and adversarial ergonomics, experiments, executable structural validation, and CI.

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
- a full-cycle automated recipe plus longitudinal and sociotechnical reviews
- six interactive modes that automatically advance when their phase contract is satisfied
- eight on-demand procedural skills
- lifecycle, adversarial, macroergonomic, cognitive-accessibility, and temporal-interaction contexts
- two experiment definitions and a weighted evaluation rubric
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
- `recipes/ergonomics-full-cycle.yaml`
- `recipes/longitudinal-agent-impact-review.yaml`
- `recipes/sociotechnical-workflow-review.yaml`

## Interactive workflow

Start with:

```text
/ergonomics-frame
Review the failed-job recovery workflow for operations analysts.
```

The bundle moves through:

```text
ergonomics-frame
  → ergonomics-research
  → ergonomics-review
  → ergonomics-recommend
  → ergonomics-verify
  → ergonomics-finish
```

Each mode defines its required artifact and allowed transitions. When the artifact is complete, the agent calls Amplifier's `mode` tool to advance. It pauses for material ambiguity, unavailable evidence, consequential user decisions, external actions, or a blocked verification result. See `docs/WORKFLOW.md`.

## Skills

- `task-analysis`
- `ux-evidence-synthesis`
- `cognitive-walkthrough`
- `accessibility-evaluation`
- `human-agent-authority-map`
- `ux-acceptance-criteria`
- `usability-study-design`
- `ergonomics-verification`

## Validation

```bash
python -m pip install pyyaml
python tests/validate_bundle.py
```

The validator checks YAML and frontmatter, agent discoverability, recipe-agent references, mode transitions, contributed capability reachability, namespaced references, and workflow completeness. GitHub Actions runs it on pushes and pull requests.

## Composition

Pair it with Microsoft's design-intelligence bundle when the task needs both ergonomic judgment and visual execution. Delegate to UX Ergonomist first for problem framing and acceptance criteria, then to visual specialists for production.

## Status

Version 0.2.0 is research-backed but not yet empirically calibrated. Run the included experiments and benchmark cases before treating severity ratings, delegation choices, or recommendations as calibrated.
