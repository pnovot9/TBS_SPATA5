---
id: ai-prilezitosti
typ: analyza
nazev: Příležitosti pro AI a otevřené otázky
tagy: [ai, analyza, dalsi-kroky]
datum-reserse: 2026-08-30
---

# Kde může pomoci AI

Tato poznámka mapuje výchozí situaci pro plánované nasazení AI ve výzkumu. Není to hotová strategie. Vychází jen z toho, co rešerše zjistila.

## Co z rešerše plyne jako podklad

- **Mechanismus nemoci je z velké části rozkrytý.** Známe strukturu proteinového komplexu (kryo-EM 2025) i obě buněčné role (ribozomy, mitochondrie). To otevírá prostor pro výpočetní přístupy: predikce dopadu variant, strukturní modelování (AlphaFold a nástupci, viz níže), in silico screening malých molekul. Viz [[gen-spata5-afg2a]].
- **Dat o pacientech je málo a jsou roztroušená.** 51 publikovaných pacientů, dalších ~30 v nepublikované kohortě v Göttingenu. AI může pomoci s extrakcí a harmonizací fenotypových dat z literatury (HPO termíny) a s napojením na kohortu. Viz [[epidemiologie]] a [[zahranicni-organizace]].
- **Český projekt teprve generuje data.** Myší model je ve vývoji. Až poběží fenotypizace v CCP, vzniknou objemná data (chování, metabolomika, imaging, EEG). To je přirozené místo pro strojové učení. Viz [[projekt-ccp-spata5]].
- **Literatura roste rychle.** Jen v letech 2025 a 2026 vyšlo několik zásadních prací. Automatický monitoring PubMed, bioRxiv a ClinVar pro SPATA5/AFG2A je levná a okamžitě užitečná věc.
- **Mediální stopa je malá.** Pro fundraising spolku může AI pomoci s obsahem a osvětou. Viz [[media-chronologie]].

> ℹ **Kryo-EM** zobrazuje rychle zmrazené molekuly elektronovým mikroskopem. **Predikce dopadu variant** odhaduje, jak konkrétní změna DNA poškodí bílkovinu.
> ℹ **In silico screening** je počítačové prosévání velkého množství látek bez laboratorní práce.
> ℹ **HPO termíny** jsou položky standardizovaného slovníku příznaků. Slouží k jednotnému popisu pacientů.
> ℹ **Fenotypizace** je systematické měření projevů nemoci. **Metabolomika** měří malé molekuly látkové výměny. **EEG** měří elektrickou aktivitu mozku.

## AlphaFold a navazující nástroje

