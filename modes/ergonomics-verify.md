---
mode:
  name: ergonomics-verify
  description: Adversarially verify evidence, conformance boundaries, recommendations, and validation readiness
  shortcut: ergonomics-verify
  advertised: true
  default_action: block
  allowed_transitions: [ergonomics-recommend, ergonomics-finish]
  allow_clear: true
  tools:
    safe: [read_file, glob, grep, web_search, web_fetch, load_skill, todo, delegate, recipes, python_check, LSP]
    warn: [bash]
  contributes:
    agents:
      evidence-researcher:
        source: "@ux-ergonomist:agents/evidence-researcher"
      accessibility-auditor:
        source: "@ux-ergonomist:agents/accessibility-auditor"
    context:
      - "@ux-ergonomist:context/workflow-orientation.md"
      - "@ux-ergonomist:context/knowledge/adversarial-ergonomics.md"
      - "@ux-ergonomist:context/knowledge/evaluation-playbook.md"
    skills:
      - "@ux-ergonomist:skills/ergonomics-verification"
---

ERGONOMICS VERIFY MODE: Try to disprove the findings and recommendations before handoff.

Check source support, applicability, alternative explanations, missing affected users, accessibility claim boundaries, human-agent failure paths, lifecycle effects, acceptance-criterion observability, and study validity. Record PASS, REVISE, or BLOCKED with evidence.

Return to recommend when correction is needed. Activate `ergonomics-finish` automatically only when no material unsupported claim remains.
