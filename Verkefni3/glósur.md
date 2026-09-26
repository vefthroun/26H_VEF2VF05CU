# Glósur VEFÞ2VF 

### 1. Flask veframminn (*Quickstart — Flask Documentation*)

*   **Grunnstillingar og keyrsla:**
    *   Forrit er frumstillt með `app = Flask(__name__)`. Breytan `__name__` segir Flask hvar á að leita að sniðmátum (`templates`) og kyrrstæðum skrám (`static`).
    *   Sjálfgefið leitar Flask skipunin að skránni `app.py` eða `wsgi.py`.
    *   **Villuleitarhamur (`Debug Mode`):** Virkjaður með `--debug` eða `debug=True`. Hann endurhleður miðlarann sjálfkrafa við breytingar og sýnir gagnvirkan villuleitara í vafranum. Aðeins ætlað til þróunar — keyrsla í vinnsluumhverfi býður upp á alvarlega öryggisáhættu þar sem hægt er að keyra hvaða Python kóða sem er úr vafranum.
*   **Rásun (Routing) og vefslóðir:**
    *   Skreytingin (decorator) `@app.route()` tengir vefslóð við tiltekið Python birtingarfall.
    *   **Breytilegar slóðir (Variable Rules):** Skilgreindar með `<variable_name>` og hægt er að tilgreina gerðir með breyturum (converters) eins og `<int:id>`, `<float:val>`, `<path:path>` eða `string` (sjálfgefið).
    *   **Skástrik neðst í slóð (Trailing Slashes):** Slóð með skástriki (t.d. `/projects/`) virkar eins og mappa — ef slegið er inn `/projects` áframvísar Flask sjálfkrafa á `/projects/`. Slóð án skástriks (t.d. `/about`) skilar 404 villu ef skástriki er bætt við.
    *   **Slóðasmíð (`url_for()`):** Býr til slóð út frá heiti falls. Kemur í veg fyrir harðkóðun, meðhöndlar sérstafi á öruggan hátt og skilar alltaf algildum (absolute) slóðum.
    *   **HTTP Aðferðir:** Sjálfgefið svara rásir aðeins GET beiðnum. Hægt er að skilgreina aðrar aðferðir með `methods=['GET', 'POST']` eða nota flýtiskreytingar eins og `@app.get()` og `@app.post()`.
*   **Sniðmát og kyrrstæðar skrár:**
    *   Fallið `render_template()` birtir HTML skrár úr möppunni `templates/` og nýtir Jinja2 sniðmátsvélina.
    *   Kyrrstæðar skrár (CSS, myndir, JavaScript) eru geymdar í möppunni `static/` og sóttar með `url_for('static', filename='style.css')`.
    *   Jinja2 hreinsar HTML stafi sjálfkrafa til að koma í veg fyrir XSS árásir, en hægt er að birta samþykkt HTML með `|safe` síunni.
*   **Gagnameðhöndlun, innskráning og svör:**
    *   Aðgangur að formgögnum fæst með `request.form`, URL færibreytum með `request.args`, skrám með `request.files` og kökum með `request.cookies`. Skráarupphal krefst þess að HTML formið noti `enctype="multipart/form-data"`.
    *   Ef reynt er að sækja ótilgreindan lykil úr `request.form` kastar Python `KeyError`, sem Flask breytir sjálfkrafa í **HTTP 400 Bad Request** villusíðu.
    *   `session` hluturinn geymir dulkóðuð gögn notanda á milli beiðna og krefst þess að `app.secret_key` sé skilgreint.
    *   Áframvísun er framkvæmd með `redirect()` og hægt er að stöðva beiðni með `abort()`. Svörum sem eru Python orðasöfn eða listar er sjálfkrafa breytt í JSON svar með `jsonify()`.

---

### 2. Python Orðasöfn og CRUD aðgerðir (*Python Dictionary*)

*   **Skilgreining og eiginleikar:**
    *   Orðasafn (`dict`) geymir gögn í `{key:value}` pörum. Þau eru **röðuð** (frá Python 3.6+), **breytileg (mutable)** og leyfa ekki tvítekna lykla.
