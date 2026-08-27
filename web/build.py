#!/usr/bin/env python3
"""Generate the SPATA5 knowledge center from the Obsidian vault in ../data.

Usage: python3 build.py   (from the web/ directory, or anywhere)
Reads data/**/*.md, writes one HTML page per article plus index.html into
web/dist/, and copies web/assets/ there so dist/ is hostable as-is.
Fails if any [[wikilink]] points to a document that does not exist.
"""
import datetime
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

WEB = Path(__file__).resolve().parent
DATA = WEB.parent / "data"
ASSETS = WEB / "assets"
OUT = WEB / "dist"

GROUPS = [
    ("Nemoc a věda", ["00-nemoc"]),
    ("Český výzkum", ["01-cesky-vyzkum"]),
    ("Lidé", ["02-lide"]),
    ("Organizace a pacienti", ["03-organizace", "04-pacienti"]),
    ("Média a zdroje", ["05-media", "06-zdroje"]),
    ("Analýzy", ["07-ai"]),
    ("Inspirace", ["08-inspirace"]),
    ("TO DO", ["09-todo"]),
]

WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def last_changed(path):
    """Date of the file's last git commit, or its mtime for uncommitted files."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(path)],
        capture_output=True, text=True, cwd=DATA.parent).stdout.strip()
    dirty = subprocess.run(
        ["git", "status", "--porcelain", "--", str(path)],
        capture_output=True, text=True, cwd=DATA.parent).stdout.strip()
    if dirty or not out:
        return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()
    return out


def parse_doc(path):
    text = path.read_text(encoding="utf-8")
    meta = {}
    body = text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    m = re.search(r"^# (.+)$", body, re.M)
    title = m.group(1).strip() if m else meta.get("nazev", path.stem)
    return meta, body.strip(), title


def inline(text, slugs):
    """Escape, then resolve wikilinks, markdown links, bold, bare URLs."""
    text = html.escape(text, quote=False)

    def wl(m):
        slug, label = m.group(1), m.group(2)
        if slug not in slugs:
            raise SystemExit(f"CHYBA: [[{slug}]] nikam nevede")
        return f'<a href="{slug}.html">{label or slugs[slug]}</a>'

    text = WIKILINK.sub(wl, text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r'(?<!["=/])(https?://[^\s<]+?)([.,)]*)(?=\s|$)',
                  r'<a href="\1">\1</a>\2', text)
    text = text.replace("⚠ OVĚŘIT", '<span class="verify-flag">⚠ OVĚŘIT</span>')
    return text


def md_to_html(body, slugs):
    lines = body.splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            lang = line[3:].strip()
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            if lang != "mermaid":
                out.append("<pre><code>" + html.escape("\n".join(block)) + "</code></pre>")
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            out.append(f"<h{level}>{inline(line[level:].strip(), slugs)}</h{level}>")
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                rows.append(cells)
                i += 1
            head, rest = rows[0], [r for r in rows[1:] if not set("".join(r)) <= set("-: ")]
            thead = "".join(f"<th>{inline(c, slugs)}</th>" for c in head)
            trs = "".join(
                "<tr>" + "".join(f"<td>{inline(c, slugs)}</td>" for c in r) + "</tr>"
                for r in rest)
            out.append(f'<div class="table-wrap"><table><thead><tr>{thead}</tr></thead>'
                       f"<tbody>{trs}</tbody></table></div>")
            continue
        if line.startswith("- ") or re.match(r"^\d+\. ", line):
            ordered = not line.startswith("- ")
            tag = "ol" if ordered else "ul"
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or re.match(r"^\d+\. ", lines[i])):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]))
                i += 1
            lis = "".join(f"<li>{inline(it, slugs)}</li>" for it in items)
            out.append(f"<{tag}>{lis}</{tag}>")
            continue
        if line.startswith("> "):
            out.append(f"<blockquote>{inline(line[2:], slugs)}</blockquote>")
            i += 1
            continue
        if line.strip():
            out.append(f"<p>{inline(line.strip(), slugs)}</p>")
        i += 1
    return "\n".join(out)


def sidebar(nav, active_slug):
    parts = [f'<a href="index.html"{" class=\"active\"" if active_slug == "index" else ""}>Domů</a>']
    for group, docs in nav:
        is_open = any(slug == active_slug for slug, _ in docs)
        links = "".join(
            f'<a href="{slug}.html"{" class=\"active\"" if slug == active_slug else ""}>{html.escape(t)}</a>'
            for slug, t in docs)
        parts.append(
            f'<details class="nav-group"{" open" if is_open else ""}>'
            f'<summary class="nav-label">{html.escape(group)}</summary>'
            f"<div>{links}</div></details>")
    return "\n".join(parts)


PAGE = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <a class="brand" href="index.html"><span class="brand-name">SPATA<em>5</em></span></a>
    <div class="brand-sub">Znalostní centrum</div>
    <nav class="nav" aria-label="Hlavní navigace">
{nav}
    </nav>
    <button class="theme-toggle" id="themeBtn" type="button" role="switch" aria-checked="false" aria-label="Tmavý režim">
      <svg class="icon sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.6M12 18.9v2.6M2.5 12h2.6M18.9 12h2.6M5.2 5.2l1.9 1.9M16.9 16.9l1.9 1.9M18.8 5.2l-1.9 1.9M7.1 16.9l-1.9 1.9"/></svg>
      <svg class="icon moon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.6 14.8A8.6 8.6 0 0 1 9.2 3.4a8.6 8.6 0 1 0 11.4 11.4Z"/></svg>
      <span class="knob"></span>
    </button>
  </aside>
  <main class="main">
    <div class="content">
      <div class="eyebrow">{eyebrow}</div>
{article}
      <footer class="site-footer">Znalostní báze spolku SPATA5 CZ. {footer_meta}</footer>
    </div>
  </main>
</div>
<script src="app.js"></script>
</body>
</html>
"""


