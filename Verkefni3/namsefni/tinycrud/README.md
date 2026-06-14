# TinyDB 

Í stuttu máli: Ef þú þarft einfaldan  API gagnagrunn sem virkar án mikillar fyrirhafnar þá gæti TinyDB verið rétti kosturinn fyrir þig.

* https://tinydb.readthedocs.io/en/latest/
* https://www.tutorialspoint.com/tinydb/index.htm

---

Til að búa til þessa spjallsíðu þurfum við að tengja saman **Flask** fyrir vefumgjörðina, **sessions** fyrir örugga aðgangsstýringu og **TinyDB** sem JSON gagnagrunn.

Hér er hvernig þú getur útfært þetta verkefni:

### 1. Uppsetning og Gagnagrunnur (TinyDB)
TinyDB geymir gögnin í hreinni JSON skrá (`db.json`). Til að tryggja að hún sé óaðgengileg öðrum en appinu, er hún geymd í rótarmöppu verkefnisins en **ekki** í `static` möppunni, því Flask þjónar aðeins skrám úr `static` beint til notenda.

```python
from flask import Flask, render_template, request, session, redirect, url_for, flash
from tinydb import TinyDB, Query

app = Flask(__name__)
app.secret_key = 'mjog-leyndur-lykill' # Nauðsynlegt fyrir session
db = TinyDB('db.json')
posts_table = db.table('posts')
users_table = db.table('users')
User = Query()
Post = Query()
```

### 2. Forsíða (index.html) - Birta alla pósta
Á forsíðunni notarðu `db.all()` til að sækja alla pósta úr TinyDB og birta þá. Samkvæmt kröfunni er enginn breytingahnappur hér, heldur aðeins lestur.

```python
@app.route('/')
def index():
    all_posts = posts_table.all() # Sækir alla pósta
    return render_template('index.html', posts=all_posts)
```

### 3. Session Aðgangsstýring og Innskráning
Til að verja prófílsíðuna notarðu `session` til að geyma `user_id` og `role` (notandi eða vefstjóri).

```python
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    # Hér myndir þú leita að notanda í users_table
    user = users_table.get(User.username == username)
    if user:
        session['user_id'] = user.doc_id # doc_id er sjálfkrafa ID hjá TinyDB
        session['role'] = user.get('role', 'user')
        return redirect(url_for('profile'))
    return "Innskráning mistókst", 401
```

### 4. Prófílsíða (profile.html) - CRUD fyrir eigin pósta
Hér geta notendur búið til nýja pósta með `insert()`, uppfært þá með `update()` eða eytt þeim með `remove()`. Lykilatriðið er að sía póstana þannig að notandi sjái aðeins sína eigin.

```python
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    
    # Sækja aðeins pósta þessa notanda
    user_posts = posts_table.search(Post.author_id == session['user_id'])
    return render_template('profile.html', posts=user_posts)

@app.route('/post/new', methods=['POST'])
def new_post():
    if 'user_id' in session:
        posts_table.insert({
            'author_id': session['user_id'],
            'content': request.form.get('content')
        })
    return redirect(url_for('profile'))
```

### 5. Aðgangur Vefstjóra (Admin)
Vefstjórinn hefur sérstaka rás þar sem athugað er hvort `session['role'] == 'admin'`. Hann getur eytt hvaða pósti eða notanda sem er.

```python
@app.route('/admin/delete_post/<int:post_id>')
def admin_delete_post(post_id):
    if session.get('role') == 'admin':
        posts_table.remove(doc_ids=[post_id])
        flash("Pósti eytt af vefstjóra")
    return redirect(url_for('index'))

@app.route('/admin/delete_user/<int:user_id>')
def admin_delete_user(user_id):
    if session.get('role') == 'admin':
        users_table.remove(doc_ids=[user_id])
        # Einnig mætti eyða öllum póstum notandans
        posts_table.remove(Post.author_id == user_id)
    return redirect(url_for('index'))
```
---

