# Architecture

The website is a static site generated from the Obsidian vault in `data/`.
No framework, no dependencies, no server-side code. Python 3 standard
library only.

## Data flow

```
data/**/*.md  ->  web/build.py  ->  web/dist/*.html
data/INDEX.md ->                ->  web/dist/index.html
web/assets/*  ->                ->  web/dist/*  (copied)
```

Run `python3 web/build.py` from anywhere. It rewrites every generated page
and copies the assets. Generated output is committed, so the site can be
hosted from the `web/dist/` folder as plain files.

## What build.py does

1. Reads every `data/*/*.md` (hidden folders like `.obsidian` are skipped).
2. Parses frontmatter (`id`, `typ`, `nazev`, `datum-reserse`). The `id`
   becomes the page slug and the URL: `<id>.html`.
3. The article title is the markdown H1, with `nazev` as fallback.
4. Converts the markdown subset the vault actually uses: h1 to h3, bullet
   and numbered lists, tables, bold, blockquotes, fenced code, bare URLs,
   and `[text](url)` links. Mermaid code fences are dropped.
5. Resolves `[[wikilink]]` to `<a href="slug.html">Article title</a>`.
   A wikilink that points to no document stops the build with an error.
   This keeps the site and the vault in sync.
6. Builds the left menu per page. Groups map from vault folders (see
   GROUPS in build.py). Order inside a group follows the first appearance
   of each article in `INDEX.md`.
7. Reads each file's last-change date from git (`git log -1 --format=%cs`).
   Uncommitted files fall back to file modification time.
8. Writes `index.html` from `INDEX.md` (the mermaid map section is cut)
   and appends a recent-changes list of the 10 newest articles.
9. Self-check at the end: every document must appear in the menu.

## File layout

- `web/build.py`: the whole generator, one file.
- `web/assets/styles.css`: the only stylesheet. See design.md.
- `web/assets/app.js`: the only script. Theme toggle logic.
- `web/dist/`: the generated site. Pages plus copies of the assets.
  Never edit by hand.
- `web/designs/`: the four original design prototypes, kept for reference.
  They are standalone files and not part of the generated site.
- `web/_documentation/`: this documentation.

## URL scheme

Flat. One article equals one page equals one URL: `<vault id>.html`.
`index.html` is the home page. Asset links are relative, which works
because every page sits in `web/dist/` next to the copied assets.

## Local preview

```bash
python3 -m http.server 8741 -d web/dist
```

Then open http://localhost:8741.

## Deployment

The site is published at https://pnovot9.github.io/TBS_SPATA5/ through
GitHub Pages. The workflow `.github/workflows/pages.yml` runs on every
push to `main` and uploads the committed `web/dist/` folder as it is.
There is no build step in CI. The committed output is the deployed site,
so `python3 web/build.py` must run before commit, as rule 1 in CLAUDE.md
already requires. All links are relative, which is why the same files
work on Pages, over `file://`, and on a local server.
