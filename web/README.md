# Web

Znalostní centrum SPATA5. Statický web vygenerovaný z vaultu v `../data/`.
Podrobná dokumentace je ve složce [_documentation](_documentation/).

## Jak to funguje

- `build.py` přečte všechny články z `../data/`, převede je na HTML a vytvoří `index.html` z `INDEX.md`. Výstup zapisuje do `dist/` a kopíruje tam soubory z `assets/`. Odkazy `[[wikilink]]` se překládají na odkazy mezi stránkami. Neexistující odkaz shodí build.
- `assets/styles.css` je jediný stylesheet (design Atlas: tmavé levé menu, světlý i tmavý režim obsahu).
- `assets/app.js` obsluhuje přepínač režimu (posuvník se sluncem a měsícem). Volba se pamatuje v prohlížeči.
- `dist/` je vygenerovaný web. Needitovat ručně, další build ho přepíše.
- `designs/` obsahuje čtyři původní návrhy designu k porovnání.

## Po změně obsahu ve vaultu

```bash
python3 web/build.py
```

Náhled: `python3 -m http.server 8741 -d web/dist` a otevřít http://localhost:8741.
