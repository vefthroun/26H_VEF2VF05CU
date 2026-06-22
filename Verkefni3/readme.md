## Verkefni 3  

- 20% af heildareinkunn
- Viðfangsefni:
  - CRUD aðgerðir með JSON / [TinyDB](https://tinydb.readthedocs.io/en/latest/getting-started.html)
  - API, beiðnir (_requests_) frá [TVmaze API](https://api.tvmaze.com)
  - Jinja2: Template inheritance, Include
  - HTML Form
  - Uppsetning (_Layout_) 

---

### Verkefnalýsing

#### JSON Tinydb 10%


1. Notaðu uppsetninguna sem þú hannaðir í 2. verkefni, taktu út orðasöfnin (_dictonaries_) úr appinu og settu innihaldið í JSON skrá.
1. Notaðu TinyDB pakkann til að framkvæma CRUD aðgerðir 
   * Allar færslur og breytingar eru vistaðar í JSON skránni
1. Á forsíðu birtast allir póstar úr json skránni
1. Nýskráning býr til nýjan notanda
1. Notandi getur síðan skráð sig inn á eigin **prófíl**
1. Notendur geta skrifað nýja pósta, breytt eigin póstum eða eytt þeim
1. Prófílsíðan er varin með **session** aðgangsvörn
1. Vefstjóri (admin) getur eytt póstum og notendum 

#### JSON API 10%
 
Útfærðu vefforrit í Flask sem birtir [TV Maze API](https://api.tvmaze.com) gögn. 

1. Á forsíðu (index) skal birta grunnupplýsingar um 20 random þætti ur _Epguides API_ gagnagrunninum. Birta skal nafn og mynd þáttaraða  **2%**
1. Þegar valin er ein þáttaröð af forsíðu er farið á síðu sem birtir nánari upplýsingar um valda þáttaröð. **3%**
    - nafn þáttaraðar (name)
    - mynd (image/medium)
    - textalýsing þáttaraðar (summary)
    - lengd þáttaraðar (runtime)
    - útgáfudagur þáttaraðar (premiered), íslensk dagsetning
    - dagsetning síðasta þáttar (ended)
    - flokkar þáttaraðar (genres)
1. Í valmynd er hlekkur á forsíðu, alla flokka (má vera í fellivalslista - select field), leitarreitur þar sem hægt er að leita að ákveðinni þáttaröð úr Epguides gagnagrunninum.  **1%**
1. Þegar valin er einn flokkur (genre) úr valmynd birtir kerfið vefsíðu með þáttaröðum sem tilheyra völdum flokki. Sömu upplýsingar og á forsíðu nafn og mynd **2%**
1. Þegar leitað er að þáttaröð er nafn slegið inn í leitarreit og ýtt á hnapp / takka.  Þá fer kerfið á vefsíðu sem birtir helstu upplýsingar um þáttaraðir sem tilheyra nafninu í leitarstregnum ( helstu upplýsingar nafn og mynd ).**2%**

> Notaðu PicoCSS fyrir uppsetningu (_layout_). <br> Notið Jinja erfðir (_Jinja2: inheritance_) og innsetningu skráa (_include: nav, footer_) á vefsíðum.

---

### Námsefni

- [JSON málskipan](namsefni/README.md)
- [JSON & Python CRUD dæmi](namsefni/pyCrudExamples/README.md)
- [TVmaze API](namsefni/TVmaze/README.md)
- [Tinydb gagnagrunnur](namsefni/Tinydb/README.md)


---

### Námsmat 

Sundurliðun námsmats er í verkefni 3 **í Canvas**

### Verkefnaskil

Skilaðu möppu með öllum skrám verkefnisins í **.zip skrá**  í Canvas (**ath!** ekki skila **venv** möppu).
