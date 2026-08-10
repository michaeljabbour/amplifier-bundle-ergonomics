---
mode:
  name: ergonomics-review
  description: Diagnose task, accessibility, cognitive, temporal, organizational, and agent-interaction breakdowns
  shortcut: ergonomics-review
  advertised: true
  default_action: block
  allowed_transitions: [ergonomics-research, ergonomics-recommend]
  allow_clear: true
  tools:
    safe: [read_file, glob, grep, web_search, web_fetch, load_skill, todo, delegate, recipes]
  contributes:
    agents:
      ux-ergonomist:
        source: "@ux-ergonomist:agents/ux-ergonomist"
      accessibility-auditor:
        source: "@ux-ergonomist:agents/accessibility-auditor"
      human-agent-designer:
        source: "@ux-ergonomist:agents/human-agent-designer"
    context:
      - "@ux-ergonomist:context/workflow-orientation.md"
      - "@ux-ergonomist:context/knowledge/ergonomics-lenses.md"
      - "@ux-ergonomist:context/knowledge/lifecycle-ergonomics.md"
      - "@ux-ergonomist:context/knowledge/adversarial-ergonomics.md"
      - "@ux-ergonomist:context/knowledge/macroergonomics.md"
      - "@ux-ergonomist:context/knowledge/cognitive-accessibility.md"
      - "@ux-ergonomist:context/knowledge/temporal-interaction.md"
    skills:
      - "@ux-ergonomist:skills/cognitive-walkthrough"
      - "@ux-ergonomist:skills/accessibility-evaluation"
      - "@ux-ergonomist:skills/human-agent-authority-map"
---

ERGONOMICS REVIEW MODE: Diagnose causal breakdowns without jumping to preferred solutions.

Create the task model, affected-user map, failure and recovery model, lifecycle risks, and prioritized findings. Separate interface friction, missing capability, reliability failure, organizational failure, and preference disagreement. Severity reflects consequence; confidence reflects evidence strength.

Return to research if a central claim lacks evidence. When causal findings are stable enough to act on, activate `ergonomics-recommend` automatically.
