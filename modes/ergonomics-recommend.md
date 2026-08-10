---
mode:
  name: ergonomics-recommend
  description: Convert diagnosed ergonomic problems into bounded interventions and measurable acceptance criteria
  shortcut: ergonomics-recommend
  advertised: true
  default_action: block
  allowed_transitions: [ergonomics-review, ergonomics-verify]
  allow_clear: true
  tools:
    safe: [read_file, glob, grep, web_search, web_fetch, load_skill, todo, delegate, recipes]
    warn: [write_file, edit_file, apply_patch, bash]
  contributes:
    agents:
      ux-ergonomist:
        source: "@ux-ergonomist:agents/ux-ergonomist"
      human-agent-designer:
        source: "@ux-ergonomist:agents/human-agent-designer"
    context:
      - "@ux-ergonomist:context/workflow-orientation.md"
      - "@ux-ergonomist:context/knowledge/evaluation-playbook.md"
    skills:
      - "@ux-ergonomist:skills/ux-acceptance-criteria"
      - "@ux-ergonomist:skills/usability-study-design"
---

ERGONOMICS RECOMMEND MODE: Propose the smallest interventions that test the diagnosed mechanisms.

For each recommendation include the user problem, change, causal mechanism, expected outcome, evidence level, trade-off, accessibility consequence, lifecycle consequence, acceptance criterion, and validation method.

Return to review if recommendations do not trace to findings. When every consequential recommendation is testable, activate `ergonomics-verify` automatically. Pause before external or irreversible implementation actions.
