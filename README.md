# TBS SPATA5

Znalostní centrum o vzácné genetické nemoci SPATA5 a o českém výzkumu
genové terapie. (Knowledge center about the rare SPATA5 disease and the
Czech gene therapy research.)

Nemoc SPATA5 způsobuje porucha genu AFG2A. V Česku ji má jen několik dětí.
Jejich rodiče založili spolek [SPATA5 CZ](https://www.zazracnedeti.cz/) a
zaplatili start výzkumu v Českém centru pro fenogenomiku. Tento repozitář
sbírá vše, co o nemoci a výzkumu víme, a prezentuje to jako přehledný web.

## Co v repozitáři je

- `data/`: znalostní vault (Obsidian). Jediný zdroj pravdy pro veškerý
  obsah. Každý článek má frontmatter, odkazy `[[wikilink]]` a sekci Zdroje
  s primárními prameny (PMID, DOI, OMIM, Orphanet).
- `web/`: statický web vygenerovaný z vaultu. Design Atlas: levé sbalovací
  menu, světlý i tmavý režim, barvy spolku. Podrobnosti ve složce
  [web/_documentation](web/_documentation/).
- `CLAUDE.md`: pravidla pro veškerý další vývoj.

## Zásada číslo jedna: ověřená fakta

Vault popisuje skutečnou nemoc a skutečný výzkum. Každé tvrzení musí mít
zdroj. Cokoli neověřeného nese značku `⚠ OVĚŘIT` s poznámkou, odkud údaj
pochází a co je potřeba dohledat. Web tyto značky zvýrazňuje, aby čtenář
vždy viděl, kde si nejsme jistí.

## Jak web vygenerovat a prohlédnout

```bash
python3 web/build.py
```

```bash
python3 -m http.server 8741 -d web
```

Pak otevřete http://localhost:8741. Stačí Python 3, nic dalšího se
neinstaluje.

## Obsah vaultu

Nemoc a věda (příznaky, gen, diagnostika, světový výzkum), český výzkum
(projekt v CCP, fáze a financování), lidé, organizace a pacienti, média a
zdroje. Mapa celého grafu je v `data/INDEX.md` a na úvodní stránce webu.