Fyrir spjallforrit af þessari stærðargráðu er besta leiðin að nýta **erfðir í sniðmátum** (e. template inheritance) í gegnum Jinja2 vélina í Flask. Þetta gerir þér kleift að halda sameiginlegum hlutum síðunnar (eins og haus, valmynd og fæti) á einum stað og forðast endurtekningu á kóða.

Hér er mælt með eftirfarandi skiptingu í `templates` möppunni:

### 1. Grunnskjalið: `layout.html`
Þetta er mikilvægasta skráin þar sem hún hýsir alla grunn-HTML uppsetninguna. Hér myndir þú setja:
*   `<head>` hlutann með tengingum í CSS í `static` möppuna.
*   **Nav-bar:** Valmynd sem breytist eftir því hvort notandi er innskráður (með því að skoða `session` hlutinn beint í sniðmátinu).
*   **Flash-skilaboð:** Stað þar sem villu- eða staðfestingarskilaboð birtast með `get_flashed_messages()`.
*   **`{% block content %}`:** Svæði þar sem hinar síðurnar munu „skrifa“ sitt eigið innihald.

### 2. Forsíðan: `index.html`
Þessi síða á að **erfa** frá `layout.html` (með `{% extends 'layout.html' %}`).
*   Hún inniheldur lykkju sem fer í gegnum alla pósta úr TinyDB og birtir þá í tímaröð.
*   Hér er engin eyðingar- eða breytingarvirkni sýnileg venjulegum notendum [Conversation].

### 3. Innskráning: `login.html`
*   Inniheldur einfalt HTML form með `method="POST"` til að senda notandanafn og lykilorð á miðlarann.
*   Nýtir sömu grunnútlitshönnun og aðrar síður.

### 4. Notendasíða: `profile.html`
Þetta er „lokaða“ svæðið þitt þar sem:
*   Notandinn sér listann yfir sína eigin pósta.
*   **CRUD aðgerðir:** Hér birtast sérstakir „eyða“ og „breyta“ hnappar sem nota `url_for()` til að kalla á réttar rætur (routes) í Flask [35, Conversation].
*   Hér er form til að skrifa nýja pósta.

### 5. (Valfrjálst) Vefstjórasíða: `admin.html`
*   Ef kerfið er umfangsmikið er gott að hafa sérstaka síðu fyrir vefstjóra þar sem hann sér yfirlit yfir alla notendur og pósta með möguleika á að fjarlægja þá [Conversation].

### Möppuskipan
Skipulagið ætti að líta svona út í verkefninu þínu:
*   `/app.py` (Aðalskráin þín)
*   `/db.json` (TinyDB gagnagrunnurinn - geymdur utan static svo hann sé ekki aðgengilegur beint) [Conversation]
*   `/static/` (Fyrir CSS og myndir)
*   `/templates/`
    *   `layout.html`
    *   `index.html`
    *   `login.html`
    *   `profile.html`
    *   `admin.html`

Með því að nota `url_for()` í þessum skrám tryggir þú að tenglar á milli síðna og í static skrár virki alltaf rétt, óháð því hvernig vefslóðirnar breytast.

### Öryggisatriði úr heimildum:
*   **HTML Escaping:** Flask og Jinja2 sjá sjálfkrafa um að hreinsa (escape) það sem notendur skrifa í póstana sína til að koma í veg fyrir sprautuhótanir (injection attacks).
*   **Secret Key:** Mikilvægt er að hafa sterkan `secret_key` svo notendur geti ekki falsað session-kökurnar sínar og gefið sér admin-réttindi.
*   **TinyDB Query:** Notaðu `Query()` hlutinn frá TinyDB til að gera leitirnar öruggar og skýrar.

---

Til að uppfæra póst í TinyDB, til dæmis á „profile“ síðunni þinni, er aðalskipunin **`db.update(fields, query)`**. 

Hér er nánari útskýring á þeim skipunum sem þarf að nota:

*   **`db.update(fields, query)`**: Þessi skipun uppfærir alla þá skjöl (pósta) sem passa við gefna fyrirspurn (query). 
    *   **`fields`**: Hér setur þú inn Python orðasafn (dict) með þeim gögnum sem þú vilt breyta eða bæta við. Til dæmis: `{'content': 'Hér er uppfærður texti'}`.
    *   **`query`**: Þetta skilgreinir hvaða póst á að uppfæra.
