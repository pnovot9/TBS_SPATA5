# Web

Znalostní centrum SPATA5. Statický web vygenerovaný z vaultu v `../data/`.

## Jak to funguje

- `build.py` přečte všechny články z `../data/`, převede je na HTML a vytvoří `index.html` z `INDEX.md`. Odkazy `[[wikilink]]` se překládají na odkazy mezi stránkami. Neexistující odkaz shodí build.
- `styles.css` je jediný stylesheet (design Atlas: tmavé levé menu, světlý i tmavý režim obsahu).
- `app.js` obsluhuje přepínač režimu (posuvník se sluncem a měsícem). Volba se pamatuje v prohlížeči.
- `designs/` obsahuje čtyři původní návrhy designu k porovnání.

## Po změně obsahu ve vaultu

```bash
python3 web/build.py
```

Náhled: `python3 -m http.server 8741 -d web` a otevřít http://localhost:8741.
