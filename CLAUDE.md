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

## Rules for all future work

0. **Ground truth first.** The vault documents a real disease and real
   research. Every factual claim in `data/` must be backed by a source in
   the article's "Zdroje" section (PMID, DOI, OMIM, Orphanet, or a press
   URL). Never invent, embellish, or round facts. A claim that cannot be
   verified in a primary source gets the `⚠ OVĚŘIT` marker with a note on
   where the number came from. Never delete sources or verification flags.
   When updating content, re-check the source still says what we claim.
1. Content changes happen in `data/`, never by editing generated HTML.
   After any vault change, run `python3 web/build.py` and commit the output.
2. Every new feature or improvement must be documented in
   `web/_documentation/` in the same PR that ships it. New doc files get
   linked from this file.
3. All styling lives in `web/styles.css` as token-based rules. No inline
   styles, no per-page style blocks, no new colors outside the token list
   in design.md.
4. Every page and view gets its own URL when it is introduced.
5. Website text is Czech, written in short plain sentences.
6. Work on branches in worktrees, land via PR. Never commit to main.
