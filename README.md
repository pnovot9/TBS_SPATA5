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
- `web/`: statický web vygenerovaný z vaultu. Podrobnosti ve složce
  [web/_documentation](web/_documentation/).
- `_guides/`: příručky pro netechnické spolupracovníky. Začněte souborem
  [introduction_how_to.html](_guides/introduction_how_to.html), otevřete
  ho v prohlížeči.

## Zásada číslo jedna: ověřená fakta

Vault popisuje skutečnou nemoc a skutečný výzkum. Každé tvrzení musí mít
zdroj. Cokoli neověřeného nese značku `⚠ OVĚŘIT` s poznámkou, odkud údaj
pochází a co je potřeba dohledat. Web tyto značky zvýrazňuje, aby čtenář
vždy viděl, kde si nejsme jistí.

## Jak web vygenerovat a prohlédnout

Potřebujete Python 3.7 nebo novější a `git` (skript z něj čte data
posledních změn). Nic se neinstaluje, žádné knihovny navíc, žádný Node.

Vygenerujte web z vaultu:

```bash
python3 web/build.py
```

Skript vypíše, kolik článků vytvořil. Spustit jde z libovolné složky.

Spusťte lokální server:

```bash
python3 -m http.server 8741 -d web
```

Pak otevřete http://localhost:8741.

## K čemu je build.py

`web/build.py` je celý generátor webu. Přečte všechny soubory `data/**/*.md`,
z každého článku udělá jednu stránku `web/<slug>.html` a k tomu složí
`web/index.html` s menu a seznamem posledních změn. Odkazy `[[wikilink]]`
převede na odkazy mezi stránkami. Datum poslední změny bere z historie gitu.

Skript hlídá dvě věci a při chybě skončí: `[[wikilink]]` musí mířit na
existující dokument a každý článek musí patřit do některé skupiny v menu.

Spouštějte ho po každé změně v `data/`. Vygenerované HTML pak patří do
stejného commitu jako změna vaultu. Ručně se HTML soubory neupravují,
příští build je přepíše. Když měníte jen `web/styles.css` nebo
`web/app.js`, build potřeba není.

## Obsah vaultu

Nemoc a věda (příznaky, gen, diagnostika, světový výzkum), český výzkum
(projekt v CCP, fáze a financování), lidé, organizace a pacienti, média a
zdroje. Mapa celého grafu je v `data/INDEX.md` a na úvodní stránce webu.

## About

Popis repozitáře na GitHubu:

> Znalostní centrum o vzácné nemoci SPATA5 a o českém výzkumu genové terapie.
> Obsidian vault je zdroj pravdy, skript z něj generuje statický web.

---

TBS v názvu znamená "To Be Solved".
