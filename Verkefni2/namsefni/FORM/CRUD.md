# Create, Read, Update, Delete

Til að búa til CRUD (Create, Read, Update, Delete) virkni í Flask er algengt að nota **Python orðasöfn (dictionaries)** sem einfaldan gagnagrunn í minni. CRUD stendur fyrir hinar fjórar grunnaraðgerðir gagnavinnslu: að búa til, lesa, uppfæra og eyða gögnum.

Hér er dæmi um hvernig má útfæra þetta í Flask:

### 1. Uppsetning og gagnaskipan
Fyrst þarf að flytja inn nauðsynleg söfn og skilgreina orðasafn til að geyma gögnin.

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Einfaldur "gagnagrunnur" í minni
nemendur = {
    "1": {"nafn": "Jón Jónsson", "netfang": "jon@skoli.is"},
    "2": {"nafn": "Anna Önnu", "netfang": "anna@skoli.is"}
}
```

### 2. Read (Lesa)
Notað til að birta lista yfir alla nemendur eða upplýsingar um einn ákveðinn.

```python
@app.route('/')
def index():
    # Birtir alla nemendur úr orðasafninu
    return render_template('index.html', nemendur=nemendur)

@app.route('/nemandi/<id>')
def view_student(id):
    # Sækir ákveðinn nemanda með lykli (key)
    nemandi = nemendur.get(id)
    return render_template('profile.html', nemandi=nemandi)
```

### 3. Create (Búa til)
Hér er notað **POST** aðferðin til að taka á móti gögnum úr HTML-formi. Nýr hlutur er bætt við orðasafnið með því að skilgreina nýjan lykil.

```python
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Sækir gögn úr formi
        nytt_id = str(len(nemendur) + 1)
        nafn = request.form.get('nafn')
        netfang = request.form.get('netfang')
        
        # Bætir við í orðasafnið
        nemendur[nytt_id] = {"nafn": nafn, "netfang": netfang}
        return redirect(url_for('index'))
    return render_template('create_form.html')
```

### 4. Update (Uppfæra)
Til að uppfæra gögn er gildið á tilteknum lykli í orðasafninu endurskilgreint.

```python
@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        # Uppfærir gildi nemanda
        nemendur[id]['nafn'] = request.form.get('nafn')
        nemendur[id]['netfang'] = request.form.get('netfang')
        return redirect(url_for('index'))
    
    nemandi = nemendur.get(id)
    return render_template('update_form.html', nemandi=nemandi, id=id)
```

### 5. Delete (Eyða)
Nota má `pop()` aðferðina eða `del` skipunina til að fjarlægja færslu úr orðasafninu.

```python
@app.route('/delete/<id>')
def delete(id):
    # Fjarlægir nemanda með gefnu ID
    if id in nemendur:
        nemendur.pop(id)
    return redirect(url_for('index'))
```

### Lykilatriði í útfærslunni:
*   **Routing:** Notað er `@app.route` til að tengja föll við ákveðnar vefslóðir.
*   **Request Object:** Gögnum úr formum er náð í gegnum `request.form`.
*   **Dictionaries:** Orðasöfn eru notuð því þau eru **breytanleg (mutable)**, sem gerir okkur kleift að bæta við, breyta og eyða gögnum á auðveldan hátt.
*   **HTTP Methods:** Mikilvægt er að skilgreina `methods=['POST']` fyrir leiðir sem breyta gögnum.

---

Til að tengja HTML form við Flask kóðann þinn þarf að huga að tveimur hliðum: hvernig formið er uppsett í HTML og hvernig Flask tekur á móti gögnunum með **request** hlutnum.

Hér er ferlið byggt á heimildum:

### 1. HTML hliðin (í templates möppu)
Í HTML skránni þarf formið að hafa tvo mikilvæga eiginleika:
*   **`method="POST"`**: Til að senda gögnin á miðlarann (í stað þess að birta þau í vefslóðinni).
*   **`name` eigindi á inntaksreitum**: Flask notar gildið í `name` til að bera kennsl á gögnin (t.d. `name="nafn"`).

Dæmi um einfalt form (**templates/create_form.html**):
```html
<form method="POST">
    <input type="text" name="nafn" placeholder="Nafn nemanda">
    <input type="email" name="netfang" placeholder="Netfang">
    <button type="submit">Vista</button>
</form>
```

### 2. Flask hliðin (Python kóðinn)
Til að vinna með formið í Flask þarftu að gera eftirfarandi:

*   **Skilgreina leyfðar aðferðir**: Sjálfgefið svara rætur (routes) aðeins við GET beiðnum. Þú verður að bæta við `methods=['GET', 'POST']` í decoratorinn.
*   **Nota `request.form`**: Þegar formið er sent (POST), geturðu nálgast gögnin í gegnum `request.form` orðasafnið.
*   **Sýna formið**: Notaðu `render_template()` til að birta HTML skrána.

Dæmi um tengingu við CRUD orðasafnið úr fyrra dæmi:
```python
from flask import Flask, render_template, request, redirect, url_for

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Gögnin sótt úr forminu með 'name' lyklunum
        nafn = request.form.get('nafn')
        netfang = request.form.get('netfang')
        
        # Hér væri gögnunum bætt við í dictionary eins og í fyrra dæmi
        nytt_id = str(len(nemendur) + 1)
        nemendur[nytt_id] = {"nafn": nafn, "netfang": netfang}
        
        return redirect(url_for('index')) # Senda notanda aftur á forsíðu
        
    # Ef aðferðin er GET, þá birtum við bara formið
    return render_template('create_form.html')
