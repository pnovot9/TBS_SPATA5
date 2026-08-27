---
id: ai-prilezitosti
typ: analyza
nazev: Příležitosti pro AI a otevřené otázky
tagy: [ai, analyza, dalsi-kroky]
datum-reserse: 2026-08-26
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

## Otevřené otázky k dořešení

Otevřené otázky z této analýzy jsou vedeny jako úkoly v poznámce [[todo]], v oddílu "Otevřené otázky z rešerše".

## Zdroje

- Přehled AlphaFold (databáze, server, AlphaFold 3): https://deepmind.google/science/alphafold/ (navštíveno 2026-08-27)
- Záznam AFG2A v AlphaFold DB: https://alphafold.ebi.ac.uk/entry/Q8NB90 (ověřeno přes API 2026-08-27)
- AlphaFold 3: Abramson J. et al., Nature 2024, DOI 10.1038/s41586-024-07487-w
- Boltz-2 (MIT + Recursion): https://ir.recursion.com/news-releases/news-release-details/mit-and-recursion-release-boltz-2-next-generation-ai-model a https://jclinic.mit.edu/boltz-2-towards-accurate-and-efficient-binding-affinity-prediction/ (navštíveno 2026-08-27)
- Partnerství Recursion a Google Cloud: https://www.prnewswire.com/news-releases/recursion-and-google-cloud-announce-expansion-of-partnership-to-support-drug-discovery-with-cloud-and-exploration-of-generative-ai-technologies-302281509.html (navštíveno 2026-08-27)

## Vazby

- [[projekt-ccp-spata5]] (výzkum, kterému má AI pomoci)
- [[gen-spata5-afg2a]] (molekulární podklad)
- [[epidemiologie]] (datová situace)
- [[faze-a-financovani]] (ekonomický kontext)
- [[todo]] (otevřené otázky a další kroky)
