/* Shared sample data for the glossary design prototypes.
   Definitions are copied verbatim from the vault's "> ℹ" lines. */
const TERMS = [
  {t:"AAV vektor", topic:"Léčba a výzkum", def:"AAV vektor je virus, který sám nemoc nezpůsobuje. Je upravený tak, aby do buněk dopravil léčebný gen.", use:[["Český výzkum SPATA5","projekt-ccp-spata5"]]},
  {t:"CRISPR/Cas9", topic:"Genetika", def:"CRISPR/Cas9 je nástroj pro cílené úpravy DNA.", use:[["Český výzkum SPATA5","projekt-ccp-spata5"]]},
  {t:"Farmakorezistentní epilepsie", topic:"Projevy nemoci", def:"Farmakorezistentní epilepsie je epilepsie, kterou léky dostatečně netlumí.", use:[["České děti a rodiny","deti-a-rodiny"]]},
  {t:"Fenotyp", topic:"Diagnostika", def:"Fenotyp je souhrn projevů nemoci u pacienta.", use:[["Vědecké publikace","vedecke-publikace"]]},
  {t:"Gen", topic:"Genetika", def:"Gen je úsek DNA s návodem na výrobu jedné bílkoviny.", use:[["SPATA5 onemocnění","spata5-nemoc"]]},
  {t:"Genová terapie", topic:"Léčba a výzkum", def:"Genová terapie dodává do buněk funkční kopii genu.", use:[["Český výzkum SPATA5","projekt-ccp-spata5"]]},
  {t:"Kauzální léčba", topic:"Léčba a výzkum", def:"Kauzální léčba odstraňuje příčinu nemoci, nejen její projevy.", use:[["SPATA5 onemocnění","spata5-nemoc"],["Léčba a výzkum ve světě","lecba-a-vyzkum-svet"]]},
  {t:"Ketogenní dieta", topic:"Léčba a výzkum", def:"Ketogenní dieta je léčebná strava s vysokým podílem tuků a minimem sacharidů.", use:[["Vědecké publikace","vedecke-publikace"]]},
  {t:"Kryo-EM", topic:"Metody a data", def:"Kryo-EM zobrazuje rychle zmrazené molekuly elektronovým mikroskopem.", use:[["Kde může pomoci AI","ai-prilezitosti"],["Vědecké publikace","vedecke-publikace"]]},
  {t:"Mitochondrie", topic:"Buněčná biologie", def:"Mitochondrie jsou buněčné elektrárny. Vyrábějí energii pro chod buňky.", use:[["Český výzkum SPATA5","projekt-ccp-spata5"]]},
  {t:"Myší model", topic:"Léčba a výzkum", def:"Myší model je myš upravená tak, aby měla stejnou poruchu genu jako pacienti. Slouží ke studiu nemoci a testování léčby.", use:[["Český výzkum SPATA5","projekt-ccp-spata5"],["RD-Factory","rd-factory"]]},
  {t:"Patogenní varianta", topic:"Genetika", def:"Patogenní varianta je změna genu, která nemoc prokazatelně způsobuje.", use:[["Databáze a registry","databaze"]]},
  {t:"Preprint", topic:"Metody a data", def:"Preprint je vědecký článek zveřejněný před recenzním řízením.", use:[["Vědecké publikace","vedecke-publikace"]]},
  {t:"Přenašeč", topic:"Genetika", def:"Přenašeč má jednu poškozenou a jednu zdravou kopii genu. Sám je zdravý, poškozenou kopii ale může předat dítěti.", use:[["Hlavní článek Hospodářských novin","hn-clanek-2026"]]},
  {t:"Repurposing", topic:"Léčba a výzkum", def:"Repurposing je využití již schváleného léku pro jinou nemoc, než pro kterou vznikl.", use:[["To do a další kroky","todo"]]},
  {t:"Westův syndrom", topic:"Projevy nemoci", def:"Westův syndrom je epilepsie kojenců se sériemi krátkých záškubů. Dnes se označuje jako infantilní epileptické spasmy.", use:[["České děti a rodiny","deti-a-rodiny"]]},
];
function norm(s) {
  return s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}
