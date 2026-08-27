# Features

Every user-facing feature of the knowledge center and how it works.

## Left menu with fold-out groups

Native `<details>`/`<summary>` accordion, one group per vault section.
The group holding the current article opens on its own and the article is
highlighted. Everything else stays rolled up. On the home page all groups
start closed. Group membership and order come from build.py (GROUPS map
plus INDEX.md order).

## Theme slider

A sun/moon switch at the bottom of the sidebar. Default follows the system
theme. A click flips the theme and remembers the choice in the browser.
Details in design.md.

## Wikilink navigation

`[[wikilinks]]` in the vault become links between pages, labeled with the
target article's title. A broken wikilink fails the build, so every link
on the site is guaranteed to lead somewhere.

## Sources and verification flags

Ground truth matters more than anything else on this site. The vault keeps
a "Zdroje" section in each article with the primary sources (PubMed PMID,
DOI, OMIM, Orphanet, press URLs). The generator renders bare URLs as
clickable links, so every claim stays one click from its source. Any fact
that is not verified, or that should be re-verified, carries the
`⚠ OVĚŘIT` marker, which the site renders as a highlighted flag. This is
mandatory for all content, per rule 0 in CLAUDE.md. Never strip sources
or verification flags when editing content.

The article `overit-flags` (menu group "Analýzy & To do") collects every
open `⚠ OVĚŘIT` flag in one place, grouped by kind, with a wikilink to
each source article. It is maintained by hand. When a flag is resolved,
fix the source article, remove the marker there, and delete the matching
row on the overview page. The page describes this workflow itself.

## Term explanations (info popovers)

Paragraphs, lists, and tables that use specialist terminology carry a small
orange circled "i" button. For a paragraph it sits inline at the end of the
text; for a list or table it sits on its own line right below. The button is
slightly dimmed and brightens on hover to signal it is interactive. A click
opens a modal window titled "Vysvětlení pojmů" with short plain-Czech
explanations of the terms used in that block. The window stays open until
the reader clicks the circled X in its top right corner, clicks outside the
window, or presses Escape.

Authoring: in the vault, add one line per term directly after the block,
starting with `> ℹ` (a blockquote with the info character, so Obsidian
renders it readably). Example:

```
> ℹ **Axon** je dlouhé vlákno nervové buňky. Vede signály k dalším buňkám.
```

Consecutive `> ℹ` lines merge into one window. build.py converts them into
the button plus a native `<dialog>` element (opened with `showModal()`, so
Escape and focus handling come from the browser). The button carries
`aria-haspopup="dialog"` and `aria-controls`; open/close logic lives in
`app.js`. Explanations are dictionary-level definitions only. Claims that go
beyond a definition belong in the article body with a source, per rule 0.

## Timestamps

- Footer of every page: "Web vygenerován YYYY-MM-DD HH:MM", stamped at
  build time.
- Article header: "Rešerše: <datum-reserse>. Poslední změna: <git date>."
  The research date is the frontmatter value. The change date is the
  file's last git commit (or mtime when uncommitted).
- Home page: "Poslední změny", the 10 most recently changed articles with
  dates, newest first.

## Recent changes list

Generated on the home page from the per-file git dates. Shows which
knowledge is newest without opening articles.

## Tables and long content

Vault tables render as styled HTML tables inside a horizontally scrollable
wrapper, so wide data never breaks the page on narrow screens.

## Responsive layout

Under 860 px the sidebar stacks above the content. No horizontal page
scroll at any width.