```

### Mikilvæg atriði:
*   **Öryggi**: Flask notar **Jinja2** sem sér sjálfkrafa um að "escape-a" HTML í sniðmátum til að verjast sprautuhótunum (injection attacks).
*   **Villa 400**: Ef þú reynir að nálgast lykil í `request.form` sem er ekki til (t.d. `request.form['vitlaus_lykill']`), skilar Flask sjálfkrafa "400 Bad Request" villu. Mælt er með að nota `.get()` aðferðina til að forðast þetta.
*   **Skrár**: Ef formið á að senda skrár (upload), þarf að muna eftir að bæta við `enctype="multipart/form-data"` í HTML formið.

---

Til að sýna listann yfir nemendur í `index.html` þarftu að nota **Jinja2** sniðmátsmál Flask til að ítra í gegnum gögnin sem þú sendir frá Python rásinni (route).

Hér er hvernig þú framkvæmir það skref fyrir skref:

### 1. Senda gögnin úr Flask rásinni
Í Python skránni þinni þarftu að nota `render_template` fallið og senda orðasafnið (dictionary) með nemendunum sem færibreytu.

```python
@app.route('/')
def index():
    # 'nemendur' er orðasafnið sem geymir gögnin þín
    return render_template('index.html', nemendur=nemendur)
```

### 2. Nota Jinja2 lykkju í index.html
Í HTML skránni notarðu `{% for ... %}` lykkju. Þar sem gögnin eru í orðasafni er best að nota `.items()` aðferðina til að fá bæði lykilinn (ID) og gildið (upplýsingar um nemandann) í hverri ítrun.

Dæmi um **index.html**:
```html
<h1>Listi yfir nemendur</h1>
<ul>
    {% for id, info in nemendur.items() %}
        <li>
            <strong>{{ info.nafn }}</strong> - {{ info.netfang }} 
            <!-- Hægt er að búa til tengil á nánari upplýsingar með ID -->
            <a href="{{ url_for('view_student', id=id) }}">Skoða</a>
        </li>
    {% endfor %}
</ul>
```

### Helstu hugtök:
*   **`render_template`**: Þetta fall leitar að HTML skránni í `templates` möppunni og gerir Python breyturnar aðgengilegar fyrir Jinja sniðmátið.
*   **`nemendur.items()`**: Þessi Python aðferð skilar pari af lykli og gildi, sem gerir þér kleift að meðhöndla bæði ID nemandans og upplýsingarnar um hann samtímis.
*   **`{{ ... }}`**: Tvöfaldir slaufusvigar eru notaðir í Jinja til að birta gildi breytu beint í HTML kóðann.
*   **Öryggi**: Flask og Jinja sjá sjálfkrafa um að **hreinsa (escape)** öll gildi sem sett eru inn í sniðmát til að verjast öryggishótunum eins og sprautuhótunum (injection attacks).

---

Flash-skilaboð í Flask eru notuð til að gefa notendum **endurgjöf** (feedback), sem er lykilatriði í góðu notendaviðmóti. Þegar unnið er með HTML form eru þau oftast notuð til að staðfesta að aðgerð hafi tekist (t.d. „Nemandi vistaður“) eða ef eitthvað fór úrskeiðis.

Hér er hvernig flash-skilaboð virka með HTML formum:

### 1. Forsenda: Leyndarlykill (Secret Key)
Flash-skilaboð eru vistuð í **session** hjá notandanum. Til þess að það virki verður þú að skilgreina `secret_key` í Flask forritinu þínu, annars færðu villu.
```python
app.secret_key = 'einhver-mjög-leyndur-lykill'
```

### 2. Í Python: Skilaboðin send með `flash()`
Þegar notandi sendir inn form (POST beiðni), vinnur þú úr gögnunum og kallar svo á `flash()` fallið áður en þú notar `redirect()` til að senda notandann á nýja síðu. Skilaboðin eru geymd þar til næsta beiðni á sér stað og eyðast svo.

**Dæmi í Python:**
```python
from flask import flash, redirect, url_for, request

@app.route('/create', methods=['POST'])
def create():
    nafn = request.form.get('nafn')
    # ... rökfræði til að vista í gagnagrunn eða dictionary ...
    
    flash(f'Nemandinn {nafn} hefur verið skráður!')
    return redirect(url_for('index'))
```

### 3. Í HTML: Skilaboðin birt með `get_flashed_messages()`
Til að skilaboðin birtist raunverulega í vafranum þarf að sækja þau í HTML sniðmátinu (template) með fallinu `get_flashed_messages()`. Þetta er venjulega gert efst í skjalinu eða í grunnskjali (layout) svo skilaboðin sjáist hvar sem er.

**Dæmi í HTML (Jinja2):**
```html
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class="flashes">
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

### Samantekt á ferlinu:
1.  **Notandi sendir form:** HTML formið notar `method="POST"`.
2.  **Bakendinn vinnur gögnin:** Flask tekur við gögnunum, framkvæmir aðgerð og skráir skilaboð með `flash()`.
3.  **Tilvísun (Redirect):** Miðlarinn skipar vafranum að fara á aðra síðu (t.d. forsíðuna).
4.  **Birting:** Á nýju síðunni keyrir Jinja2 kóðinn, sækir flash-skilaboðin og birtir þau notandanum. Eftir þetta eyðast skilaboðin úr biðröðinni.

---