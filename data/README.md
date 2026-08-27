---
id: readme
typ: navod
nazev: Jak číst tento vault
datum-reserse: 2026-08-26
---

# SPATA5 znalostní vault

Tento adresář shrnuje vše podstatné o vzácném genetickém onemocnění SPATA5 a o českém výzkumu, který iniciovali rodiče nemocných dětí. Je psaný pro nespecialistu a zároveň strukturovaný tak, aby se v něm snadno orientoval i jazykový model (LLM).

Vstupní bod je [INDEX.md](INDEX.md). Obsahuje mapu celého grafu a odkazy na všechny poznámky.

## Konvence

- Každý soubor je jeden uzel znalostního grafu. Jeden soubor drží jedno téma.
- Hlavička souboru (YAML frontmatter) nese `id`, `typ`, `nazev` a `tagy`. Typy uzlů: `nemoc`, `gen`, `osoba`, `organizace`, `projekt`, `pacienti`, `media`, `zdroj`, `analyza`, `navod`.
- Odkazy mezi uzly mají tvar `[[id-uzlu]]` (styl Obsidian). Každá poznámka má na konci sekci **Vazby** se seznamem souvisejících uzlů a popisem vztahu.
- Každý fakt má u sebe zdroj (URL). Sekce **Zdroje** je na konci každé poznámky.
- Nejistoty a rozpory mezi zdroji jsou značené štítkem `⚠ OVĚŘIT` přímo u daného tvrzení. Nic nezamlčujeme a nic nedomýšlíme.

## Struktura složek

```
00-nemoc/          co je SPATA5 onemocnění, gen, diagnostika, léčba, výskyt
01-cesky-vyzkum/   projekt v Českém centru pro fenogenomiku, fáze, financování, RD-Factory
02-lide/           klíčové osoby (Zajíc, Zajícová, Sedláček, Procházka)
03-organizace/     spolek SPATA 5 CZ, CCP, zahraniční pacientské organizace
04-pacienti/       příběhy českých dětí a rodin (veřejně publikované informace)
05-media/          chronologie mediálního pokrytí, klíčový článek HN
06-zdroje/         vědecké publikace (PMID, DOI), databáze (OMIM, Orphanet, ClinVar)
07-ai/             mapování příležitostí pro nasazení AI ve výzkumu
```

## Důležité upozornění

Vault je rešerše veřejných zdrojů ke dni 2026-08-26. Není to lékařská rada. Informace o dětech pocházejí výhradně z veřejně publikovaných příběhů na webu spolku a v médiích.
