---
id: overit-flags
typ: analyza
nazev: "Ověřit: všechny štítky"
datum-reserse: 2026-08-27
---

# Ověřit: všechny štítky

Přehled všech štítků `⚠ OVĚŘIT` ve vaultu na jednom místě. Slouží k rychlému projití otevřených otázek. Jakmile je otázka zodpovězena, opravte text ve zdrojovém článku, odstraňte tam štítek a smažte odpovídající řádek zde. Stav k 27. 8. 2026: 20 štítků v 16 článcích.

## Rozpory mezi zdroji

Nejvyšší priorita. Dva zdroje si protiřečí, nebo mediální číslo nesedí s odbornou literaturou.

- **Věk dcery Zajícových.** HN (květen 2026) i Roklen24 (prosinec 2024) uvádějí 12 let. Obě čísla nemohou platit zároveň. Dohledat datum narození nebo věk potvrdit u rodiny. Článek: [[deti-a-rodiny]].
- **Úmrtnost "třetina dětí do šesti let".** Číslo uvádí HN, v odborné literatuře jsme je nedohledali. Štítek je na dvou místech: [[hn-clanek-2026]] a [[spata5-nemoc]].
- **Počet pacientů.** HN píše o stovkách diagnostikovaných celosvětově, literatura zachycuje 51 publikovaných. Štítek je na dvou místech: [[hn-clanek-2026]] a [[epidemiologie]].
- **RD-Factory: 12 vs. 11 nemocí prvního kola.** Tisková zpráva mluví o 12 vybraných nemocech, seznam na avcr.cz jich jmenuje 11. Článek: [[rd-factory]].
- **Zařazení SPATA5 do RD-Factory.** Seznam Zprávy a BIOTRIN jmenují SPATA5 mezi prvními nemocemi programu, oficiální seznam na avcr.cz ji neuvádí. Štítek je na dvou místech: [[rd-factory]] a [[projekt-ccp-spata5]].
- **Shoda myších a lidských genů 98 %.** Číslo pochází z mediálních textů o CCP. Odborné zdroje formulují podobnost jinak. Dohledat přesnou formulaci a primární zdroj. Článek: [[ccp-centrum]].

## Tvrzení bez dohledaného zdroje

U těchto tvrzení platí: dohledat zdroj, jinak tvrzení smazat.

- **Procházka: terapie "v horizontu let".** Věta v dostupném textu HN není. Dohledat v tištěném nebo plném znění článku. Článek: [[jan-prochazka]].
- **Sedláček: výzkum "na nekomerční bázi".** Formulace na zazracnedeti.cz není. Dohledat, odkud pochází. Článek: [[radislav-sedlacek]].
- **Sedláček: předsednictví konsorcia IMPC.** Profil na biocev.eu roli nepotvrzuje. Ověřit na impc.org nebo v ÚMG. Článek: [[radislav-sedlacek]].
- **Nepřímé zmínky o Janu Zajícovi.** Odkazy na Deník.cz a biotrin.cz chybí. Dohledat URL a datum. Článek: [[jan-zajic]].

## Technické překážky při rešerši

- **OMIM blokoval strojové stažení (HTTP 403).** Údaje jsou zprostředkované z výsledků vyhledávání. Ověřit při ručním přístupu. Článek: [[databaze]].
- **Vybraná částka sbírky na Donio.** Stránka částku vykresluje skriptem, nepodařilo se ji spolehlivě přečíst. Článek: [[faze-a-financovani]].

## Neúplná rešerše

- **Boltz-2 a Recursion.** Detaily pocházejí z tiskové zprávy a materiálů MIT. Před citováním v žádosti o grant zkontrolovat primární zdroje. Článek: [[ai-prilezitosti]].
- **Chybějící myší a zebrafish model.** Publikovaný model nebyl při rešerši nalezen. Negativní zjištění, které je potřeba čas od času znovu ověřit. Článek: [[lecba-a-vyzkum-svet]].
- **Zkomolená citace Procházky.** Slovo "buňové" místo "buněčné" vzniklo při strojovém čtení HN. Ověřit přesné znění. Článek: [[jan-prochazka]].
- **SPATA5/AFG2A v datasetu RxRx3.** Zastoupení genu mezi knockouty zatím nebylo ověřeno. Článek: [[inspirace]].
- **Zahraniční nadace SPATA.** Chybí web, sídlo a přehled aktivit. Článek: [[zahranicni-organizace]].

## Jak s přehledem pracovat

1. Vyberte štítek a ověřte tvrzení v primárním zdroji.
2. Opravte text ve zdrojovém článku a odstraňte tam štítek. Pokud je štítek na více místech, opravte všechna.
3. Smažte řádek z tohoto přehledu a upravte počet štítků v úvodu.
4. Spusťte `python3 web/build.py` a změny commitněte.
