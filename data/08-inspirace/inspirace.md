---
id: inspirace
typ: analyza
nazev: Inspirace ze světa
tagy: [inspirace, ai, vzacne-nemoci]
datum-reserse: 2026-08-27
---

# Inspirace ze světa

Přehled zahraničních firem a organizací, které spojují AI a vzácné nemoci. Slouží jako referenční rámec pro český projekt. Každá pokrývá jinou část problému: objev léčiva, pacientská data, nebo diagnostiku.

## Komerční firmy

- **Recursion** (recursion.com): americká biotechnologická firma. Trénuje AI modely na snímcích buněk a hledá tak nové léky. Má kandidáty v klinických zkouškách, i pro vzácné nemoci. Běží na infrastruktuře Google Cloud a spolu s MIT vyvinula Boltz-2, otevřenou alternativu k AlphaFold 3. Podrobněji v [[ai-prilezitosti]].
- **Healx** (healx.ai): britská firma zaměřená přímo na vzácné nemoci. Pomocí AI znovu využívá a kombinuje již známé látky (repurposing). Uvádí, že 90 % vzácných nemocí nemá žádnou léčbu.

> ℹ **Repurposing** je využití již schváleného léku pro jinou nemoc, než pro kterou vznikl.
> ℹ **Klinické zkoušky** ověřují léčbu na lidech.

## Neziskové organizace

- **Every Cure** (everycure.org): nezisková organizace. Vyhledává již schválená léčiva použitelná pro nemoci bez dostupné léčby. Její AI porovnává tisíce léčiv proti tisícům nemocí současně. Platforma se jmenuje MATRIX a je otevřená: kód i seznamy nemocí, léků a indikací jsou veřejné na GitHubu pod licencí Apache-2.0. Ověřeno 2026-08-27 na https://github.com/everycure-org/matrix.

## Pacientská data

- **Citizen Health** (citizen.health): aplikace pro pacienty se vzácnými nemocemi. Pomáhá jim shromáždit zdravotní záznamy na jednom místě a dobrovolně je poskytnout výzkumu. Řeší datovou vrstvu, ne objev molekuly.

## Diagnostika

- **Face2Gene** (face2gene.com): nástroj firmy FDNA pro lékaře. Z fotografie obličeje rozpozná rysy typické pro genetické syndromy a nabídne možné diagnózy. Používají ho velké nemocnice jako Mayo Clinic nebo Boston Children's Hospital. ⚠ OVĚŘIT: tvrzení o obou nemocnicích pochází jen z marketingu výrobce (face2gene.com). Dohledat nezávislý zdroj.

## Relevance pro projekt SPATA5

Rozbor z 2026-08-27. Položky jsou seřazeny podle dostupnosti a přínosu. Vyplývající akční body shrnuje [[todo]].

1. **Healx provozuje partnerský program pro pacientské skupiny.** Rare Treatment Accelerator přijímá žádosti od pacientských a akademických skupin. Podání žádosti je bezplatné a program nemá uzávěrku. Spolupráce je pro vybrané žadatele typicky bezplatná. SPATA5 splňuje podmínku vzácnosti (méně než 1 z 2 000). Healx se zaměřuje na repurposing známých látek. Ten může přinést terapeutický výsledek v kratším horizontu než genová terapie. Publikovaný účinek ketogenní diety na mitochondrie ([[lecba-a-vyzkum-svet]]) představuje mechanistické vodítko, na kterém takový screening staví. Kontakt: accelerate@healx.ai.
2. **Every Cure poskytuje predikce bezplatně.** Návrh na repurposing lze podat přes everycure.org/ideas. Platforma MATRIX je navíc otevřená, takže tým CCP může predikce pro SPATA5 spustit i vlastními silami.
3. **Citizen Health představuje model pro studii přirozeného průběhu.** Partnerské komunity platformy tvoří onemocnění stejné kategorie jako SPATA5: ADCY5, CACNA1A, CASK, CHD2, FOXG1, STXBP1. Z dat sdílených pacienty vznikají publikované studie přirozeného průběhu. Göttingenská kohorta ([[zahranicni-organizace]]) je pro nábor uzavřena, a tento přístup je proto jednou z mála cest k novým longitudinálním datům. Omezení: platforma se zatím soustředí na USA.
4. **Recursion zveřejňuje data s potenciálem pro repurposing.** Otevřený dataset RxRx3 obsahuje přes 17 000 genových knockoutů a přes 1 600 schválených léčiv. Prohlížet jej lze nástrojem MapApp. ⚠ OVĚŘIT: zastoupení SPATA5/AFG2A mezi knockouty zatím nebylo ověřeno. Pokud je gen zastoupen, lze bez laboratorní práce identifikovat léčiva s podobným nebo opačným buněčným profilem.
5. **Face2Gene má pro projekt nejnižší prioritu.** Diagnózu dnes potvrzuje sekvenování a onemocnění nemá výrazný obličejový fenotyp ([[spata5-nemoc]]). Nástroj může přispět k identifikaci dosud nediagnostikovaných pacientů.

> ℹ **Repurposing** je využití již schváleného léku pro jinou nemoc, než pro kterou vznikl. **Screening** je hromadné testování mnoha látek najednou.
> ℹ **Mechanistické vodítko** je poznatek o mechanismu nemoci, který napovídá, kde léčbu hledat.
> ℹ **Studie přirozeného průběhu** sleduje vývoj nemoci bez léčby. **Longitudinální data** jsou opakovaná měření týchž pacientů v čase.
> ℹ **Genový knockout** je cílené vypnutí jednoho genu v buňce.
> ℹ **Sekvenování** je přečtení pořadí písmen v DNA. U SPATA5 dává definitivní diagnózu jen genetické vyšetření a standardem je sekvenování exomu. U části pacientů je potřeba doplnit čipovou analýzu, která najde velké delece. **Obličejový fenotyp** je soubor rysů obličeje typických pro daný syndrom.

## Vazby

- [[todo]] (úkoly, které z rozboru plynou)

- [[ai-prilezitosti]] (kde může AI pomoci českému projektu)
- [[lecba-a-vyzkum-svet]] (světový výzkum SPATA5)
- [[diagnostika]] (jak se nemoc pozná)

## Zdroje

- https://www.recursion.com (navštíveno 2026-08-27)
- https://healx.ai (navštíveno 2026-08-27)
- https://everycure.org/about/ (navštíveno 2026-08-27)
- https://www.citizen.health (navštíveno 2026-08-27)
- https://www.face2gene.com (navštíveno 2026-08-27)
- Healx Rare Treatment Accelerator: https://healx.ai/rare-treatment-accelerator/ (navštíveno 2026-08-27)
- Every Cure MATRIX na GitHubu: https://github.com/everycure-org/matrix (navštíveno 2026-08-27)
- Otevřená data Recursion: https://www.rxrx.ai (navštíveno 2026-08-27)