*   **`Query()`**: Þú þarft að búa til fyrirspurnarhlut (query object) til að finna rétta póstinn. 

### Dæmi um útfærslu í „profile“ samhengi:
Þar sem þú vilt að notendur geti aðeins uppfært sína eigin pósta, væri öruggast að nota skipunina þannig að hún síaði bæði eftir **ID póstsins** og **ID notandans** úr session-inu:

```python
from tinydb import Query
Post = Query()

# Uppfærir póstinn þar sem ID póstsins passar OG höfundurinn er sá sem er innskráður
db.update(
    {'content': nyr_texti}, 
    (Post.doc_id == valinn_id) & (Post.author_id == session['user_id'])
)
```

**Lykilatriði:**
*   Skipunin skilar lista yfir ID þeirra skjala sem var breytt.
*   Hægt er að nota hvers kyns samanburð í fyrirspurninni (t.d. `==`, `!=`, `>`, osfrv.) til að finna réttu gögnin.
*   Ef þú ert með ID skjalsins beint (t.d. `doc_id`), getur þú einnig notað `db.update(fields, doc_ids=[id])`.

---

Til að tengja nýja spjallpósta við ákveðinn notanda í TinyDB er algengasta og öruggasta leiðin að geyma **notanda-ID** í **session** þegar notandinn skráir sig inn, og bæta því ID-i svo við sem sérstökum reit í póst-orðasafnið þegar þú vistar það í gagnagrunninn.

Hér er ferlið skref fyrir skref:

### 1. Geyma notanda-ID í Session
Þegar notandi skráir sig inn þarftu að vista auðkenni hans (t.d. `user_id`) í session svo hægt sé að nálgast það síðar. 
*Athugið að Flask krefst þess að `app.secret_key` sé stilltur til að nota sessions.*

### 2. Sækja gögn úr formi og Session
Þegar notandinn sendir nýjan póst í gegnum HTML-form (POST beiðni), notarðu `request.form` til að sækja póstinn sjálfan og `session` til að sækja auðkenni höfundarins.

### 3. Vista í TinyDB með `insert()`
TinyDB væntir þess að gögn séu á formi Python orðasafna (dictionaries). Þú býrð til orðasafn sem inniheldur bæði texta póstsins og notanda-ID-ið og notar svo `insert()` aðferðina.

**Dæmi um útfærslu í Flask:**

```python
from flask import request, session, redirect, url_for
from tinydb import TinyDB

db = TinyDB('db.json')
posts_table = db.table('posts')

@app.route('/create_post', methods=['POST'])
def create_post():
    # 1. Athugum hvort notandi sé innskráður
    if 'user_id' in session:
        # 2. Sækjum gögnin (post-innihald og notanda-id)
        post_content = request.form.get('content') # Úr HTML formi
        author_id = session['user_id']             # Úr session
        
        # 3. Búum til orðasafn og vistum í TinyDB
        new_post = {
            'author_id': author_id,
            'content': post_content,
            'timestamp': '2026-06-14' # Dæmi um aukagögn
        }
        
        posts_table.insert(new_post)
        return redirect(url_for('index'))
    
    return "Þú verður að vera innskráður", 401
```

### Helstu kostir þessarar aðferðar:
*   **Tenging gagna:** Með því að geyma `author_id` með hverjum pósti geturðu síðar notað `db.search()` til að finna alla pósta sem tiltekinn notandi hefur skrifað.
*   **Öryggi:** Þar sem Flask skrifar undir session-kökur með leyndarlykli, getur notandinn ekki auðveldlega falsað `author_id` sitt til að þykjast vera annar notandi þegar hann sendir inn póst.
*   **Einfaldleiki:** TinyDB meðhöndlar þessi tengsl sjálfkrafa þar sem þetta eru bara venjuleg JSON gögn í skrá.

---

Til þess að takmarka eyðingu pósts þannig að aðeins höfundur hans geti eytt honum þarf að nota samspil á milli **session-stýringar** í Flask og **fyrirspurna** í TinyDB.

