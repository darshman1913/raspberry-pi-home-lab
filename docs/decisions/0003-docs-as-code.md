# 0003 - Docs Are a Build Artifact

**Status:** Accepted

**Date:** 2026-10-18

## Context

Each project was documented in one long README. They got long. The Pi-hole one mixed setup steps, command lists, version tables, and explanations of how DNS works all on one page. That made it hard to find one command or one IP without scrolling through everything.

I also wanted a site I could link to from a resume that looks like real documentation and not just a repo.

## Decision

The docs are markdown files in `docs/`, split into tutorials, how-to guides, reference, explanation, and this decision log. Zensical builds them into a static site using `zensical.toml`. GitHub Actions builds and publishes the site to GitHub Pages on every push to `main`.

The published site is at <https://darshman1913.github.io/raspberry-pi-home-lab/>.

## Consequences

* The markdown is still the source. It still reads on GitHub, and the site is generated from it.
* Docs changes go through git like code. History is kept, and I used `git mv` for the move so the original README history follows the files.
* The project folders now only hold short README stubs that point at the site.
* There is one more thing that can break. If the build fails, the site does not update.
* Everything stays free. Zensical is open source and GitHub Pages is free for public repos.

## Alternatives considered

* **GitHub wiki.** Free and built in, but it lives outside the main repo history and has no real structure or search.
* **Notion.** Easy to write in, but the content lives in someone else's service and does not sit next to the code and configs.
* **README only.** What I had. Fine for one project, but it does not scale to seven.
