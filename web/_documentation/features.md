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