Hér er ferlið útskýrt í þremur skrefum:

### 1. Geyma notanda-ID í Session
Þegar notandi skráir sig inn þarf að vista einkvæmt auðkenni hans í `session`. Þetta gerir kerfinu kleift að vita hvaða notandi er að reyna að framkvæma eyðinguna.
```python
session['user_id'] = logged_in_user_id
```

### 2. Skilgreina tengingu í gagnagrunni
Hver póstur í TinyDB verður að innihalda reit sem vísar í höfundinn (t.d. `author_id`). Þegar póstur er búinn til er hann vistaður sem orðasafn (dict) með þessum upplýsingum.

### 3. Nota samsetta fyrirspurn við eyðingu
Í stað þess að eyða pósti eingöngu eftir ID-i póstsins, þá notarðu skipunina `db.remove(query)` með **og-skilyrði** (`&`) í TinyDB. Þannig er pósti aðeins eytt ef bæði ID póstsins og ID notandans úr session-inu passa saman.

**Dæmi um útfærslu í Flask rás (route):**
```python
from flask import session, redirect, url_for
from tinydb import TinyDB, Query

db = TinyDB('db.json')
Post = Query()

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    # 1. Athuga hvort notandi sé yfirhöfuð innskráður
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # 2. Keyra eyðingu með tvöföldu skilyrði
    # Póstinum er aðeins eytt ef hann hefur rétt ID OG höfundurinn er réttur
    db.remove((Post.doc_id == post_id) & (Post.author_id == session['user_id']))
    
    return redirect(url_for('profile'))
```

### Helstu kostir þessarar nálgunar:
*   **Öryggi:** Jafnvel þótt notandi reyni að kalla beint á eyðingar-slóð annars notanda (t.d. `/delete/50`), þá mun TinyDB ekki finna neinn póst sem passar við bæði ID 50 og `user_id` þess sem reynir eyðinguna.
*   **Einfaldleiki:** Þú þarft ekki að sækja póstinn fyrst til að athuga hver á hann; TinyDB sér um síuna í einni skipun.
*   **Gagnaöryggi:** Með því að nota `session` eru notendaupplýsingarnar dulkóðaðar í vafrakökum, sem kemur í veg fyrir að notandinn geti breytt ID-inu sínu handvirkt.

---

Að búa til sérstakt **„admin“** hlutverk í TinyDB felst ekki í því að stilla gagnagrunninn sjálfan, heldur að geyma upplýsingar um hlutverk (e. role) sem sérstakan reit (key) í orðasafni (dict) notandans. TinyDB geymir öll gögn sem Python orðasöfn, svo þú einfaldlega bætir við reitnum `'role': 'admin'` þegar þú býrð til notandann.

Hér er ferlið byggt á heimildum og fyrri samskiptum:

### 1. Skilgreina hlutverkið í gagnagrunni
Þegar þú setur notanda inn í `users` töflu TinyDB með `insert()` aðferðinni, bætirðu við hlutverkinu:

```python
from tinydb import TinyDB, Query
db = TinyDB('db.json')
users_table = db.table('users')

# Búa til admin notanda
users_table.insert({
    'username': 'vefstjori',
    'role': 'admin',
    'password': '...' 
})
```

### 2. Sækja hlutverkið við innskráningu
Þegar notandi skráir sig inn notarðu `Query()` til að finna hann og geymir svo hlutverkið í **Flask session**. Þetta gerir kerfinu kleift að muna réttindi notandans á milli síðna.

```python
from flask import session

User = Query()
user = users_table.get(User.username == form_username)

if user:
    session['user_id'] = user.doc_id # doc_id er sjálfkrafa ID í TinyDB
    session['role'] = user.get('role', 'user') # Sækir 'admin' eða sjálfgefið 'user'
```

### 3. Aðgangsstýring í Flask rás (Route)
Til að verja sérstakar aðgerðir (eins og að eyða póstum eða öðrum notendum) notarðu einfalda `if` skilyrðingu til að athuga hvaða hlutverk er vistað í session-inu [Conversation].

