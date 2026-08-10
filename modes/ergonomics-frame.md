---
mode:
  name: ergonomics-frame
  description: Frame the people, task, context, outcome, constraints, evidence, and failure cost
  shortcut: ergonomics-frame
  advertised: true
  default_action: block
  allowed_transitions: [ergonomics-research]
  allow_clear: true
  tools:
    safe: [read_file, glob, grep, web_search, web_fetch, load_skill, todo, delegate, recipes]
  contributes:
    agents:
      ux-ergonomist:
        source: "@ux-ergonomist:agents/ux-ergonomist"
    context:
      - "@ux-ergonomist:context/workflow-orientation.md"
    skills:
      - "@ux-ergonomist:skills/task-analysis"
---

ERGONOMICS FRAME MODE: Establish the decision frame before diagnosing or proposing changes.

Produce a frame containing: target users, primary job, context of use, business outcome, constraints, available evidence, failure cost, assumptions, and decision question.

Do not diagnose from an incomplete description when the actual product state is inspectable. Do not recommend solutions in this phase.

When the frame is sufficient to guide evidence collection, call the `mode` tool to activate `ergonomics-research` and briefly explain the transition. Pause only for a material ambiguity or required access.
