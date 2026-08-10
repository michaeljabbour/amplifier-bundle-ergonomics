---
mode:
  name: ergonomics-research
  description: Gather and grade product evidence, standards, research, and current user signal
  shortcut: ergonomics-research
  advertised: true
  default_action: block
  allowed_transitions: [ergonomics-frame, ergonomics-review]
  allow_clear: true
  tools:
    safe: [read_file, glob, grep, web_search, web_fetch, load_skill, todo, delegate, recipes]
  contributes:
    agents:
      evidence-researcher:
        source: "@ux-ergonomist:agents/evidence-researcher"
    context:
      - "@ux-ergonomist:context/workflow-orientation.md"
      - "@ux-ergonomist:context/knowledge/source-policy.md"
    skills:
      - "@ux-ergonomist:skills/ux-evidence-synthesis"
---

ERGONOMICS RESEARCH MODE: Build the evidence base for the framed decision.

Separate direct product evidence, external research, standards, expert inspection, anecdotes, and hypotheses. Record source applicability and limitations. Use public posts for vocabulary and leads, not prevalence.

Return to `ergonomics-frame` if the evidence question is malformed. When the evidence map is decision-usable, activate `ergonomics-review` automatically. Pause when a required source is unavailable or evidence creates a new consequential choice.
