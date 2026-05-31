## Verkefni 5 
- 35% af heildareinkunn
- **Lykilmatsþáttur**
- Viðfangsefni: Allt námsefni
- Nemendur kynna verkefni sín í síðustu viku spannar

---

### Verkefnalýsing

Útfærðu vef með Flask tengt áhugamáli þar sem þú notar upplýsingar frá API (TVMaze API er ekki í boði) ásamt því að vera með persónulegt blogg tengt áhugamálinu. Efnisval (texti og myndir) er valfrjálst en nemendur mega ekki vera með sama API. Gert er ráð fyrir sjálfstæðum vinnubrögðum. 
<details>
<summary>Listi af APIs </summary>
  
<!-- There’s an amazing amount of data available on the Web. Many web services, like YouTube and GitHub, make their data accessible to third-party applications through an API. Here are some examples of available APIs: -->
- [Public APIs](https://github.com/public-apis/public-apis)  
- [List of free apis](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/)
- [free for dev - apis](https://github.com/ripienaar/free-for-dev#apis-data-and-ml)

</details>

**Ath.** sumir API biðja um að fá kreditkorta upplýsingar, sleppum þeim.

---

### Námsmat 
Eftirfarandi verkþættir eru metnir til einkunna: <br>

#### Námsefni: verkefni 1-4 (70%)

1. Jinja: inheritance, include, skilyrðissetnignar, lykkjunotkun, filter, url_for, breytur. **(10%)**
1. PicoCSS eða eigið CSS safn fyrir uppsetningu og útlit. **(10%)**
1. Efnisyfirlit (menu) sýnir hvaða hlekkur er virkur hverju sinni og í efnisyfirlitinu er leitargluggi **(5%)**
1. API notkun (ekki TVMaze og TMDB) til að sækja gögn sem birtast á vef, lágmark 2 mismunandi fyrirspurnir. **(10%)**
1. Notkun á dynamic route og errorhandler (404 villa) **(5%)**
1. Vefsíða sem birtir blogfærslur með röðun (nýjast efst). **(5%)**
1. Login, sessions, validation og einföld auðkenning fyrir einn notanda (admin@admin.is og lykilorðið 123456), logout. **(5%)**
1. Admin (dashboard) með töfluuppsetningu, CRUD aðgerðir á JSON skrá höndlað með TinyDB (blogfærslur). **(20%)**
   * Blog yfirlit í töflu
   * Hnappur til að búa til blogfærslu -> síða með HTML Form til að skrifa nýja blogfærslu, Flash tilkynning.
   * Hnappur til að uppfæra blogfærslu -> síða með HTML Form til að uppfæra blogfærslu, Flash tilkynning.
   * Hnappur til að eyða blogfærslu -> FLash tilkynning birtist á stjórnborði
   * "Select" innsláttarreitur til að velja flokk (_Category_)
   * [sýnidæmi](https://blog-admin-ui.netlify.app/)
1. Nemendur kynna kennara verkefni sitt, útskýra alla helstu ofangreinda virkni, eins og tími gefst. <br> **Ef nemandi getur ekki gert grein fyrir kóða sínum, útskýrt útfærslu / virkni telst það vera fall á lykilmati**  

#### Nýjungar: (30% í boði)

1. Notendur geta skráð sig í gagnagrunn og síðan loggað sig inn og skrifað pósta sem birtast í blogginu **(10%)** 
1. [Fileupload](https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/), ljósmyndir fyrir blogfærslur. **(10%)**
1. Vefurinn er hýstur (live production) með [PythonAnywhere](https://www.pythonanywhere.com/). **(10%)**
1. Síða þar sem hægt er að breyta eða bæta við flokkum **(5%)**
1. [Pagination in Flask: Split Your Data Into Pages](https://www.youtube.com/watch?v=U18hO1ngZEQ).  **(5%)**
<!--1. Notaðu [htmx](https://htmx.org/docs/) til að gera vefinn dýnamískan (án þess að reload alla síðu) fyrir [delete](https://youtu.be/O2Xd6DmcB9g?t=1996) aðgerð á blogfærslum og [leit](https://www.youtube.com/watch?v=PWEl1ysbPAY). **(5%)**-->
1. Annað sem nemendur skýra frá í Innu, "_Athugasemd til kennara_" **(5%)**

---

### Skil
- Þjöppuð (zip/rar) mappa með öllum skrám (ekki venv) á Innu
- Láttu fylgja með textaskrá með lista af söfnum sem þarf að pip install (dependencies - pip freeze)
- Vefslóð á hýsingu.
