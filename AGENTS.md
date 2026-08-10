# Repository instructions

This repository packages evidence-led ergonomics and UX capabilities for Microsoft Amplifier.

## Architecture

- Keep `bundle.md` thin.
- Put reusable wiring in `behaviors/`.
- Keep always-loaded context under 500 tokens and limited to capability awareness.
- Put heavy reference material behind agent context sinks.
- Keep agents provider-neutral through `model_role`.
- Recipes must name explicit inputs, outputs, agents, and timeouts.
- Modes must define explicit identity, tool policy, completion contract, and intentional transitions.
- Procedural methodology belongs in `skills/`; domain reference belongs in agent or mode-gated context.

## Quality rules

- Never convert anecdote into prevalence.
- Never claim accessibility conformance without adequate runtime and manual evidence.
- Keep observation, inference, recommendation, and validation distinct.
- Every consequential recommendation needs an acceptance criterion.
- Update `tests/benchmark-cases.yaml` when changing an agent's scope or output contract.
- Validate YAML, frontmatter, namespace references, and archive integrity before release.
- Run `python tests/validate_bundle.py` before publishing.
