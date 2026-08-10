# Ergonomics workflow

The ergonomic workflow advances through six states:

`ergonomics-frame → ergonomics-research → ergonomics-review → ergonomics-recommend → ergonomics-verify → ergonomics-finish`

Advance automatically with the `mode` tool when the current mode's completion contract is satisfied. Tell the user what was established and which mode is starting. Pause instead when a required decision, unavailable source, material ambiguity, or consequential approval requires human input.

Move backward when later evidence invalidates an earlier artifact. Never preserve forward motion by inventing evidence or filling a required artifact speculatively.

The interactive modes and `recipes/ergonomics-full-cycle.yaml` implement the same conceptual lifecycle. Modes provide steering; the recipe provides cruise control.
