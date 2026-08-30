---
id: alphafold
typ: zdroj
nazev: AlphaFold DB
tagy: [zdroj, databaze, alphafold, struktura, ai]
datum-reserse: 2026-08-30
---

# AlphaFold DB

Databáze predikovaných 3D struktur proteinů. Web: https://alphafold.ebi.ac.uk

## Co to je

AlphaFold Protein Structure Database provozují společně Google DeepMind a EMBL-EBI. Obsahuje přes 200 milionů predikovaných struktur proteinů, tedy téměř všechny katalogizované proteiny z UniProtu. Data jsou volně přístupná. Struktury se hledají podle UniProt identifikátoru.

Predikce počítá AI systém AlphaFold. Metodu popisuje článek Jumper a kol., Nature 2021 (DOI 10.1038/s41586-021-03819-2).

> ℹ **Predikovaná struktura** je výpočetní odhad tvaru proteinu, ne experimentální měření. Každý model nese skóre spolehlivosti predikce.

## Záznam k SPATA5

Pro lidský protein SPATA5/AFG2A (UniProt Q8NB90) existuje model AF-Q8NB90-F1 a dva modely alternativních izoform.

- https://alphafold.ebi.ac.uk/entry/Q8NB90

## Použitelnost pro náš výzkum

- Rychlý pohled na stavbu proteinu tam, kde experimentální struktura chybí.
- Mapování pacientských missense variant na strukturu: kde v proteinu změna leží a co může poškodit. Navazuje na [[gen-spata5-afg2a]].
- Srovnání predikce s experimentální kryo-EM strukturou komplexu z roku 2025 (viz [[vedecke-publikace]]).
- Struktura myšího ortologu pro návrh modelů v [[projekt-ccp-spata5]].

Pozor: jde o predikce. Závěry pro terapii je nutné opřít o experiment.

## Zdroje

- https://alphafold.ebi.ac.uk/about (provozovatelé, přes 200 mil. struktur, metoda, navštíveno 30. 8. 2026)
- https://alphafold.ebi.ac.uk/api/prediction/Q8NB90 (existence modelu AF-Q8NB90-F1 a izoform, staženo 30. 8. 2026)

## Vazby

- [[uniprot]] (zdrojový identifikátor Q8NB90)
- [[gen-spata5-afg2a]], [[ai-prilezitosti]]
