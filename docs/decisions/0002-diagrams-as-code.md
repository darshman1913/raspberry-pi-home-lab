# 0002 - Diagrams Are Python Files

**Status:** Accepted

**Date:** 2026-10-18

## Context

The three project READMEs had ASCII network diagrams in code blocks. They were readable on GitHub but painful to update. Every time the lab changes, the diagrams have to change too, and with ASCII that meant redrawing lines by hand. Moving the docs into a real site was a good point to fix this.

## Decision

Each network diagram is a Python file in `docs/assets/diagrams/` that uses the `diagrams` library and Graphviz. Running the file renders a PNG next to it. The PNG is committed and the tutorial pages show it.

The old ASCII version stays in each tutorial inside a collapsed `<details>` block.

## Consequences

* Diagram changes show up as readable text diffs in git.
* Updating a diagram is editing a line and re-running one command.
* Rendering needs Python, the `diagrams` package, and Graphviz installed. Graphviz is not a pip package, so it is a separate install on Windows.
* The PNG can go stale if I edit the `.py` file and forget to render. The GitHub Actions workflow does not render diagrams, it only builds the site.

More on the reasoning in [Why the diagrams are code](../explanation/why-diagrams-are-code.md).

## Alternatives considered

* **Keep the ASCII art.** Zero tools needed, but hard to edit and it looks rough on the published site.
* **Hand-drawn PNG.** Looks good, but every change needs an image editor and git can only tell me the file changed, not what changed.
* **Mermaid.** Text based and renders on GitHub. The built-in shapes are mostly boxes and arrows, and proper router and device icons need extra icon packs that GitHub does not load.