*   **C — Create (Stofnun):**
    *   Stofnað með slaufusvigum `{}` (t.d. `my_dict = {"Name": "Jón", "Age": 23}`) eða með `dict()` fallinu.
*   **R — Read (Uppfletting):**
    *   Gildi eru sótt með hornklofum `my_dict[key]`. Ef lykillinn er ekki til kastar Python `KeyError`.
    *   Fallið `my_dict.get(key, default)` er öruggari leið sem skilar `None` (eða sjálfgefnu gildi) án þess að kasta villu ef lykillinn finnst ekki.
    *   `in` virkinn athugar hvort tiltekinn lykill sé til staðar.
*   **U — Update (Uppfærsla og viðbót):**
    *   Gildi er breytt eða nýju staki bætt við með gildistökunni `my_dict[key] = value`.
    *   Aðferðin `my_dict.update(other_dict)` uppfærir mörg pör í einu eða skeytir tveimur orðasöfnum saman.
*   **D — Delete (Eyðing):**
    *   `pop(key)` fjarlægir stak og skilar gildi þess (kastar `KeyError` ef lykill finnst ekki).
    *   `popitem()` fjarlægir og skilar síðasta `(key, value)` parinu sem tuple.
    *   `del my_dict[key]` eyðir staki eða öllu orðasafninu úr minni.
    *   `clear()` tæmir öll pör úr orðasafninu en heldur tómum hlut í minni.
*   **Ítrun og hjálparföll:**
    *   Sjálfgefin `for` lykkja ítrar yfir lykla.
    *   `keys()` skilar öllum lyklum, `values()` skilar gildum og `items()` skilar öllum `(key, value)` pörum sem tuples.
    *   `len()` skilar heildarfjölda para.
*   **Gagnavinnsla**
    *   **Birting á lista í HTML:** Notuð er lykkja `{% for i in a %} <li>{{ a }}</li> {% endfor %}`.
    *   **Birting úr orðasafni:** Gildi eru sótt með `{{ i.nafn }}` eða `{{ i['nafn'] }}`.
    *   **Breytilegar slóðir:** Slóð sem tekur við texta úr `url_for('f', t='string')` er skilgreind sem `@app.route('/f/<string>')`.
    *   **Formvinnsla:** `@app.route('/form', methods=['POST'])` tekur við inntaki með `request.form['txt']`.
    *   **Error Handler:** Skrifað með `@app.errorhandler(404)`.
    *   **Static vs. Dynamic Routing:** Static rásir eru fastar vefslóðir (t.d. `/about`), á meðan dynamic rásir innihalda breytilega hluta sem taka við inntaki úr slóðinni (t.d. `/user/<username>`).

### 3. TinyDB 4.8.2 — Léttur skráargagnagrunnur í Python

#### Grunnatriði og gagnageymsla
* **Gagnagerð:** TinyDB vinnur með gögn í formi Python orðasafna (`dict`) og vistast sjálfgefið á JSON sniði í skrá (t.d. `db.json`).
* **Nýskráning gagna:** Aðferðin `db.insert(...)` bætir skjali við gagnagrunninn og skilar einstöku auðkenni skjalsins (document ID).

#### Sækja og ítrast yfir gögn
* **Ná í öll skjöl:** Aðferðin `db.all()` skilar öllum skjölum sem geymd eru í gagnagrunninum.
* **Ítrun:** Hægt er að ítrast beint yfir gagnagrunninn með `iter(db)`.

#### Fyrirspurnir og leit (`Query()`)
* **Leit:** Aðferðin `db.search(query)` skilar lista af öllum skjölum sem passa við gefið skilyrði.
* **Query hlutur:** `Query()` er notað til að búa til leitarskilyrði, t.d. `Query().field == 2` (styður einnig samanburðarvirkja eins og `!=`, `>`, `>=`, `<`, `<=`).
* **Takmarkanir á fyrirspurnum:** Samanburður í fyrirspurnum styður aðeins fasta-gildi (literals) hægra megin við samanburðarmerkið. Ekki er hægt að bera saman tvo reiti beint (eins og `Query().a == Query().b`) — til þess þarf að nota lambda fall, t.d. `db.search(lambda doc: doc.get('a') == doc.get('b'))`.

