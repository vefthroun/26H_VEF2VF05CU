## Verkefni 4 

- 25% af heildareinkunn
- **Lykilmatsþáttur**
- Viðfangsefni: Allt námsefni
- Nemendur kynna verkefni sín í síðustu viku spannar

---

### Verkefnalýsing

Útfærðu vef með Flask tengt áhugamáli þar sem þú notar upplýsingar frá API (_Epguides API er ekki í boði_) ásamt því að vera með persónulegt blogg tengt áhugamálinu. Efnisval (texti og myndir) er valfrjálst en nemendur mega ekki vera með sama API. Gert er ráð fyrir sjálfstæðum vinnubrögðum. 

<details>
   <summary>Listi af APIs </summary>
   
   <!-- There’s an amazing amount of data available on the Web. Many web services, like YouTube and GitHub, make their data accessible to third-party applications through an API. Here are some examples of available APIs: -->
   Margar vefþjónustur, eins og YouTube og GitHub, gera gögn sín aðgengileg fyrir forrit þriðja aðila í gegnum forritaskil (API). Hér eru nokkur dæmi um tiltæk forritaskil:

   - [Public APIs](https://github.com/public-apis/public-apis)  
   - [List of free apis](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/)
   - [free for dev - apis](https://github.com/ripienaar/free-for-dev#apis-data-and-ml)

</details>

**Ath.** sumir API biðja um að fá kreditkorta upplýsingar, sleppum þeim.

---

### Námsmat 

Matþættir eru í verkefni 4 **í Canvas**. (_í vinnslu_)

#### Eftirfarandi verkþættir eru metnir til einkunna: verkefni 1-4 (70%)

1. **(10%)** Jinja: inheritance, include, skilyrðissetnignar, lykkjunotkun, filter, url_for, breytur. 
1. **(5%)** PicoCSS eða eigið CSS safn fyrir uppsetningu og útlit. 
1. **(10%)** API notkun (_ekki TWmaze API_) til að sækja gögn sem birtast á vef, lágmark 2 mismunandi fyrirspurnir.
1. **(5%)** Efnisyfirlit (menu) er með leitarglugga þar sem hægt er að leyta að efni í API 
1. **(5%)** Notkun á dynamic route og errorhandler (404 villa) 
1. **(5%)** Vefsíða sem birtir blogfærslur með röðun (nýjast efst). 
1. **(5%)** Login, sessions, validation og logout. 
1. **(5%)** Nýskráning notanda í Tinydb gagnagrunn 
1. **(10%)** Á pófíl síðu getur notandi framkvæmt CRUD aðgerðir á JSON skrá, höndlað með TinyDB (blogfærslur) 
   * Hnappur til að búa til blogfærslu -> síða með HTML Form til að skrifa nýja blogfærslu, Flash tilkynning.
   * Hnappur til að uppfæra blogfærslu -> síða með HTML Form til að uppfæra blogfærslu, Flash tilkynning.
   * Hnappur til að eyða blogfærslu -> FLash tilkynning 
1. **(10%)** Stjónborð (_Admin dashboard_) með töfluuppsetningu [sýnidæmi](https://blog-admin-ui.netlify.app/). 
   * Einungis notandi með session `role='admin'` getur komist á admin síðuna  
   *  Yfirlit notenda (_users_) í töflu
   *  Hnappur til að eyða notenda úr gagnagrunni -> FLash tilkynning
   *  Yfirlit pósta (_posts_) í töflu
   *  Hnappur til að eyða póstum úr gagnagrunni -> FLash tilkynning


   

#### Nýjungar: (30%)

Búðu til eigin kóðalausnir sem henta þínu lokaverkefni. Hér eru nokkrir **valmöguleikar** í boði:

- [Fileupload](https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/), ljósmyndir fyrir blogfærslur. (**10%** vægi)
- Vefurinn er hýstur (live production) með [PythonAnywhere](https://www.pythonanywhere.com/). (**10%** vægi)
  - - **[hýsing vefs á Py anywhere](py-anywhere/README.md)**
- Í stjórnborð síðu er hægt að bæta við flokkum í Tinydb gagnagrunn. (**5%** vægi)
- [Pagination in Flask: Split Your Data Into Pages](https://www.youtube.com/watch?v=U18hO1ngZEQ). (**5%** vægi)
- [WTFORM WTForms is a flexible forms validation and rendering library for Python web development.](https://flask-wtf.readthedocs.io/en/1.2.x/)  (**5%** vægi)
- [CKeditor. Rich Text Editor in Flask](https://ckeditor.com/) (**5%** vægi)
- **Annað** sem nemendur skýra frá í kynningu lokverkefnis (**5%** vægi)
<!-- - **HTMX** er framendalausn þar sem vafrinn er í lykilhlutverki í samskiptum við miðlarann  
    - Notaðu [htmx](https://htmx.org/docs/) til að gera vefinn dýnamískan (án þess að reload alla síðu) fyrir [delete](https://youtu.be/O2Xd6DmcB9g?t=1996) aðgerð á blogfærslum og [leit](https://www.youtube.com/watch?v=PWEl1ysbPAY). (**5%** vægi)-->

---

#### Kynning á lokaverkefni

1. Nemendur kynna kennara verkefni sitt, útskýra alla helstu ofangreinda virkni, eins og tími gefst. 
   - **Ef nemandi getur ekki gert grein fyrir kóða sínum, útskýrt útfærslu eða virkni þá fær lokaverkefnið falleinkunn**  

---

#### [Tímaáætlun lokaverkefnis](Skipulag.md)

---

### Verkefnaskil

Skilaðu möppu með öllum skrám verkefnisins í **.zip skrá**  í Canvas (**ath!** ekki skila **venv** möppu).


