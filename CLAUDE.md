# TBS_SPATA5

Knowledge base about the SPATA5 disease and the Czech research project, plus a
static website that presents it.

## Layout

- `data/` is the Obsidian vault. It is the single source of truth for all
  content. Articles use frontmatter (`id`, `typ`, `nazev`, `datum-reserse`)
  and `[[wikilinks]]`. `data/INDEX.md` defines the reading order.
- `web/` is the generated website plus its generator. See
  [web/_documentation/architecture.md](web/_documentation/architecture.md).
- `web/_documentation/` holds all developer documentation:
  - [architecture.md](web/_documentation/architecture.md): build pipeline, file layout, URL scheme
  - [design.md](web/_documentation/design.md): design system, tokens, dark mode, brand colors
  - [features.md](web/_documentation/features.md): every user-facing feature and how it works
  - [content.md](web/_documentation/content.md): language, tone, and register rules for all text

## Rules for all future work

0. **Ground truth first, triple check everything.** The vault documents a
   real disease and real research. Every factual claim in `data/` must be
   backed by a source in the article's "Zdroje" section (PMID, DOI, OMIM,
   Orphanet, or a press URL). Never invent, embellish, or round facts.
   Any fact or information that is not verified, or that should be
   re-verified, always gets the `⚠ OVĚŘIT` marker with a note on where it
   came from and what to check. This applies to every kind of content:
   numbers, dates, names, quotes, claims about people or organizations.
   When in doubt, flag it. Before publishing a fact without the marker,
   verify it three times: the claim matches the cited source, the source
   is primary (or the best available), and the number or wording was
   copied exactly. Never delete sources or verification flags. When
   updating content, re-check that the source still says what we claim.
   **Dual-agent verification (mandatory).** Before any PR that adds or
   changes factual claims, data, or statistics in `data/` is opened,
   launch two fresh, independent agents (Agent tool), each verifying
   every touched claim from scratch against its cited source — neither
   agent sees the other's findings or this conversation's reasoning.
   Each agent reports per claim: matches source / mismatch / source not
   found. Any disagreement between the agents, or any mismatch, blocks
   the PR until resolved or the claim gets the `⚠ OVĚŘIT` marker.
1. Content changes happen in `data/`, never by editing generated HTML.
   After any vault change, run `python3 web/build.py` and commit the output.
2. Every new feature or improvement must be documented in
   `web/_documentation/` in the same PR that ships it. New doc files get
   linked from this file.
3. All styling lives in `web/assets/styles.css` as token-based rules. No inline
   styles, no per-page style blocks, no new colors outside the token list
   in design.md.
4. Every page and view gets its own URL when it is introduced.
5. All text (vault and website) is Czech, written in short plain sentences
   in a professional register. The audience is professionals: researchers,
   clinicians, association representatives, donors. No colloquial phrasing,
   no marketing tone, no cute headings. Precise domain terminology is
   welcome. Full rules with examples:
   [content.md](web/_documentation/content.md).
6. Work on branches in worktrees, land via PR. Never commit to main.
