---
mode:
  name: ergonomics-finish
  description: Deliver the verified decision package, limitations, ownership, and next operating checkpoint
  shortcut: ergonomics-finish
  advertised: true
  default_action: block
  allowed_transitions: [ergonomics-frame, ergonomics-verify]
  allow_clear: true
  tools:
    safe: [read_file, glob, grep, load_skill, todo, delegate, recipes]
    warn: [write_file, edit_file, apply_patch, bash]
  contributes:
    agents:
      ux-ergonomist:
        source: "@ux-ergonomist:agents/ux-ergonomist"
    context:
      - "@ux-ergonomist:context/workflow-orientation.md"
      - "@ux-ergonomist:context/knowledge/lifecycle-ergonomics.md"
---

ERGONOMICS FINISH MODE: Package the verified decision for action.

Deliver the decision, evidence map, prioritized findings, recommendations, acceptance criteria, validation plan, limitations, accountable owners, monitoring signals, and next review trigger. Distinguish work completed from work merely proposed.

Return to verification if handoff exposes a material gap. Otherwise summarize completion and call the `mode` tool to clear the active mode.
