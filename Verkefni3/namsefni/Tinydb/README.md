# TinyDB 

Ef þú þarft einfaldan API gagnagrunn sem virkar án mikillar fyrirhafnar þá gæti TinyDB verið rétti kosturinn fyrir þig.

* https://tinydb.readthedocs.io/en/latest/
* https://www.tutorialspoint.com/tinydb/index.htm

---

Til að búa til þessa spjallsíðu þurfum við að tengja saman **Flask** fyrir vefumgjörðina, **sessions** fyrir örugga aðgangsstýringu og **TinyDB** sem JSON gagnagrunn.

### 1. Bakendinn: `app.py`

Pakkarnir sem notaðir eru í appinu eru **session** fyrir auðkenningu, **TinyDB** fyrir gögnin, **os** og **datetime** úr stýrikerfinu,  og **pprint** til að gera json söfnin læsileg í terminal

```python

from flask import Flask, render_template, request, redirect, url_for, session, flash
from tinydb import TinyDB, Query
import os                       # að búa til leynilykil með stýrikerfi í Flask appinu
from datetime import datetime   # fyrir tímaskráningu pósta í spjallborði
from pprint import pprint       # pprint er python safninu

app = Flask(__name__)

```
### Secret key for session management

```python

app.config["SECRET_KEY"] = os.urandom(16)
# Display the secret key in console ONLY for debugging
pprint(app.config["SECRET_KEY"])

```

### Uppsetning TinyDB

```python

db = TinyDB('db.json')
users_table = db.table('users')
posts_table = db.table('posts')
fav_table = db.table('favorites')
User = Query()
Post = Query()

# --- HJÁLPARFÖLL ---
def get_posts_with_users():
    all_posts = posts_table.all()
    for post in all_posts:
        # Nota author_id til að finna notanda [6, Conversation]
        user = users_table.get(doc_id=post['author_id'])
        post['username'] = user['username'] if user else "Óþekktur"
        post['id'] = post.doc_id # Ná í doc_id fyrir eyðingu/uppfærslu
    return all_posts

```

