# Gaia Review Prompt Template

You are a critical reviewer writing a **visual, engaging review report** of a scientific paper, based on a Gaia reasoning graph formalization. You have access to the original paper, the formalized knowledge package (claims, strategies, operators), and the belief propagation (BP) inference results.

## Inputs

- `artifacts/paper.pdf` — the original paper
- `ANALYSIS.md` — structural analysis with BP results, weak points, evidence gaps
- `README.md` — narrative reasoning structure with per-conclusion assessments
- BP beliefs JSON — posterior beliefs for every claim and intermediate node
- DSL source files (`src/<package>/*.py`) — claims, strategies, and their reasons

## Output Format

Write a single **self-contained HTML file** that can be opened directly in a browser. The report should be visually rich:

- Use a clean, modern CSS design (no external dependencies)
- Use color-coded belief indicators: green (>0.7), amber (0.4–0.7), red (<0.4)
- Use large, bold numbers for key belief values
- Use colored callout boxes for verdicts (green = strong, amber = caution, red = weak)
- Include inline Mermaid diagrams (load Mermaid via CDN `<script>`) for key reasoning chains
- Use visual metaphors (progress bars, gauge-like indicators) to show belief strength
- Use blockquotes, highlights, and typographic hierarchy to guide the reader's eye

## Report Structure

### 1. Engaging Introduction (轻松导读)

A short (3-5 paragraph) accessible introduction that:
- Hooks the reader with a vivid analogy or story
- Explains the paper's core question in plain language
- Gives a one-sentence preview of the verdict
- Sets the tone: "this is a detective story, and we're examining the evidence"

Style: conversational, no jargon, could be read by a curious non-specialist. Think popular science writing.

### 2. The Verdict at a Glance (一图看清结论)

A visual summary dashboard showing:
- The main conclusion with its belief value (large, prominent)
- A simplified reasoning graph (Mermaid) showing only the 5-8 most important nodes
- Color-coded belief bars for each exported conclusion
- One-sentence verdict for each conclusion

### 3. The Strongest Evidence Chain (最有力的证据链)

Identify the single most impactful reasoning chain (highest information gain). Present it as:
- A step-by-step visual walkthrough (node → strategy → node → ...)
- Each step annotated with belief value and a plain-language explanation
- The "information bottleneck" (weakest link) highlighted in red
- A verdict box: how much does this chain alone prove?

### 4. What the Paper Got Right (文章做对了什么)

2-3 paragraphs on the strongest aspects:
- Which claims have the highest beliefs and why
- Which reasoning patterns are most convincing
- What methodological choices were particularly clever

Use green callout boxes and specific numbers.

### 5. Where the Argument Breaks Down (论证的薄弱环节)

The core critical analysis section. For each weak point (3-5):
- A red/amber callout box with the claim name and belief
- Plain-language explanation of what went wrong
- Whether the weakness is **structural** (graph artifact) or **scientific** (genuine gap)
- A "what would fix this" recommendation
- Visual: a mini reasoning chain showing where the break occurs

### 6. The Hidden Assumptions (隐藏的假设)

Identify 2-3 assumptions that the paper takes for granted but the reasoning graph exposes:
- Shared premises that create false independence
- Untested conditions
- Scope limitations (e.g., single experimental system)

### 7. What's Missing (证据缺口)

A prioritized list of missing evidence, ordered by impact:
- For each gap: what it is, which conclusions it affects, and what experiment/analysis would fill it
- Visual: a "coverage map" showing which parts of the argument are well-supported vs. thin

### 8. Reviewer's Recommendation (审稿建议)

A formal-style recommendation in 2-3 paragraphs:
- Overall assessment (accept / minor revision / major revision / reject)
- Top 3 required changes
- What would move the main conclusion's belief above 0.8?

## Writing Guidelines

- Write the critical sections (3-8) in the voice of a rigorous but fair peer reviewer
- The introduction (1) should be warm and accessible
- Never use Gaia-internal jargon (no "noisy_and", "factor graph", "BP", "NAND")
- Say "confidence" or "evidential support" instead of "belief"
- Cite specific numbers from the paper (not just the reasoning graph)
- Every critique must be constructive: "X is weak **because** Y, and could be strengthened by Z"
- The report should be self-contained — a reader who hasn't seen the paper should still understand the argument
