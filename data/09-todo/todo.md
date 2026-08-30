---
id: todo
typ: analyza
nazev: To do a další kroky
tagy: [todo, dalsi-kroky, inspirace]
datum-reserse: 2026-08-30
---

# To do a další kroky

Jediný seznam úkolů projektu. Akční body vycházejí z rozboru zahraničních organizací v [[inspirace]] a z analýzy [[ai-prilezitosti]]. Stav k 2026-08-30.

## Krátkodobé kroky

- [ ] **Podat žádost do programu Healx Rare Treatment Accelerator.** Podání žádosti je bezplatné a program nemá uzávěrku. Prvním krokem je dotazník způsobilosti na https://healx.ai/rare-treatment-accelerator/. Kontaktní adresa programu: accelerate@healx.ai.
- [ ] **Nominovat SPATA5 u organizace Every Cure.** Návrh na repurposing lze podat prostřednictvím formuláře na https://everycure.org/ideas/.

> ℹ **Repurposing** je využití již schváleného léku pro jinou nemoc, než pro kterou vznikl.

## Analytické úkoly

- [ ] **Ověřit zastoupení genu SPATA5/AFG2A v datech Recursion.** Vyhledat gen v nástroji MapApp (https://www.rxrx.ai). Pokud je mezi knockouty zastoupen, sestavit seznam schválených léčiv s podobným nebo opačným buněčným profilem.
- [ ] **Posoudit platformu MATRIX.** Vyhodnotit, zda lze predikce pro SPATA5 spustit lokálně z veřejného repozitáře: https://github.com/everycure-org/matrix.

> ℹ **Knockout** je cílené vypnutí genu v buňce. **Buněčný profil** je otisk toho, jak zásah změní vzhled a chování buněk.
> ℹ **Predikce** zde znamená počítačový odhad, které léky by mohly na nemoc působit.

- [ ] **Ohodnotit varianty genu SPATA5/AFG2A modelem Evo 2.** Model je otevřený a nepotřebuje trénovací data pro daný gen. Postup převzít z návodu pro BRCA1: https://docs.nvidia.com/bionemo-framework/2.5/user-guide/examples/bionemo-evo2/zeroshot_brca1/. Vstupem jsou varianty z publikované kohorty a ze záznamů v ClinVar ([[databaze]]). Výstupem je pořadí variant podle předpokládané závažnosti jako podklad pro výběr varianty do myšího modelu. Podrobněji v [[ai-prilezitosti]].
- [ ] **Zjistit, zda CCP může Evo 2 spustit vlastními silami.** Největší varianty modelu vyžadují silné GPU. Alternativou je hostovaná služba NIM na platformě BioNeMo. Ověřit výpočetní kapacitu ÚMG a cenu hostované varianty.

> ℹ **Kohorta** je skupina pacientů sledovaná ve studii. **GPU** je grafický procesor, dnes běžný hardware pro běh AI modelů.

## Strategická rozhodnutí

- [ ] **Posoudit vytvoření komunity pacientských dat po vzoru Citizen Health.** Göttingenská kohorta je pro nábor uzavřena ([[zahranicni-organizace]]). Možnosti jsou dvě: oslovit Citizen Health ohledně komunity SPATA5, nebo obdobný model vybudovat v Evropě. K projednání se spolkem [[spolek-spata5-cz]].

## Otevřené otázky z rešerše

Přeneseno z analýzy [[ai-prilezitosti]]. Stav k 2026-08-26, dosud nevyřešeno.

- [ ] Zjistit přesný stav myšího modelu v CCP. Web říká jen "in development". Kontakt: jana.safrankova@img.cas.cz.
- [ ] Ověřit, zda je SPATA5 formálně v programu [[rd-factory]], nebo běží čistě na smlouvě s ÚMG. Zdroje si odporují.
- [ ] Objasnit roli SPATA Foundation. Zjistit, zda se lze napojit na göttingenská data přirozeného průběhu.
- [ ] Ověřit tvrzení HN o třetinové úmrtnosti do šesti let. V literatuře nedohledáno.
- [ ] Zjistit, zda se česká skupina účastní 8. CCP konference (9. až 11. 9. 2026) s vlastními daty k SPATA5.
- [ ] Sledovat, kdy NVIDIA Academic Grant Program znovu otevře příjem žádostí. K 30. 8. 2026 je uzavřen. Žadatelem musí být akademické pracoviště, tedy ÚMG.

## Vazby

- [[inspirace]] (rozbor, ze kterého vycházejí krátkodobé a analytické úkoly)
- [[ai-prilezitosti]] (analýza, ze které vycházejí otevřené otázky)

## Zdroje

- https://healx.ai/rare-treatment-accelerator/ (navštíveno 2026-08-27)
- https://everycure.org/ideas/ (odkaz z everycure.org, 2026-08-27)
- https://github.com/everycure-org/matrix (navštíveno 2026-08-27)
- https://www.rxrx.ai (navštíveno 2026-08-27)
- Návod k predikci variant modelem Evo 2: https://docs.nvidia.com/bionemo-framework/2.5/user-guide/examples/bionemo-evo2/zeroshot_brca1/ (navštíveno 2026-08-30)
- NVIDIA Academic Grant Program: https://www.nvidia.com/en-us/industries/higher-education-research/academic-grant-program/ (navštíveno 2026-08-30)
