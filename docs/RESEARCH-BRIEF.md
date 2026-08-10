# Research brief: an Amplifier-native UX ergonomist

Date: 2026-08-10

## Executive read

The strongest opportunity is not another agent that makes interfaces look polished. Microsoft already has an Amplifier design-intelligence bundle centered on visual and component craft. The missing capability is an evidence-led expert that judges whether a product fits its users, tasks, abilities, risks, and organizational setting. Recent human-agent research converges on user control, explainability of activity, editable intent and plans, calibrated trust, recovery, and visible completion. Established HCI and accessibility work adds task success, mental models, cognitive load, error prevention, inclusive operation, and measurement discipline. Public X posts are useful for surfacing fast-moving patterns and vocabulary, but are too anecdotal to establish prevalence or causal claims. The proposed `ux-ergonomist` is therefore a single context-sink expert agent with a thin composable behavior, a rigorous evidence ladder, and explicit output and validation contracts.

## Product position

**Job:** Help a team turn a product, workflow, or agent-experience question into an evidence-backed design decision and a falsifiable validation plan.

**Primary users:** product designers, UX researchers, PMs, engineers, accessibility specialists, and AI-agent builders.

**Owns:** human factors, cognitive ergonomics, task and workflow fit, information architecture, accessibility, research synthesis, human-AI interaction, UX evaluation, and acceptance criteria.

**Does not own:** art direction, visual identity, detailed component styling, production motion, or frontend implementation. Those should compose with `amplifier-bundle-design-intelligence` rather than be duplicated.

## Evidence synthesis

### 1. Human-agent UX needs a different control model

Traditional interfaces are mostly deterministic and directly manipulated. Agents introduce inferred intent, hidden plans, long-running activity, uncertainty, and delegated authority. Current research on computer-use agents identifies prompts, explanation of activity, user control, mental models, task preview, and end-of-task indicators as core design areas. Workplace-agent research likewise emphasizes controllability, transparency, explainability, privacy, and collaboration. This supports a mandatory agent-interaction review covering scope, plan, progress, intervention, undo, provenance, and completion evidence.

### 2. Appropriate trust is the goal

Maximizing trust is unsafe. Users need enough information to predict behavior, verify consequential outputs, and intervene without being buried in low-value confirmation. The agent therefore calibrates approval gates to consequence and reversibility and explicitly checks for automation bias, overreliance, and alert fatigue.

### 3. Expert review is useful but epistemically limited

Heuristic reviews and cognitive walkthroughs can identify plausible defects quickly. They cannot prove frequency, explain every failure, or substitute for testing with affected users. The bundle encodes an evidence ladder so recommendations expose whether they arise from direct product evidence, external research, expert inspection, anecdote, or hypothesis.

### 4. Accessibility is broader than a conformance scan

WCAG 2.2 and ARIA practices provide essential normative grounding, but inclusive UX also requires manual operation, cognitive clarity, assistive-technology behavior, recovery, and testing with affected users. The agent treats automated scanning as one input and refuses to claim full conformance without suitable evidence.

### 5. UX advice must end in a decision and a test

Generic principles rarely change a roadmap. Each recommendation needs a causal mechanism, trade-off, expected outcome, and observable acceptance criterion. The evaluation playbook maps product questions to methods and discourages invented benchmarks or arbitrary sample-size rules.

## X and practitioner signal

The public scan showed recurring claims around screenshot-derived UI generation, automated design review, WCAG compliance, human-agent handoffs, and the idea that AI review supplements rather than replaces usability testing. These signals are directionally useful, especially for identifying what practitioners are trying now. They remain E4 anecdotal evidence unless corroborated. The bundle uses X as a discovery surface, not an authority layer.

## Architecture decision

Use one broad expert rather than many narrow agents in v0.1. The work is diagnostically coupled: task analysis changes accessibility interpretation; human-AI authority changes recovery design; research strength changes recommendation confidence. Splitting too early increases coordination cost and creates false certainty at handoffs. Heavy knowledge files load only when the expert is delegated to, following Amplifier's context-sink pattern.

## Core workflow

1. Frame the user, task, context, outcome, constraints, and failure cost.
2. Inspect the actual product evidence.
3. Build a task and failure model.
4. Diagnose using ergonomic lenses.
5. Prioritize by consequence and confidence.
6. Recommend the smallest causal intervention.
7. Define acceptance criteria and the lightest valid test.

## Evaluation plan for the agent itself

Create a benchmark set with at least these case families:

- onboarding abandonment with incomplete analytics
- inaccessible modal and keyboard trap
- high-stakes agent action with inadequate approval and undo
- low-risk repetitive workflow with excessive confirmations
- conflicting qualitative anecdotes and telemetry
- visually polished flow with poor information architecture
- user request that actually belongs to visual design specialists

Blind-review outputs against: evidence calibration, causal diagnosis, prioritization, accessibility coverage, human-AI control coverage, actionability, validation quality, and scope discipline. Include adversarial cases where the correct behavior is to state that evidence is insufficient. Compare against a general agent and the design-intelligence bundle. Track false claims as a hard guardrail, not a soft score.

## Sources

- Microsoft Amplifier Foundation, Bundle Authoring Guide: https://github.com/microsoft/amplifier-foundation/blob/main/docs/BUNDLE_GUIDE.md
- Microsoft Amplifier Foundation, Agent Authoring Guide: https://github.com/microsoft/amplifier-foundation/blob/main/docs/AGENT_AUTHORING.md
- Microsoft Amplifier Design Intelligence bundle: https://github.com/microsoft/amplifier-bundle-design-intelligence
- Amershi et al. (2019), Guidelines for Human-AI Interaction: https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- W3C, WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Cheng et al. (2026), Mapping the Design Space of User Experience for Computer Use Agents: https://arxiv.org/abs/2602.07283
- Paimann et al. (2026), A Framework of User Experience Principles for Human-AI Agent Interaction in the Workplace: https://arxiv.org/abs/2607.19941
- Imagining Design Workflows in Agentic AI Futures (2025): https://arxiv.org/abs/2509.20731
- ADEPTS: A Capability Framework for Human-Centered Agent Design (2025): https://arxiv.org/abs/2507.15885

## Known limitations

- X indexing is incomplete and can overrepresent promotional accounts and recent posts.
- Several 2025-2026 agent-UX frameworks are preprints or formative studies with small samples.
- ISO 9241 material is relevant but not embedded because the normative text is not freely reproducible.
- The bundle is structurally designed from current Amplifier documentation but has not yet been run through Amplifier's repository validation recipe in this workspace.
