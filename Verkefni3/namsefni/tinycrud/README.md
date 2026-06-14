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
