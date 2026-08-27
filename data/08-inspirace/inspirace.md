---
id: inspirace
typ: analyza
nazev: Inspirace ze světa
tagy: [inspirace, ai, vzacne-nemoci]
datum-reserse: 2026-08-27
---

# Inspirace ze světa

Přehled zahraničních firem a organizací, které spojují AI a vzácné nemoci. Slouží jako inspirace pro český projekt. Každá řeší jiný kus problému: objev léku, data pacientů, nebo diagnostiku.

## Komerční firmy

- **Recursion** (recursion.com): americká biotechnologická firma. Trénuje AI modely na snímcích buněk a hledá tak nové léky. Má kandidáty v klinických zkouškách, i pro vzácné nemoci.
- **Healx** (healx.ai): britská firma zaměřená přímo na vzácné nemoci. Pomocí AI znovu využívá a kombinuje už známé látky. Uvádí, že 90 % vzácných nemocí nemá žádnou léčbu.

## Neziskové organizace

- **Every Cure** (everycure.org): nezisková organizace. Hledá už schválené léky, které by šly použít na nemoci bez léčby. Jejich AI porovnává tisíce léků proti tisícům nemocí najednou. Platforma se jmenuje MATRIX a je otevřená: kód i seznamy nemocí, léků a indikací jsou veřejné na GitHubu pod licencí Apache-2.0. Ověřeno 2026-08-27 na https://github.com/everycure-org/matrix.

## Pacientská data

- **Citizen Health** (citizen.health): aplikace pro pacienty se vzácnými nemocemi. Pomáhá jim shromáždit zdravotní záznamy na jednom místě a dobrovolně je poskytnout výzkumu. Řeší datovou vrstvu, ne objev molekuly.

## Diagnostika

- **Face2Gene** (face2gene.com): nástroj firmy FDNA pro lékaře. Z fotografie obličeje rozpozná rysy typické pro genetické syndromy a nabídne možné diagnózy. Používají ho velké nemocnice jako Mayo Clinic nebo Boston Children's Hospital.

## Co z toho plyne pro SPATA5

Rozbor z 2026-08-27. Seřazeno podle toho, jak rychle se dá jednat. Konkrétní kroky shrnuje [[todo]].

1. **Healx má program pro pacientské skupiny.** Rare Treatment Accelerator přijímá žádosti od pacientských a akademických skupin. Přihláška je zdarma a nemá uzávěrku. Spolupráce je pro vybrané žadatele typicky bezplatná. SPATA5 splňuje podmínku vzácnosti (méně než 1 z 2 000). Zajímavé je to proto, že Healx hledá léčbu v už známých látkách. To může přinést výsledek dřív než genová terapie. Signál ketogenní diety na mitochondrie ([[lecba-a-vyzkum-svet]]) je přesně typ vodítka, na kterém takový screening staví. Kontakt: accelerate@healx.ai.
2. **Every Cure dává predikce zdarma.** Nápad na repurposing jde poslat přes everycure.org/ideas. A protože je MATRIX otevřený, může si tým CCP predikce pro SPATA5 spustit i sám.
3. **Citizen Health je vzor pro studii přirozeného průběhu.** Jejich partnerské komunity jsou nemoci stejného typu jako SPATA5: ADCY5, CACNA1A, CASK, CHD2, FOXG1, STXBP1. Z dat pacientů staví studie přirozeného průběhu a publikují je. Göttingenská kohorta ([[zahranicni-organizace]]) je uzavřená, takže tudy vede jedna z mála cest k novým dlouhodobým datům. Háček: platforma zatím cílí na USA.
4. **Recursion zveřejňuje data, která stojí za prověření.** Otevřený dataset RxRx3 obsahuje přes 17 000 genových knockoutů a přes 1 600 schválených léků, prohlížet se dá nástrojem MapApp. ⚠ OVĚŘIT: zda je mezi knockouty SPATA5/AFG2A, jsme zatím nezjišťovali. Pokud ano, dají se zdarma najít léky s podobným nebo opačným buněčným otiskem.
5. **Face2Gene je pro projekt nejméně podstatný.** Diagnózu dnes potvrzuje sekvenování a nemoc nemá výrazný obličejový vzorec ([[spata5-nemoc]]). Může ale pomoci najít dosud nediagnostikované pacienty.

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