#### Uppfærsla og eyðing
* **Uppfærsla:** `db.update(fields, query)` uppfærir öll skjöl sem passa við leitarskilyrðið til að innihalda tilgreinda reiti.
* **Eyðing á skjölum:** `db.remove(query)` eyðir öllum skjölum sem passa við skilyrðið.
* **Tæming gagnagrunns:** `db.truncate()` eyðir öllum skjölum úr gagnagrunninum og skilar tómum grunni.

### 4. TVmaze REST API — Sjónvarpsgögn og vefþjónusta

#### Grunnatriði og uppbygging
* **Grunnvefslóð og snið:** Grunnslóð API-ins er `https://api.tvmaze.com` og þjónustan skilar gögnum á **JSON** formi samkvæmt **HAL** og **HATEOAS** staðlinum.
* **HTTPS og CORS:** Allar slóðir styðja HTTPS og öll köll eru með **CORS** virkjað, sem gerir kleift að kalla í API-ið beint úr vefforritum án proxy-þjóna.
* **Leyfismál:** Ókeypis notkun er háð **CC BY-SA** leyfi, sem krefst þess að TVmaze sé eignaður uppruni gagna (t.d. með hlekk).

#### Endapunktar og leit (Endpoints)
* **Almenn leit (`/search/shows?q=:query`):** Notar fuzzy-reikniverk (fuzziness 2) sem fyrirgefur stafsetningarvillur og skilar öllum mögulegum þáttum raðað eftir relevancy-stigi (`score`).
* **Einstök leit (`/singlesearch/shows?q=:query`):** Skilar eingöngu einum þætti (eða engum) með strangara fuzzy-reikniverki (fuzziness 1) og styður innfellingu gagna (`embed`).
* **Uppfletting og aðrar leitarleiðir:** Hægt er að fletta upp þætti eftir IMDB/TVDB auðkenni (`/lookup/shows?imdb=:id` eða `thetvdb=:id`) eða leita að fólki (`/search/people?q=:query`).
* **Algengir endapunktar:**
  * **Sjónvarpsþáttur:** aðalupplýsingar `/shows/:id`, þáttalisti `/shows/:id/episodes`, árstíðir `/shows/:id/seasons`, leikarar `/shows/:id/cast`, og myndir `/shows/:id/images`.
  * **Stakir þættir:** `/episodes/:id`.
  * **Fólk / Leikarar:** aðalupplýsingar `/people/:id` og leikferill `/people/:id/castcredits`.
* **Uppsöfnun og síðutal (Show Index):** Endapunkturinn `/shows?page=:num` skilar heildarlista þátta (allt að 250 á síðu) sem auðveldar staðbundna samstillingu gagna.

#### Innfelling gagna (Embedding)
* Hægt er að draga tengd gögn inn í sama svar með því að nota `?embed=...` breytuna (t.d. `?embed=episodes` eða `?embed=cast`). Til að innfella mörg söfn í einu er notað fylkjasnið eins og `?embed[]=episodes&embed[]=cast`.

#### Myndir (Images)
* Reiturinn `image` inniheldur orðasafn með lyklunum `medium` (minni gerð) og `original` (upprunaleg upplausn), en skilar `null` ef engin mynd er til staðar.

#### Skyndiminni og Hraðatakmörk (Rate Limiting)
* **Skyndiminni:** Flestar niðurstöður eru geymdar í skyndiminni hjá TVmaze í **60 mínútur**.
* **Hraðatakmörk:** API-ið leyfir að lágmarki **20 köll á hverjum 10 sekúndum** á hverja IP-tölu. Ef farið er yfir mörkin skilar miðlarinn **HTTP 429** stöðukóða. Mælt er með að biðlarinn bíði í smá stund og reyni aftur (back-off).

---