AlphaFold od Google DeepMind predikuje 3D strukturu proteinů z jejich sekvence. Pro práci na SPATA5/AFG2A jsou relevantní tři produkty (přehled: https://deepmind.google/science/alphafold/):

- **AlphaFold Protein Structure Database** (https://alphafold.ebi.ac.uk). Otevřená databáze, kterou DeepMind provozuje spolu s EMBL-EBI. Obsahuje přes 200 milionů predikovaných struktur. Predikce pro lidský protein AFG2A je dostupná pod záznamem UniProt Q8NB90. Databáze je zdarma a bez registrace.
- **AlphaFold Server** (https://alphafoldserver.com). Webové rozhraní nad modelem AlphaFold 3. Predikuje strukturu komplexů proteinu s dalšími molekulami: jinými proteiny, DNA, RNA, ionty a vybranými ligandy. Pro nekomerční výzkum je zdarma. Hodí se pro modelování interakcí komplexu AFG2A bez vlastní výpočetní infrastruktury.
- **AlphaFold 3.** Model publikovaný v Nature v květnu 2024. Oproti AlphaFold 2 predikuje nejen samotné proteiny, ale i jejich interakce s malými molekulami a nukleovými kyselinami. Kód a váhy modelu jsou dostupné na GitHubu pro akademické použití.

> ℹ **Sekvence** je pořadí stavebních jednotek v DNA nebo v bílkovině.
> ℹ **Ligand** je malá molekula, která se váže na bílkovinu.
> ℹ **Nukleové kyseliny** jsou DNA a RNA, nosiče genetické informace.
> ℹ **Váhy modelu** jsou naučené parametry AI modelu. Jejich zveřejnění umožňuje model provozovat vlastními silami.

### Vazba na Recursion

Recursion (viz [[inspirace]]) má na AlphaFold dvě vazby:

- **Infrastruktura od Googlu.** Recursion přes šest let běží na Google Cloud a v říjnu 2024 partnerství rozšířila o zkoumání generativních modelů Gemini pro svou platformu RecursionOS. Nejde tedy o přímou spolupráci s DeepMind, ale o infrastrukturní partnerství v rámci Googlu.
- **Boltz-2, otevřená alternativa k AlphaFold 3.** Recursion vyvinula spolu s MIT model Boltz-2 (červen 2025). Navazuje na Boltz-1, nejrozšířenější open-source alternativu k AlphaFold 3. Boltz-2 navíc predikuje vazebnou afinitu, tedy jak silně se molekula váže na cíl. To je přímý krok k in silico screeningu léčiv. Model je pod licencí MIT, takže jej lze volně použít i pro projekt SPATA5. Trénován byl na superpočítači Recursion BioHive-2. ⚠ OVĚŘIT: detaily převzaty z tiskové zprávy Recursion a materiálů MIT Jameel Clinic, před citováním v žádosti o grant zkontrolovat primární zdroje.

> ℹ **Generativní modely** jsou AI modely, které vytvářejí nový obsah. **Vazebná afinita** udává, jak silně se molekula váže na svůj cíl.
> ℹ **Open source** znamená veřejně dostupný kód, který smí kdokoli používat a upravovat. **Licence MIT** je jedna z nejvolnějších open source licencí.

## Otevřené modely NVIDIA

NVIDIA vyvíjí a zveřejňuje modely a nástroje pro biologii pod značkou BioNeMo. Kód samotného frameworku je pod licencí Apache 2.0. Licence vah a dat se liší model od modelu, u kopií hostovaných NVIDIA jde často o NVIDIA Open Model License. Před použitím je nutné licenci konkrétního modelu zkontrolovat. Pro projekt SPATA5 jsou relevantní čtyři položky.

- **Evo 2.** Jazykový model DNA pracující v rozlišení jednotlivých nukleotidů. Vznikl ve spolupráci Arc Institute, Stanfordovy univerzity a NVIDIA, trénink běžel na NVIDIA DGX Cloud. Trénovací sada OpenGenome2 obsahuje 8,8 bilionu tokenů ze všech domén života, samotný trénink podle autorů proběhl na více než 9,3 bilionu tokenů. Kontextové okno největších variant je 1 milion bází. Model odhaduje dopad genetických variant bez doladění na konkrétní úlohu. Tisková zpráva Arc Institute uvádí, že v testech s variantami genu BRCA1 model rozlišil s přesností přes 90 %, které mutace jsou neškodné a které možná patogenní. Jde o formulaci z tiskové zprávy, článek v Nature uvádí místo přesnosti hodnoty AUROC a AUPRC. Model nebyl doladěn na variantách BRCA1 ani neviděl údaje o jejich dopadu. Samotná sekvence lidského genomu včetně BRCA1 v trénovacích datech je. Kód i váhy jsou pod licencí Apache 2.0. Autoři uvádějí, že zveřejnili parametry modelu, trénovací i inferenční kód a dataset OpenGenome2.
- **BioNeMo Framework.** Otevřená sada nástrojů pro trénink a nasazení biologických modelů. Přes ni je Evo 2 dostupné i jako hostovaná služba NIM, tedy bez vlastní výpočetní infrastruktury. 23. 6. 2026 NVIDIA přidala BioNeMo Agent Toolkit, který tyto modely zpřístupňuje jako nástroje pro AI agenty.
- **Parabricks.** Nástroje pro zarovnání sekvencí a volání variant zrychlené na GPU. Jsou bezplatné a nevyžadují licenční klíč. Uplatní se, až bude projekt sekvenovat myší model.
- **Academic Grant Program.** Program NVIDIA poskytoval akademickým pracovištím výpočetní čas a hardware, například až 30 000 hodin na GPU H100. K 30. 8. 2026 program nepřijímá nové žádosti. Stojí za to jej sledovat, protože výpočetní kapacita by nezatížila rozpočet v [[faze-a-financovani]].

> ℹ **Nukleotid** je jedno písmeno genetického kódu. **Kontextové okno** je délka úseku, který model zpracuje najednou.
> ℹ **Volání variant** je vyhledání odchylek od referenčního genomu v naměřených datech. **Zarovnání sekvencí** přiřazuje přečtené úseky DNA na jejich místo v genomu.
> ℹ **Inference** je spuštění natrénovaného modelu na nových datech. **Doladění** je dotrénování hotového modelu na konkrétní úloze.
> ℹ **AUROC** a **AUPRC** jsou míry úspěšnosti klasifikace. Nabývají hodnot od 0 do 1, vyšší je lepší.

### Konkrétní využití pro SPATA5

Evo 2 je pro projekt nejzajímavější. Pracuje přímo s DNA, takže nepotřebuje kohortu pacientů ani trénovací data pro daný gen. To odpovídá situaci, kdy je publikováno 51 pacientů ([[epidemiologie]]).

Možné využití jsou dvě. Ohodnotit dopad všech dosud popsaných variant v genu SPATA5/AFG2A a použít pořadí jako podklad pro výběr varianty do myšího modelu ([[projekt-ccp-spata5]]). A dále zařadit varianty nejasného významu, které se objeví u nově diagnostikovaných dětí ([[diagnostika]]). NVIDIA k modelu zveřejnila návod pro gen BRCA1, který lze na AFG2A přepsat. ⚠ OVĚŘIT: přenositelnost návodu na AFG2A nebyla vyzkoušena, jde o odhad z dokumentace. Výsledky modelu jsou predikce, ne diagnóza, a pro klinické použití je nutné je ověřit laboratorně.

> ℹ **Varianta nejasného významu (VUS)** je nalezená odchylka v DNA, u které se zatím neví, zda nemoc způsobuje.

## Otevřené otázky k dořešení

Otevřené otázky z této analýzy jsou vedeny jako úkoly v poznámce [[todo]], v oddílu "Otevřené otázky z rešerše".

## Zdroje

- Přehled AlphaFold (databáze, server, AlphaFold 3): https://deepmind.google/science/alphafold/ (navštíveno 2026-08-27)
- Záznam AFG2A v AlphaFold DB: https://alphafold.ebi.ac.uk/entry/Q8NB90 (ověřeno přes API 2026-08-27)
- AlphaFold 3: Abramson J. et al., Nature 2024, DOI 10.1038/s41586-024-07487-w
- Boltz-2 (MIT + Recursion): https://ir.recursion.com/news-releases/news-release-details/mit-and-recursion-release-boltz-2-next-generation-ai-model a https://jclinic.mit.edu/boltz-2-towards-accurate-and-efficient-binding-affinity-prediction/ (navštíveno 2026-08-27)
- Partnerství Recursion a Google Cloud: https://www.prnewswire.com/news-releases/recursion-and-google-cloud-announce-expansion-of-partnership-to-support-drug-discovery-with-cloud-and-exploration-of-generative-ai-technologies-302281509.html (navštíveno 2026-08-27)

- Evo 2: Brixi G. et al., "Genome modelling and design across all domains of life with Evo 2", Nature 2026, 652(8112), s. 1349 až 1361, online 4. 3. 2026, DOI 10.1038/s41586-026-10176-5, PMID 41781614
- Kód a váhy Evo 2: https://github.com/arcinstitute/evo2 a https://huggingface.co/arcinstitute/evo2_7b (navštíveno 2026-08-30)
- Evo 2 na platformě BioNeMo a údaj o přesnosti u BRCA1: https://blogs.nvidia.com/blog/evo-2-biomolecular-ai/ (navštíveno 2026-08-30)
- Návod k predikci variant BRCA1: https://docs.nvidia.com/bionemo-framework/2.5/user-guide/examples/bionemo-evo2/zeroshot_brca1/ (navštíveno 2026-08-30)
- Licence frameworku BioNeMo: https://docs.nvidia.com/bionemo-framework/latest/main/references/FAQ/ (navštíveno 2026-08-30)
- Údaj o přesnosti přes 90 % u BRCA1: https://arcinstitute.org/news/evo2 (navštíveno 2026-08-30)
- BioNeMo Agent Toolkit: https://nvidianews.nvidia.com/news/nvidia-launches-bionemo-agent-toolkit-giving-ai-agents-the-tools-to-accelerate-scientific-discovery (navštíveno 2026-08-30)
- Parabricks: https://docs.nvidia.com/clara/parabricks/latest/ (navštíveno 2026-08-30)
- NVIDIA Academic Grant Program: https://www.nvidia.com/en-us/industries/higher-education-research/academic-grant-program/ (navštíveno 2026-08-30)

## Vazby

- [[projekt-ccp-spata5]] (výzkum, kterému má AI pomoci)
- [[gen-spata5-afg2a]] (molekulární podklad)
- [[epidemiologie]] (datová situace)
- [[faze-a-financovani]] (ekonomický kontext)
- [[diagnostika]] (kde by predikce variant pomohla)
- [[todo]] (otevřené otázky a další kroky)
