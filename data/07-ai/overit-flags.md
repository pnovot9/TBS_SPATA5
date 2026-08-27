---
id: overit-flags
typ: analyza
nazev: "Ověřit: všechny štítky"
datum-reserse: 2026-08-27
---

# Ověřit: všechny štítky

Přehled všech štítků `⚠ OVĚŘIT` ve vaultu na jednom místě. Slouží k rychlému projití otevřených otázek. Jakmile je otázka zodpovězena, opravte text ve zdrojovém článku, odstraňte tam štítek a smažte odpovídající řádek zde. Stav k 27. 8. 2026: 19 štítků ve 13 článcích.

## Rozpory mezi zdroji

Nejvyšší priorita. Dva zdroje si protiřečí, nebo mediální číslo nesedí s odbornou literaturou.

- **Věk dcery Zajícových.** HN (květen 2026) i Roklen24 (prosinec 2024) uvádějí 12 let. Obě čísla nemohou platit zároveň. Dohledat datum narození nebo věk potvrdit u rodiny. Článek: [[deti-a-rodiny]].
- **Úmrtnost "třetina dětí do šesti let".** Číslo uvádí HN. Kohorta z roku 2026 (plný text PMID 41933351) uvádí úmrtnost 3 z 51 pacientů (4,9 %), s číslem z HN je tedy v rozporu. Štítek je na dvou místech: [[hn-clanek-2026]] a [[spata5-nemoc]].
- **Počet pacientů.** HN píše o stovkách diagnostikovaných celosvětově, literatura zachycuje 51 publikovaných. Štítek je na dvou místech: [[hn-clanek-2026]] a [[epidemiologie]].
- **RD-Factory: čísla prvního kola.** Tisková zpráva a vzacni.cz mluví o 44 nominacích a 12 vybraných nemocech, avcr.cz uvádí 45 nominací a seznam jen 11 nemocí. Článek: [[rd-factory]].
- **Zařazení SPATA5 do RD-Factory.** Seznam Zprávy a BIOTRIN jmenují SPATA5 mezi prvními nemocemi programu, oficiální seznam na avcr.cz ji neuvádí. Štítek je na dvou místech: [[rd-factory]] a [[projekt-ccp-spata5]].
- **Shoda myších a lidských genů 98 %.** Číslo pochází z mediálních textů o CCP. Odborné zdroje formulují podobnost jinak. Dohledat přesnou formulaci a primární zdroj. Článek: [[ccp-centrum]].

## Technické překážky při rešerši

- **OMIM blokoval strojové stažení (HTTP 403).** Údaje jsou zprostředkované z výsledků vyhledávání. Ověřit při ručním přístupu. Článek: [[databaze]].
- **Vybraná částka sbírky na Donio.** Stránka částku vykresluje skriptem, nepodařilo se ji spolehlivě přečíst. Článek: [[faze-a-financovani]].

## Neúplná rešerše

- **Boltz-2 a Recursion.** Detaily pocházejí z tiskové zprávy a materiálů MIT. Před citováním v žádosti o grant zkontrolovat primární zdroje. Článek: [[ai-prilezitosti]].
- **Chybějící myší a zebrafish model.** Publikovaný model nebyl při rešerši nalezen. Negativní zjištění, které je potřeba čas od času znovu ověřit. Článek: [[lecba-a-vyzkum-svet]].
- **SPATA5/AFG2A v datasetu RxRx3.** Zastoupení genu mezi knockouty zatím nebylo ověřeno. Článek: [[inspirace]].
- **Zahraniční nadace SPATA.** Web už známe (spatafoundation.org, odkazuje na něj stránka ERN ITHACA). Chybí sídlo a přehled aktivit. Článek: [[zahranicni-organizace]].
- **Datum vyhlášení studie v Göttingenu.** Údaj "leden 2024" na citované stránce ERN ITHACA není. Dohledat zdroj data. Článek: [[zahranicni-organizace]].
- **Kapacity CCP.** Čísla "přes 1000 myších modelů" a "více než 15 specializací" se opírají jen o obecnou prezentaci na phenogenomics.cz. Doložit konkrétní stránku. Článek: [[ccp-centrum]].
- **Face2Gene v nemocnicích.** Tvrzení o Mayo Clinic a Boston Children's Hospital pochází jen z marketingu výrobce. Dohledat nezávislý zdroj. Článek: [[inspirace]].
- **Čtyřkombinace antiepileptik u Michaely.** Údaj se nepodařilo potvrdit z textu Deník.cz. Ověřit v původním článku. Článek: [[deti-a-rodiny]].

## Jak s přehledem pracovat

1. Vyberte štítek a ověřte tvrzení v primárním zdroji.
2. Opravte text ve zdrojovém článku a odstraňte tam štítek. Pokud je štítek na více místech, opravte všechna.
3. Smažte řádek z tohoto přehledu a upravte počet štítků v úvodu.
4. Spusťte `python3 web/build.py` a změny commitněte.
