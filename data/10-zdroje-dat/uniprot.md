---
id: uniprot
typ: zdroj
nazev: UniProt
tagy: [zdroj, databaze, uniprot, protein]
datum-reserse: 2026-08-30
---

# UniProt

Světová znalostní báze o proteinech. Web: https://www.uniprot.org

## Co to je

UniProt (Universal Protein Resource) spravuje od roku 2002 konsorcium tří institucí: EMBL-EBI (Velká Británie), SIB Swiss Institute of Bioinformatics (Švýcarsko) a Protein Information Resource (USA). Data jsou volně přístupná.

Hlavní částí je znalostní báze UniProtKB. Ta má dvě úrovně:

- Swiss-Prot: záznamy ručně zkontrolované kurátory (reviewed).
- TrEMBL: záznamy anotované automaticky, bez ruční kontroly.

Vedle toho existují databáze UniRef (klastry podobných sekvencí) a UniParc (archiv všech sekvencí).

> ℹ **Anotace** je popis funkce, stavby a vlastností proteinu připojený k jeho sekvenci.

## Záznam k SPATA5

Lidský protein SPATA5/AFG2A má kurátorovaný záznam Q8NB90 (Swiss-Prot). Uvedený název je "ATPase family gene 2 protein homolog A", délka 893 aminokyselin. Záznam shrnuje funkci, domény a odkazy do dalších databází.

- https://www.uniprot.org/uniprotkb/Q8NB90/entry

## Použitelnost pro náš výzkum

- Výchozí bod pro vše o proteinu: sekvence, domény AAA+ ATPázy, publikace, křížové odkazy na struktury a varianty. Doplňuje [[gen-spata5-afg2a]].
- Identifikátor Q8NB90 je klíč do dalších zdrojů, mimo jiné do databáze [[alphafold]].
- Srovnání lidského proteinu s myším ortologem při návrhu myších modelů v [[projekt-ccp-spata5]].

## Zdroje

- https://www.uniprot.org/help/about (konsorcium, databáze, Swiss-Prot vs. TrEMBL, navštíveno 30. 8. 2026)
- https://rest.uniprot.org/uniprotkb/search?query=gene:AFG2A+AND+organism_id:9606 (záznam Q8NB90, reviewed, 893 aminokyselin, staženo 30. 8. 2026)

## Vazby

- [[gen-spata5-afg2a]], [[alphafold]], [[databaze]]
