# Obsah a tón

Pravidla pro veškerý text ve vaultu (`data/`) a na webu. Čtenáři jsou
profesionálové: vědci, lékaři, zástupci spolku a dárci.

## Jazyk

- Čeština, krátké věty, jedna myšlenka na větu.
- Odborné termíny se používají přesně (repurposing, knockout, fenotyp,
  longitudinální data). Nevysvětlujeme je opisem, kde je čtenář zná.
- Odborné termíny v odstavci vysvětlují řádky `> ℹ` hned pod ním. Web z
  nich vytvoří tlačítko s vysvětlivkami (viz features.md). Vysvětlení jsou
  krátké slovníkové definice bez čísel a bez tvrzení, která by potřebovala
  zdroj. Delší kontext a vztah pojmu k nemoci patří do souboru
  `data/09-todo/slovnik-rozsireni.md` (viz features.md), kde každé tvrzení
  kryje zdroj.
- Každý nový pojem `> ℹ` dostává ve stejném PR i záznam v
  `slovnik-rozsireni.md` s kontextem a odstavcem `**Vztah k nemoci:**`.
  Odstavec vztahu se vynechá jen tam, kde pojem k nemoci žádný vztah
  nemá. Pravidlo 7 v [CLAUDE.md](../../CLAUDE.md).
- Bez pomlček uvnitř vět a bez středníků. Dvě věty místo jedné dlouhé.

## Rejstřík

Věcný a formální. Žádné hovorové obraty, hodnotící zkratky ani reklamní tón.

| Nevhodné | Správně |
|---|---|
| Hned a zdarma | Krátkodobé kroky |
| Jedno odpoledne práce | Analytické úkoly |
| Háček: cílí na USA | Omezení: platforma se soustředí na USA |
| dává predikce zdarma | poskytuje predikce bezplatně |
| data, která stojí za prověření | data s potenciálem pro repurposing |
| už schválené léky | již schválená léčiva |

## Nadpisy

- Krátké jmenné fráze bez interpunkce.
- Nadpisy sekcí popisují obsah, ne dojem ("Strategická rozhodnutí",
  ne "Velké věci na potom").

## Fakta

Pravidla ověřování určuje bod 0 v [CLAUDE.md](../../CLAUDE.md): každé
tvrzení má zdroj, nejisté nese značku `⚠ OVĚŘIT`. Tón nikdy nejde proti
přesnosti. Formulace se nesmí zpřesněním vyostřit ani zaoblit nad rámec
zdroje.