def main():
    OUT.mkdir(exist_ok=True)
    for stale in OUT.glob("*.html"):
        stale.unlink()
    for asset in ASSETS.iterdir():
        shutil.copy2(asset, OUT / asset.name)

    docs = {}
    for path in sorted(DATA.glob("*/*.md")):
        if path.parent.name.startswith("."):
            continue
        meta, body, title = parse_doc(path)
        slug = meta.get("id", path.stem)
        docs[slug] = {"meta": meta, "body": body, "title": title,
                      "folder": path.parent.name, "changed": last_changed(path)}

    index_meta, index_body, index_title = parse_doc(DATA / "INDEX.md")
    index_body = index_body.split("## Vizuální mapa")[0].strip()

    order = [m.group(1) for m in WIKILINK.finditer(index_body)]
    rank = {slug: n for n, slug in enumerate(order)}

    nav = []
    for group, folders in GROUPS:
        members = [(s, d["title"]) for s, d in docs.items() if d["folder"] in folders]
        members.sort(key=lambda st: (rank.get(st[0], 999), st[0]))
        nav.append((group, members))

    slugs = {s: d["title"] for s, d in docs.items()}
    group_of = {s: g for g, members in nav for s, _ in members}

    built = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    footer = f"Web vygenerován {built}."

    for slug, doc in docs.items():
        body = re.sub(r"^# .+$", "", doc["body"], count=1, flags=re.M)
        datum = doc["meta"].get("datum-reserse", "")
        article = (f"<h1>{html.escape(doc['title'])}</h1>\n"
                   f'<p class="article-meta">Rešerše: {datum}. '
                   f'Poslední změna: {doc["changed"]}.</p>\n'
                   + md_to_html(body, slugs))
        page = PAGE.format(title=f"{doc['title']} | SPATA5",
                           nav=sidebar(nav, slug),
                           eyebrow=html.escape(group_of.get(slug, "")),
                           article=article,
                           footer_meta=footer)
        (OUT / f"{slug}.html").write_text(page, encoding="utf-8")

    body = re.sub(r"^# .+$", "", index_body, count=1, flags=re.M)
    newest = sorted(docs.items(), key=lambda sd: sd[1]["changed"], reverse=True)[:10]
    recent = "".join(
        f'<li><a href="{s}.html">{html.escape(d["title"])}</a>'
        f'<span class="recent-date">{d["changed"]}</span></li>'
        for s, d in newest)
    article = (f"<h1>{html.escape(index_title)}</h1>\n"
               + md_to_html(body, slugs)
               + f'\n<h2>Poslední změny</h2>\n<ul class="recent">{recent}</ul>')
    page = PAGE.format(title="SPATA5 Znalostní centrum",
                       nav=sidebar(nav, "index"),
                       eyebrow="Znalostní centrum",
                       article=article,
                       footer_meta=footer)
    (OUT / "index.html").write_text(page, encoding="utf-8")

    in_nav = {s for _, members in nav for s, _ in members}
    missing = set(docs) - in_nav
    assert not missing, f"dokumenty mimo menu: {missing}"
    print(f"OK: {len(docs)} článků + index.html")


if __name__ == "__main__":
    sys.exit(main())
