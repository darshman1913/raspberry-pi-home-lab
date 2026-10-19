# Why the Diagrams Are Code

The first three writeups used ASCII diagrams inside code blocks. They looked fine on GitHub, but they were hard to keep accurate. Moving one box meant redrawing half the lines by hand.

When I moved the docs into this site, I replaced them with Python files in `docs/assets/diagrams/`. Each file uses the `diagrams` library and Graphviz to render a PNG next to it, and the tutorial pages show the PNG.

There were three reasons.

**Diffs are readable.** A change to the network shows up in git as a changed line, like a new label or a new edge. A changed PNG on its own just shows up as a binary file that changed, with no way to see what moved.

**The diagram matches reality after changes.** When I change something in the lab, I edit one line in the Python file and render it again. Redrawing is no longer annoying enough to skip, so the diagram does not drift away from the real setup.

**No binary editor needed.** No draw.io file, no Visio, nothing paid. Everything is free and runs on my Windows laptop.

## Rendering a diagram

Graphviz has to be installed. I used:

```powershell
winget install --id Graphviz.Graphviz -e
```

Then from the diagrams folder, with the virtual environment active:

```powershell
cd docs\assets\diagrams
python 01-pihole-topology.py
```

The PNG shows up next to the `.py` file. If Python says it cannot find `dot`, add `C:\Program Files\Graphviz\bin` to PATH. I had to do that in the shell I was using right after the install.

The rendered PNGs are committed, so GitHub shows them without anyone running anything. The original ASCII version is still in each tutorial inside a collapsed block for anyone reading the raw markdown.
