# Ergonomics workflow

## Two tracks

Interactive modes and the full-cycle recipe implement the same lifecycle.

| Phase | Interactive mode | Recipe step | Required artifact |
|---|---|---|---|
| Frame | `/ergonomics-frame` | `frame` | decision frame and task boundary |
| Research | `/ergonomics-research` | `research` | claim-level evidence map |
| Review | `/ergonomics-review` | `review` | causal findings and failure models |
| Recommend | `/ergonomics-recommend` | `recommend` | bounded interventions and criteria |
| Verify | `/ergonomics-verify` | `verify` | PASS, REVISE, or BLOCKED audit |
| Finish | `/ergonomics-finish` | `finish` | verified decision package |

## Automatic movement

Each mode defines a completion contract in its body and an `allowed_transitions` list in frontmatter. When the contract is satisfied, the agent calls Amplifier's `mode` tool to activate the next mode and tells the user what changed. The `mode` tool remains available regardless of tool policy.

Automatic movement stops when:

- a required decision belongs to the user
- access to necessary evidence is unavailable
- a material ambiguity would change the result
- an external or irreversible action requires approval
- verification returns BLOCKED

Later evidence may move the workflow backward. Forward progress is never preserved by fabricating a required artifact.

## Start interactively

```text
/ergonomics-frame
Review the failed-job recovery workflow for operations analysts.
```

## Run automatically

```bash
amplifier tool invoke recipes operation=execute \
  recipe_path=recipes/ergonomics-full-cycle.yaml \
  context='{"target":"./prototype","users_and_task":"Operations analyst resolves a failed job","decision":"What should change before implementation?"}'
```