### Uppsetning Gagnagrunns
TinyDB geymir gögn sem Python orðasöfn (dicts) í JSON skrá. [Sjá nánari skýringu neðst á síðunni](https://github.com/vefthroun/26H_VEF2VF05CU/blob/main/Verkefni3/namsefni/Tinydb/README.md#gagnagrunnurinn-dbjson)

### Forsíða með póstum, innskráning, nýskráning og prófílsíða með CRUD virkni

Ferlið við að smíða vefkerfi sem styður nýskráningu, innskráningu og CRUD aðgerðir (Create, Read, Update, Delete) fyrir spjallpósta með **TinyDB** sem gagnagrunn.

```python
# --- RÁSIR (ROUTES) ---

@app.route('/')
def index():
    posts = get_posts_with_users()
    return render_template('index.html', posts=posts)

```

## 2. Innskráning (Create & Authenticate)
Til að kerfið virki þarf notandi að geta búið til aðgang og skráð sig inn. Við notum **Flask session** til að muna eftir innskráðum notendum.

```python

```

### Nýskráning (`/signup`)
Gögnum er safnað úr formi og vistuð í `users` töfluna með `insert()`.
1. Sækja `username` og `password` úr `request.form`.
2. Vista í TinyDB. `insert()` skilar sjálfkrafa einstöku ID (doc_id).

```python

```

### Innskráning (`/login`)
1. Leita að notanda með `Query()` þar sem notandanafn passar.
2. Ef notandi finnst, vistum við `user_id` hans í `session['user_id']` [57, Conversation].
3. **login.html:** Þetta skjal þarf að innihalda form með `method="POST"` sem sendir gögnin á viðeigandi rás.

```python

```

## 3. Forsíða: Lesa gögn (Read on Index)
Á forsíðunni viljum við birta alla pósta ásamt upplýsingum um höfund og tímasetningu 

1. Sækjum alla pósta með `posts_table.all()`.
2. Fyrir hvern póst flettum við upp höfundi í `users_table` með því að nota `author_id` póstsins
3. Sendum listann á `index.html` með `render_template()`.

**Mikilvægt:** Til að íslenskir stafir birtist rétt þarf `layout.html` að innihalda `<meta charset="UTF-8">` 

```python

```

## 4. Prófílsíða og Aðgangsstýring
Prófílsíðan sýnir aðeins þá pósta sem tilheyra innskráðum notanda.

1. Athugum hvort `user_id` sé í `session`.
2. Notum `posts_table.search(Query().author_id == session['user_id'])` til að sía gögnin [6, 7, Conversation].

## 5. Stjórnun pósta (Create, Update, Delete)

### Búa til póst (Create)
Notandi skrifar texta í form. Við bætum við `author_id` úr session og tímastimpli áður en við vistum [20, Conversation].
```python
new_post = {
    'content': request.form.get('content'),
    'author_id': session['user_id'],
    'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M") # íslensk tímaröð
}
posts_table.insert(new_post)
```

### Uppfæra póst (Update)
Til að breyta pósti notum við `update()` aðferðina þar sem við skilgreinum nýju gögnin og hvaða póst á að uppfæra.
```python
posts_table.update({'content': nyr_texti}, Query().doc_id == post_id)
```

### Eyða pósti (Delete)
Til að eyða notum við `remove()`. Gættu þess að notandi geti aðeins eytt sínum eigin póstum (nema hann sé með **admin** hlutverk) [6, 7, Conversation].
```python
posts_table.remove(doc_ids=[int(post_id)])
```

> **Athugið:** Allar skrár (`.py`, `.html`, `.json`) skulu vistaðar með **UTF-8** kóðun til að tryggja að íslenskir sérstafir skili sér rétt frá bakenda yfir í Jinja sniðmát [Conversation].

---

Hér er grunnkóðinn fyrir Flask forritið og HTML sniðmátin sem fylgja þeirri rökréttu uppbyggingu sem við ræddum: 

Gættu þess að vista allar skrár með **UTF-8** kóðun svo íslenskir stafir birtist rétt [Conversation].





@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password') # Í alvöru kerfi þarf að hasha þetta!
        
        if not users_table.search(User.username == username):
            users_table.insert({'username': username, 'password': password, 'role': 'user'})
            flash("Nýskráning tókst! Skráðu þig inn.")
            return redirect(url_for('login'))
        flash("Notandanafn er frátekið.")
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users_table.get((User.username == username) & (User.password == password))
        
        if user:
            session['user_id'] = user.doc_id # Vista ID í session
            session['username'] = user['username']
            return redirect(url_for('profile'))
        flash("Rangt notandanafn eða lykilorð.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    if 'user_id' not in session: 
        return redirect(url_for('login'))
    # Sækja aðeins pósta þessa notanda [7, Conversation]
    my_posts = posts_table.search(Post.author_id == session['user_id'])
    for p in my_posts: p['id'] = p.doc_id
    return render_template('profile.html', posts=my_posts)

@app.route('/create_post', methods=['POST'])
def create_post():
    if 'user_id' in session:
        content = request.form.get('content')
        posts_table.insert({
            'content': content,
            'author_id': session['user_id'],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
    return redirect(url_for('profile'))

@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    post = posts_table.get(doc_id=post_id)
    if post and post['author_id'] == session.get('user_id'):
        posts_table.remove(doc_ids=[post_id])
        flash("Pósti eytt.")
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
```

### 2. Sniðmát (Templates)

#### `templates/layout.html`
Grunnskjalið sem öll önnur erfa frá. Hér er **UTF-8** stillingin [Conversation].
```html
<!DOCTYPE html>
<html lang="is">
<head>
    <meta charset="UTF-8"> <!-- Mikilvægt fyrir íslenska stafi! -->
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">Forsíða</a>
        {% if session.user_id %}
            <a href="{{ url_for('profile') }}">Mín síða ({{ session.username }})</a>
            <a href="{{ url_for('logout') }}">Útskrá</a>
        {% else %}
            <a href="{{ url_for('login') }}">Innskrá</a>
            <a href="{{ url_for('signup') }}">Nýskrá</a>
        {% endif %}
    </nav>

    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for msg in messages %}<p>{{ msg }}</p>{% endfor %}
        {% endif %}
    {% endwith %}

    <main>{% block content %}{% endblock %}</main>
</body>
</html>
```

#### `templates/index.html`
Birtir alla pósta með notendanafni og tíma [Conversation].
```html
{% extends "layout.html" %}
{% block title %}Spjallborð{% endblock %}
{% block content %}
    <h1>Nýjustu færslur</h1>
    {% for post in posts %}
        <div class="post">
            <p>{{ post.content }}</p>
            <small>Sent af: {{ post.username }} | {{ post.timestamp }}</small>
        </div>
        <hr>
    {% endfor %}
{% endblock %}
```

#### `templates/login.html`
```html
{% extends "layout.html" %}
{% block content %}
    <h2>Innskráning</h2>
    <form method="POST">
        Notandanafn: <input type="text" name="username" required><br>
        Lykilorð: <input type="password" name="password" required><br>
        <button type="submit">Innskrá</button>
    </form>
{% endblock %}
```

#### `templates/profile.html`
Hér getur notandi búið til nýjan póst og eytt sínum eigin [6, 20, Conversation].
```html
{% extends "layout.html" %}
{% block content %}
    <h1>Velkomin(n), {{ session.username }}</h1>
    
    <h3>Búa til nýjan póst</h3>
    <form action="{{ url_for('create_post') }}" method="POST">
        <textarea name="content" required></textarea><br>
        <button type="submit">Senda póst</button>
    </form>

    <hr>
    <h3>Mínir póstar</h3>
    {% for post in posts %}
        <div class="my-post">
            <p>{{ post.content }}</p>
            <small>{{ post.timestamp }}</small> | 
            <a href="{{ url_for('delete_post', post_id=post.id) }}" onclick="return confirm('Eyða?')">Eyða</a>
        </div>
    {% endfor %}
{% endblock %}
```

### Lykilatriði:
1.  **UTF-8**: Meta-tagið í `layout.html` kemur í veg fyrir skrípi-stafi eins og „Ã¦“ [Conversation].
2.  **Tenging gagna**: Í `index()` rásinni flettum við upp notanda í hvert sinn sem póstur er birtur til að sýna nafn en ekki bara ID-tölu [6, Conversation].
3.  **CRUD**: `profile.html` sýnir hvernig á að eyða (`remove`) og búa til (`insert`) gögn í TinyDB.

---

Til að útfæra **`signup.html`** þarftu að búa til HTML-form sem sendir gögnin (notandanafn og lykilorð) á bakendann með `POST` aðferðinni. Sniðmátið á að nota Jinja2 erfðir til að fylgja útliti vefsins þíns og birta endurgjöf ef eitthvað fer úrskeiðis.

Hér er hvernig þú setur síðuna upp:

### 1. Nota erfðir (`{% extends %}`)
Eins og rætt hefur verið í fyrri samtölum okkar á síðan að byrja á því að erfa frá **`layout.html`** [Conversation]. Þetta tryggir að hún hafi sömu valmynd og útlit og aðrar síður.

### 2. Uppsetning formsins
Formið þarf að nota `method="POST"` til að flytja gögnin á öruggan hátt í `request.form` safnið í Flask. Við notum `url_for('signup')` í `action` eigindinu til að vísa á rétta rás í bakendanum.

### Dæmi um `signup.html`:
```html
{% extends "layout.html" %}

{% block title %}Nýskráning{% endblock %}

{% block content %}
    <h2>Búa til nýjan aðgang</h2>

    {# Formið sendir gögnin á /signup rásina með POST #}
    <form action="{{ url_for('signup') }}" method="POST">
        <div>
            <label for="username">Notandanafn:</label>
            {# 'name' eigindið verður að passa við request.form.get('username') í Python #}
            <input type="text" id="username" name="username" required>
        </div>
        
        <div>
            <label for="password">Lykilorð:</label>
            <input type="password" id="password" name="password" required>
        </div>

        <button type="submit">Nýskrá</button>
    </form>

    <p>Áttu þegar aðgang? <a href="{{ url_for('login') }}">Innskráning hér</a></p>
{% endblock %}
```

### Mikilvæg atriði við útfærsluna:

*   **`name` eigindið**: Þetta er mikilvægasti hlutinn. Gildin í `name="username"` og `name="password"` verða að vera nákvæmlega þau sömu og þú notar í Python kóðanum þegar þú kallar í `request.form.get()` [49, Conversation].
*   **Öryggi og endurgjöf**:
    *   Flask og Jinja2 sjá sjálfkrafa um að **hreinsa (escape)** gögnin sem notandinn slær inn til að verjast sprautuhótunum (injection attacks).
    *   Ef notandanafnið er þegar til í **TinyDB**, mun bakendinn nota `flash()` til að gefa skilaboð [60, Conversation]. Gakktu úr skugga um að `layout.html` skjalið þitt sé með lykkju til að birta þessi skilaboð með `get_flashed_messages()`.
*   **Vefslóðir**: Notaðu alltaf **`url_for()`** til að búa til hlekki á milli síðna (t.d. yfir á innskráningu). Það er öruggara en að harðkóða slóðir eins og `/login`.

Með þessari uppsetningu smellpassar síðan við bakendann sem við bjuggum til áðan og vistar nýja notendur sem orðasöfn (dictionaries) í **`db.json`** skránni [5, Conversation].

---

Það er einfalt að bæta við **'admin'** hlutverki (role) í bakendanum þar sem TinyDB geymir gögn sem sveigjanleg Python orðasöfn. Þú getur bætt við hvaða lykli sem er í notandagögnin án þess að breyta uppsetningu gagnagrunnsins sérstaklega [20, Conversation].

Hér er hvernig þú útfærir hlutverkakerfi:

### 1. Sjálfgefið hlutverk við nýskráningu
Í `signup` rásinni (route) bætirðu við `'role': 'user'` sem sjálfgefnu gildi þegar nýr notandi er búinn til [20, Conversation].

```python
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Við bætum 'role' lyklinum við orðasafnið
    nyr_notandi = {
        'username': username, 
        'password': password, 
        'role': 'user'  # Allir byrja sem venjulegir notendur
    }
    users_table.insert(nyr_notandi)
    return redirect(url_for('login'))
```

### 2. Vista hlutverk í Session
Þegar notandi skráir sig inn er gott að geyma hlutverkið í `session` svo þú þurfir ekki að fletta því upp í gagnagrunninum í hvert sinn sem notandinn hleður síðu.

```python
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    user = users_table.get(Query().username == username)
    
    if user:
        session['user_id'] = user.doc_id
        session['role'] = user.get('role', 'user') # Sækjum hlutverkið
        return redirect(url_for('index'))
```

Til þess að bæta við skilyrði fyrir stjórnanda (administrator) í `/login` rásinni þarftu að nota `request.form` til að sækja gögnin og uppfæra svo `session` hlutinn með viðeigandi hlutverki (role).

Hér er hvernig þú getur breytt rásinni til að tryggja að notandinn „admin“ fái réttindi í session:

### Uppfærð `/login` rás

```python
@app.route('/login', methods=['GET', 'POST']) # 1. Skilgreinum báðar aðferðir 
def login():
    # 2. Ef aðferðin er POST, þá vinnum við úr gögnunum úr forminu 
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Leitum að notanda í TinyDB (Conversation history)
        user = users_table.get((User.username == username) & (User.password == password))
        
        if user:
            session['user_id'] = user.doc_id # Vistum í session 
            
            # Skilyrði fyrir administrator eins og þú baðst um (Conversation history)
            if username == 'admin':
                session['role'] = 'admin'
            else:
                session['role'] = user.get('role', 'user')
                
            return redirect(url_for('profile')) # Sendum á prófíl eftir innskráningu [5]
        
        # Ef upplýsingar voru rangar
        flash("Rangt notandanafn eða lykilorð.") # Gefum feedback [6]
        return redirect(url_for('login'))

    # 3. Ef aðferðin er GET (notandi bara að opna síðuna), birtum við formið [7]
    return render_template('login.html')

```

### Mikilvæg atriði:

*   **Session hluturinn:** `session` í Flask virkar eins og Python orðasafn (dict) þar sem þú getur geymt upplýsingar sem eiga að fylgja notandanum á milli síðna.
*   **Secret Key:** Mundu að þú verður að vera með `app.secret_key` stilltan í forritinu þínu til að `session` virki, annars færðu villu þegar reynt er að skrifa í það.
*   **Öryggi:** Með því að vista `session['role'] = 'admin'` geturðu á öðrum síðum (eins og í `admin_panel`) einfaldlega athugað þetta gildi áður en þú hleypir notandanum áfram.
*   **Gagnageymsla:** Þar sem TinyDB vinnur með orðasöfn er auðvelt að fletta upp notandanum og athuga hvort hann sé sá sem hann segist vera áður en réttindin eru veitt.

---

### 3. Aðgangsstýring í rás (Admin check)
Þú getur nú búið til rásir sem aðeins 'admin' hefur aðgang að með því að nota einfalda `if` skilyrðingu [Conversation].

```python
@app.route('/admin_panel')
def admin_panel():
    # Athugum hvort notandi sé innskráður OG sé admin
    if session.get('role') == 'admin':
        allir_notendur = users_table.all()
        return render_template('admin.html', users=allir_notendur)
    
    # Ef ekki admin, sendum hann burt með villuboðum
    flash("Þú hefur ekki aðgang að þessari síðu.")
    return redirect(url_for('index'))
```

### 4. Uppfæra notanda í Admin
Til að gera venjulegan notanda að admin geturðu notað `update()` aðferðina í TinyDB. Þetta er hægt að gera handvirkt í Python eða í gegnum sérstaka stjórnunarsíðu.

```python
# Uppfærum notanda með ákveðið notendanafn í admin
users_table.update({'role': 'admin'}, Query().username == 'gummi')
```

### Lykilatriði:
*   **Sveigjanleiki**: Þar sem orðasöfn í Python eru breytanleg (mutable) er auðvelt að bæta við fleiri hlutverkum síðar, t.d. 'moderator'.
*   **Öryggi**: Mundu að athuga alltaf `session.get('role')` á bakendanum (í Python) en ekki bara fela hnappa í HTML-inu, þar sem tæknilega þenkjandi notendur gætu reynt að skrifa slóðina handvirkt í vafrann [31, Conversation].
*   **Jinja2**: Í HTML sniðmátum geturðu notað hlutverkið til að sýna eða fela hluti:
    ```html
    {% if session.role == 'admin' %}
        <a href="/admin_panel">Stjórnborð</a>
    {% endif %}
    ```

Hönnunin á **`admin_panel.html`** byggir á því að sýna yfirlit yfir alla notendur kerfisins og bjóða upp á aðgerðir til að stýra þeim. Síðan nýtir erfðir frá `layout.html` til að viðhalda samræmdu útliti og fær gögnin send sem lista af orðasöfnum (dictionaries) frá Flask bakendanum [44, 45, Conversation].

Hér er uppsetning stjórnborðsíðunnar:

### 1. Grunnur og tafla
Best er að nota töflu (table) til að sýna notendagögnin á skipulegan hátt. Við ítrum í gegnum `users` listann sem TinyDB skilar [6, 25, Conversation].

```html
{% extends "layout.html" %}

{% block title %}Stjórnborð{% endblock %}

{% block content %}
    <h1>Stjórnun notenda</h1>

    <table class="admin-table">
        <thead>
            <tr>
                <th>Notendanafn</th>
                <th>Hlutverk</th>
                <th>Aðgerðir</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
                <tr>
                    <td>{{ user.username }}</td>
                    <td>
                        <span class="role-tag {{ user.role }}">
                            {{ user.role }}
                        </span>
                    </td>
                    <td>
                        {# Aðgerð 1: Breyta hlutverki #}
                        {% if user.role != 'admin' %}
                            <a href="{{ url_for('make_admin', user_id=user.doc_id) }}" class="btn-small">Gera að admin</a>
                        {% endif %}

                        {# Aðgerð 2: Eyða notanda (Conversation) #}
                        <a href="{{ url_for('delete_user', user_id=user.doc_id) }}" 
                           class="btn-danger" 
                           onclick="return confirm('Ertu viss um að þú viljir eyða þessum notanda?')">
                           Eyða
                        </a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

### 2. Lykilatriði í hönnuninni
*   **Aðgangur að gögnum**: Inni í lykkjunni nálgast þú gildi eins og `user.username` og `user.role` með punkt-málfræði Jinja2, sem svarar til lykla í Python orðasafni.
*   **doc_id**: Við notum `user.doc_id` (sjálfgefið auðkenni í TinyDB) í `url_for` til að vita nákvæmlega hvaða notanda við ætlum að eyða eða uppfæra [6, 39, Conversation].
*   **Skilyrt birting**: Með því að nota `{% if user.role != 'admin' %}` tryggjum við að við séum ekki að bjóða upp á að gera einhvern að admin sem er það þegar.


**Samantekt:** `admin_panel.html` er öflugt tæki þar sem þú notar **Jinja2 lykkjur** til að lesa úr **TinyDB** og **URL building** til að framkvæma CRUD aðgerðir á notendagrunninum.

---

### Uppfærsla eigin pósta

Til þess að notandi geti breytt eigin póstum þarftu að nýta **`update()`** aðferðina í TinyDB og búa til nýja rás (route) í Flask sem birtir breytingarform og vistar nýja textann. Ferlið krefst þess að við staðfestum að sá sem reynir að breyta sé örugglega höfundur póstsins með því að bera saman `user_id` úr session við `author_id` póstsins.

Hér er hvernig þú bætir þessari virkni við:

### 1. Flask rásin: `edit_post` í `app.py`
Þessi rás þarf að styðja bæði `GET` (til að sýna formið með gamla textanum) og `POST` (til að vista breytingarnar).

```python
@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    # 1. Athugum hvort notandi sé innskráður
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # 2. Sækjum póstinn úr TinyDB með doc_id
    post = posts_table.get(doc_id=post_id)

    # 3. Öryggisathugun: Má notandinn breyta þessum pósti?
    if not post or post['author_id'] != session['user_id']:
        flash("Þú getur aðeins breytt þínum eigin póstum!")
        return redirect(url_for('profile'))

    if request.method == 'POST':
        # 4. Sækjum nýja textann úr forminu
        new_content = request.form.get('content')
        
        # 5. Uppfærum póstinn í gagnagrunninum
        posts_table.update({'content': new_content}, doc_ids=[post_id])
        
        flash("Pósti hefur verið breytt!")
        return redirect(url_for('profile'))

    # Ef GET: Sýnum síðu með formi og gamla textanum
    return render_template('edit_post.html', post=post)
```

### 2. Uppfæra `profile.html`
Bættu við hlekk við hvern póst í listanum þínum svo notandinn geti smellt á „Breyta“. Notaðu **`url_for`** til að búa til slóðina með réttu `post_id`.

```html
{# Inni í for-lykkjunni í profile.html #}
{% for post in posts %}
    <div class="post">
        <p>{{ post.content }}</p>
        <small>{{ post.timestamp }}</small> | 
        
        {# Hlekkur á breytingasíðuna #}
        <a href="{{ url_for('edit_post', post_id=post.id) }}">Breyta pósti</a> |
        
        <a href="{{ url_for('delete_post', post_id=post.id) }}" 
           onclick="return confirm('Ertu viss?')">Eyða</a>
    </div>
{% endfor %}
```

### 3. Nýtt sniðmát: `templates/edit_post.html`
Þetta skjal birtir form þar sem gamli textinn er þegar inni í `textarea` svo notandinn geti lagfært hann.

```html
{% extends "layout.html" %}

{% block title %}Breyta pósti{% endblock %}

{% block content %}
    <h1>Breyta pósti</h1>
    
    <form method="POST">
        <label for="content">Innihald:</label><br>
        {# Birtum gamla textann inni í textarea #}
        <textarea name="content" rows="5" cols="40" required>{{ post.content }}</textarea><br>
        
        <button type="submit">Vista breytingar</button>
        <a href="{{ url_for('profile') }}">Hætta við</a>
    </form>
{% endblock %}
```

### Lykilatriði:
*   **Update í TinyDB**: Við notum `db.update(fields, query)` eða `doc_ids` til að breyta aðeins ákveðnum reitum í skjalinu án þess að eyða því.
*   **doc_id**: Þegar við birtum póstana á prófílsíðunni verðum við að muna að geyma `doc_id` (t.d. sem `post.id`) svo rásin viti hvaða póst á að uppfæra.
*   **Aðgangsstýring**: Það er mikilvægt að athuga `author_id` á bakendanum (Python) en ekki bara fela hlekkinn í HTML, því annars gæti einhver breytt póstum annarra með því að giska á `post_id` í vefslóðinni.
*   **Sjálfvirk hreinsun**: Jinja2 sér um að **hreinsa (escape)** textann sjálfkrafa þegar hann er birtur í forminu, sem verndar gegn öryggisvandanum.

---

### Gagnagrunnurinn db.json

Hér er dæmi um hvernig **`db.json`** skráin þín á að líta út til að passa við appið sem við höfum verið að smíða. TinyDB geymir gögnin í flokkuðum töflum þar sem hver færsla fær sjálfvirkt númer (ID) sem lykil [5, 6, Conversation].

```json
{
    "users": {
        "1": {
            "username": "admin",
            "password": "lykill_123",
            "role": "admin"
        },
        "2": {
            "username": "jon_jonsson",
            "password": "psw456",
            "role": "user"
        }
    },
    "posts": {
        "1": {
            "content": "Hæ öll! Þetta er fyrsti pósturinn minn á nýja spjallinu.",
            "author_id": 1,
            "timestamp": "06/18, 2026 10:30"
        },
        "2": {
            "content": "Mér finnst Epguides API-ið virka mjög vel með Flask.",
            "author_id": 2,
            "timestamp": "06/18, 2026 11:45"
        }
    },
    "favorites": {
        "1": {
            "user_id": 2,
            "show_id": "the-flash",
            "title": "The Flash",
            "image": "https://static.tvmaze.com/uploads/images/medium_portrait/448/1121792.jpg"
        }
    }
}
```

### Útskýring á uppbyggingunni:

1.  **`users` taflan:** Hér eru notendurnir geymdir. Lykillinn `"1"` eða `"2"` er það sem við köllum **doc_id**. Við höfum bætt við `role` lyklinum til að stýra aðgangi að stjórnborðinu (admin panel) eins og við ræddum áðan [Conversation].
2.  **`posts` taflan:** Hver póstur hefur `content`, `timestamp` (tímastimpil) og `author_id`. **`author_id`** verður að passa við lykilinn í `users` töflunni (t.d. póstur 1 er eftir notanda 1) svo appið geti flett upp réttu nafni á forsíðunni [6, Conversation].
3.  **`favorites` taflan:** Hér geymum við þætti sem notendur hafa valið úr Epguides API. Við vistar titilinn og myndaslóðina frá **TVMaze** beint í skrána svo við þurfum ekki að kalla aftur í API-ið þegar notandinn skoðar prófílinn sinn [3, 20, Conversation].

**Athugið:** Ef þú ert að byrja með tóman gagnagrunn mun TinyDB búa þessa skrá til sjálfkrafa þegar þú notar `insert()` í fyrsta skipti í Python.

**Mikilvægt:** Vistaðu JSON skrána með **UTF-8** kóðun til að íslenskir stafir eins og „þ“ og „ð“ birtist rétt [Conversation].
