# Ergonomics lenses

Use these as diagnostic lenses, not a checklist that forces findings.

## Task and workflow fit

- Is the user's goal represented directly, or translated into system-shaped work?
- Are prerequisites, dependencies, ownership, and completion conditions visible?
- Does the interaction preserve continuity across interruptions and handoffs?
- Is effort placed where judgment matters, or wasted on transcription and coordination?

## Mental model and information architecture

- Can users predict what will happen before acting?
- Do labels, grouping, navigation, and system boundaries match the user's concepts?
- Is hidden state exposed at the point where it changes decisions?
- Does the interface rely on recall when recognition is possible?

## Cognitive ergonomics

- Working-memory load, task switching, divided attention, vigilance, uncertainty, and decision density.
- Progressive disclosure should hide incidental complexity without concealing consequence.
- Defaults should reduce routine effort without silently changing ownership or risk.
- Consistency is valuable when it improves transfer, not when it preserves a bad pattern.

## Perceptual and motor ergonomics

- Legibility, contrast, hierarchy, grouping, target size, target spacing, reach, pointer travel, keyboard effort, motion, timing, and environmental constraints.
- Evaluate across viewport, zoom, orientation, input mode, and assistive technology.
- Do not infer accessibility from appearance alone.

## Feedback, control, and recovery

- Every meaningful action needs timely, proportional feedback.
- Destructive or consequential actions need clear scope and recoverability.
- Errors should preserve user work, identify the failed object and cause when known, and offer a viable next action.
- Status messages must be perceivable without stealing focus.

## Human-AI fit

- What does the system know, infer, remember, decide, and do?
- What can the user inspect, edit, approve, interrupt, reverse, and verify?
- Is confidence communicated in a way users can interpret and act on?
- Does the design reduce automation bias and complacency without imposing alert fatigue?
- Is authority allocated according to risk, reversibility, expertise, and user preference?

## Social and organizational ergonomics

- Role clarity, collaboration, handoffs, accountability, privacy, surveillance effects, and incentive compatibility.
- Local efficiency can create downstream coordination cost. Evaluate the whole service journey.
- Accessibility work must include procurement, content, support, and operational ownership where relevant.

## Severity model

- **S0 Note:** no demonstrated task impact.
- **S1 Minor:** friction or delay with an obvious recovery.
- **S2 Moderate:** repeated error, meaningful delay, exclusion for some users, or avoidable support burden.
- **S3 Major:** task failure, loss of work, serious exclusion, or high-probability harmful decision.
- **S4 Critical:** safety, legal, financial, privacy, security, or irreversible harm requiring immediate containment.

Severity is consequence, not visual ugliness. Report confidence separately.