```python
@app.route('/admin/delete_user/<int:user_id>')
def delete_user(user_id):
    # Athugum hvort hlutverkið í session sé 'admin'
    if session.get('role') == 'admin':
        users_table.remove(doc_ids=[user_id]) # Eyða notanda
        return "Notanda eytt"
    else:
        # Ef ekki admin, þá sýna villu eða neita aðgangi
        return "Aðgangur aðeins fyrir vefstjóra", 401
```

### Lykilatriði:
*   **Sveigjanleiki:** Þar sem TinyDB geymir orðasöfn geturðu auðveldlega bætt við eða breytt hlutverkum með `update()` skipuninni, t.d. `db.update({'role': 'admin'}, User.username == 'jon')`.
*   **Öryggi:** Gættu þess að hafa sterkan `app.secret_key` í Flask svo notendur geti ekki sjálfir breytt hlutverkinu sínu í session-inu í vafranum.
*   **Sjálfgefin gildi:** Notaðu `.get('role', 'user')` þegar þú sækir hlutverkið svo forritið hrynji ekki ef einhvern notanda vantar hlutverka-reitinn í gagnagrunninum.

---

Til að hanna **`layout.html`** þannig að það nýti erfðir (e. template inheritance) í Flask, þarftu að búa til grunnskjal sem inniheldur þá þætti sem eiga að vera eins á öllum síðum forritsins. Þetta sparar vinnu þar sem þú þarft ekki að endurtaka sama HTML kóðann fyrir hverja síðu.

Hér er hvernig þú hannar þetta skref fyrir skref:

### 1. Uppsetning á `layout.html`
Þetta skjal virkar sem „skelin“ fyrir vefinn þinn. Þú skilgreinir sérstök **blokkir** (e. blocks) þar sem undirsíðurnar munu setja sitt eigið innihald.

**Dæmi um uppbyggingu:**
```html
<!DOCTYPE html>
<html lang="is">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Vefforritun 1{% endblock %}</title>
    <!-- Tenging við CSS skrá í static möppu með url_for -->
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <!-- Sameiginleg valmynd fyrir allar síður -->
        <a href="{{ url_for('index') }}">Forsíða</a>
        <a href="{{ url_for('login') }}">Innskrá</a>
    </nav>

    <main>
        <!-- Birting á flash-skilaboðum (feedback) -->
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            {% for message in messages %}
              <div class="flash">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        <!-- Hér kemur innihald undirsíðna -->
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>© 2026 Tækniskólinn - Vefforritun 1</p>
    </footer>
</body>
</html>
```

### 2. Lykilatriði í hönnuninni
*   **`{% block content %}`**: Þetta er mikilvægasta skipunin. Hún segir Jinja að hér eigi að setja innihald frá öðrum síðum.
*   **Sameiginlegir þættir**: Þú setur haus (header), valmynd (navigation) og fót (footer) beint í `layout.html` svo þeir birtist alls staðar.
*   **Static skrár**: Notaðu `url_for('static', filename='...')` til að tengja CSS og JavaScript svo slóðirnar séu alltaf réttar, óháð því hvar notandinn er staddur á síðunni.
*   **Flash skilaboð**: Best er að setja `get_flashed_messages()` í grunnskjalið svo að endurgjöf til notandans (t.d. „Innskráning tókst“) birtist alltaf á réttum stað.

### 3. Hvernig undirsíður (t.d. `index.html`) nýta erfðirnar
Þegar þú býrð til nýja síðu byrjarðu hana á því að „erfa“ frá grunnskjalinu með **`extends`** skipuninni og fyllir svo í blokkirnar.

**Dæmi um `index.html`:**
```html
{% extends "layout.html" %}

{% block title %}Forsíða - Spjallborð{% endblock %}

{% block content %}
    <h1>Velkomin á spjallborðið</h1>
    <p>Hér er listi yfir nýjustu póstana...</p>
{% endblock %}
```

Með þessari hönnun verður auðveldara að breyta útlitinu á öllum vefnum í einu; þú breytir einfaldlega `layout.html` og allar undirsíður fylgja með sjálfkrafa.
