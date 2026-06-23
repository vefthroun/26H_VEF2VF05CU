# TinyDB 

Ef þú þarft einfaldan API gagnagrunn sem virkar án mikillar fyrirhafnar þá gæti TinyDB verið rétti kosturinn fyrir þig.

* https://tinydb.readthedocs.io/en/latest/
* https://www.tutorialspoint.com/tinydb/index.htm

---

Til að búa til þessa spjallsíðu þurfum við að tengja saman **Flask** fyrir vefumgjörðina, **sessions** fyrir örugga aðgangsstýringu og **TinyDB** sem JSON gagnagrunn.

### Bakendinn: `app.py`

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

# --- DATABASE --- leiðin að db.json fundinn
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, 'data'))
# Ensure DB folder exists & instantiate
os.makedirs(DB_PATH, exist_ok=True) 

POSTDB_FILE = os.path.join(DB_PATH, 'db.json')

# indent tvö bil og hvert par fær sér línu. íslenskir stafir notaðir og ascii afþakkað
db = TinyDB(POSTDB_FILE, indent=2, encoding='utf-8', ensure_ascii=False)

# --- AÐGANGSTÝRING db ---
users_table = db.table('users')
posts_table = db.table('posts')
User = Query()
Post = Query()

# --- HJÁLPARFÖLL ---
def get_posts_with_users():
    all_posts = posts_table.all()
    for post in all_posts:
        # Nota author_id til að finna notanda 
        user = users_table.get(doc_id=post['author_id'])
        post['username'] = user['username'] if user else "Óþekktur"
        post['id'] = post.doc_id # Ná í doc_id fyrir eyðingu/uppfærslu
    return all_posts

```

### Uppsetning Gagnagrunns
TinyDB geymir gögn sem Python orðasöfn (dicts) í JSON skrá. [Sjá nánari skýringu neðst á síðunni](https://github.com/vefthroun/26H_VEF2VF05CU/blob/main/Verkefni3/namsefni/Tinydb/README.md#gagnagrunnurinn-dbjson)

### Forsíða með póstum, innskráning, nýskráning og prófílsíða með CRUD virkni

Ferlið við að smíða vefkerfi sem styður nýskráningu, innskráningu og CRUD aðgerðir (Create, Read, Update, Delete) fyrir spjallpósta með **TinyDB** sem gagnagrunn.

### Forsíða: Lesa gögn (Read on Index)

Á forsíðunni viljum við birta alla pósta ásamt upplýsingum um höfund og tímasetningu 

1. Sækjum alla pósta með `posts_table.all()`.
2. Fyrir hvern póst flettum við upp höfundi í `users_table` með því að nota `author_id` póstsins
3. Sendum listann á `index.html` með `render_template()`.

```python
# --- RÁSIR (ROUTES) ---

@app.route('/')
def index():
    posts = get_posts_with_users()
    return render_template('index.html', posts=posts)

```

### Session innskráning og útskráning

1. Leita að notanda með `Query()` þar sem notandanafn passar.
2. Ef notandi finnst, vistum við `user_id` hans í `session['user_id']` Við notum **Flask session** til að muna eftir innskráðum notendum.
3. **login.html:** þarf að innihalda form með `method="POST"` sem sendir gögnin á viðeigandi rás.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users_table.get((User.username == username) & (User.password == password))
        
        if user:
            session['user_id'] = user.doc_id # Vista ID í session
            session['username'] = user['username']
            
            # Skilyrði fyrir administrator með role: úr db
            if username == 'admin':
                session['role'] = 'admin'
            else:
                session['role'] = user.get('role', 'user')
            return redirect(url_for('profile'))
        
        flash("Rangt notandanafn eða lykilorð.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```
Til að kerfið virki þarf nýr notandi að geta búið til aðgang og skráð sig síðan inn. 

### Nýskráning (`/signup`) 
Gögnum er safnað úr formi og vistuð í `users` töfluna með `insert()`.
1. Sækja `username` og `password` úr `request.form`.
2. Vista í TinyDB. `insert()` skilar sjálfkrafa einstöku ID (doc_id).

```python
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
```

### Prófílsíða og aðgangsstýring

Prófílsíðan sýnir aðeins þá pósta sem tilheyra innskráðum notanda.

1. Athugum hvort `user_id` sé í `session`.
2. Notum `posts_table.search(Query().author_id == session['user_id'])` til að sía gögnin

```python
@app.route('/profile')
def profile():
    if 'user_id' not in session: 
        return redirect(url_for('login'))
    # Sækja aðeins pósta þessa notanda 
    my_posts = posts_table.search(Post.author_id == session['user_id'])
    for p in my_posts: p['id'] = p.doc_id
    return render_template('profile.html', posts=my_posts)
```

### Stjórnun pósta (Create, Update, Delete)


> **Athugið:** Allar skrár (`.py`, `.html`, `.json`) skulu vistaðar með **UTF-8** kóðun til að tryggja að íslenskir sérstafir skili sér rétt frá bakenda yfir í Jinja sniðmát.

### Búa til póst (Create)
Notandi skrifar texta í form. Við bætum við `author_id` úr session og tímastimpli áður en við vistum.

```python
@app.route('/create_post', methods=['POST'])
def create_post():
    if 'user_id' in session:
        content = request.form.get('content')
        posts_table.insert({
            'content': content,
            'author_id': session['user_id'],
            'timestamp': datetime.now().strftime("%d. %m. %Y. Kl. %H:%M") # Íslensk dagsetning skráð í db
        })
    return redirect(url_for('profile'))
```

### Uppfæra póst (Update)
Til að breyta pósti notum við `update()` aðferðina þar sem við skilgreinum nýju gögnin og hvaða póst á að uppfæra.

```python
# Uppfærsla pósta
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

### Eyða pósti (Delete)
Til að eyða notum við `remove()`. Gættu þess að notandi geti aðeins eytt sínum eigin póstum (nema hann sé með **admin** hlutverk).
```python
@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    post = posts_table.get(doc_id=post_id)
    if post and post['author_id'] == session.get('user_id'):
        posts_table.remove(doc_ids=[post_id])
        flash("Pósti eytt.")
    return redirect(url_for('profile'))
```

---

### Sniðmát (Templates)

#### `templates/layout.html`

1. Skipulagssíðan sem allar grunnsíður "_templates_" erfa `{% extends "layout.html" %}`. 
1.  **UTF-8**: Meta-tagið í `layout.html` kemur í veg fyrir skrípi-stafi eins og „Ã¦“ .

```html
<!DOCTYPE html>
<html lang="is">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="TinyDB og Json">
    <meta name="author" content="Guðmundur Jón Guðjónsson">
    <title> {% block title %}. 
                Verkefni 3. TinyDB & JSON 
            {% endblock %}
    </title>
    <link rel="stylesheet" href="{{url_for('static', filename='pico.indigo.min.css')}}">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <link rel="icon" type="image/svg" href="/static/images/Glogo.svg">
</head>
<body>
    <nav class="container">
        <ul>
            <li><h5><a href="{{ url_for('index') }}">Klúbburinn</a></h5></li>
        </ul>
        <ul>
        {% if session.user_id %}
            <li><a href="{{ url_for('profile') }}">Mín síða ({{ session.username }})</a></li>
            <li><a href="{{ url_for('logout') }}">Útskrá</a></li>
        {% else %}
            <li><a href="{{ url_for('login') }}">Innskrá</a></li>
            <li><a href="{{ url_for('signup') }}">Nýskrá</a></li>
        {% endif %}
        </ul>
    </nav>
    <main class="container">
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for msg in messages %}<p class="flashes">{{ msg }}</p>{% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>
    <footer class="container">
        <p class="center">&copy; Cat,  VEFÞ2VF, spönn 1, haust 2026.</p>
    </footer>
</body>
</html>
```

#### `templates/index.html`

1. Birtir alla pósta ú **db** með notendanafni og tímasetningu.
2.  **Tenging gagna**: Í `index()` rásinni flettum við upp notanda í hvert sinn sem póstur er birtur til að sýna nafn en ekki bara ID-tölu.
   
```html
{% extends "layout.html" %}
{% block title %}Skilaboðaskjóðan{% endblock %}
{% block content %}
    <h3>Nýjustu skilaboðin</h3>
    <div class="newpost">
    {% for post in posts %}
        <article>
            <p>{{ post.content }}</p>
            <small>Skrifað þann: {{ post.timestamp }}. Höfundur: {{ post.username }}</small>
        </article>
        <hr>
    {% endfor %}
    </div>
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

- Til að útfæra **`signup.html`** þarftu að búa til HTML-form sem sendir gögnin (notandanafn og lykilorð) á bakendann með `POST` aðferðinni. Sniðmátið á að nota Jinja2 erfðir til að fylgja útliti vefsins þíns og birta endurgjöf ef eitthvað fer úrskeiðis.
- Formið þarf að nota `method="POST"` til að flytja gögnin á öruggan hátt í `request.form` safnið í Flask. Við notum `url_for('signup')` í `action` eigindinu til að vísa á rétta rás í bakendanum.

####  `templates/signup.html`

```html
{% extends "layout.html" %}

{% block title %}Nýskráning{% endblock %}

{% block content %}
    <h2>Búa til nýjan aðgang</h2>
    <article>
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
	</article>
    <p>Áttu þegar aðgang? <a href="{{ url_for('login') }}">Innskráning hér</a></p>
{% endblock %}
```

### Mikilvæg atriði við útfærsluna:

*   **`name` eigindið**: Þetta er mikilvægasti hlutinn. Gildin í `name="username"` og `name="password"` verða að vera nákvæmlega þau sömu og þú notar í Python kóðanum þegar þú kallar í `request.form.get()`.
*   **Öryggi og endurgjöf**:
    *   Flask og Jinja2 sjá sjálfkrafa um að **hreinsa (escape)** gögnin sem notandinn slær inn til að verjast sprautuhótunum (injection attacks).
    *   Ef notandanafnið er þegar til í **TinyDB**, notum við `flash()` til að senda skilaboð. Gakktu úr skugga um að `layout.html` skjalið þitt sé með lykkju `get_flashed_messages()` til að birta skilaboðin.
*   **Vefslóðir**: Notaðu alltaf **`url_for()`** til að búa til tengingar á milli síðna (t.d. yfir á innskráningu). Það er öruggara en að harðkóða slóðir eins og `/login`.

#### `templates/profile.html`

- Hér getur notandi búið til nýjan póst og eytt sínum eigin.
- **profile.html** sýnir hvernig á að eyða (`remove`) og búa til (`insert`) gögn í TinyDB.
  
```html
{% extends "layout.html" %}
{% block content %}
    <h1>Velkomin(n), {{ session.username }}</h1>
    {% if session.role == 'admin' %}
        <form action="/admin_panel">
            <button>Stjórnborð</button>
        </form>
    {% endif %}
    <h3>Búa til nýjan póst</h3>
    <form action="{{ url_for('create_post') }}" method="POST">
        <textarea name="content" required></textarea>
        <button type="submit">Senda póst</button>
    </form>
    <hr>
    <h3>Mínir póstar</h3>
    {% for post in posts %}
        <article>
            <p>{{ post.content }}</p>
            <small>{{ post.timestamp }}</small> |

            {# Hlekkur á breytingasíðuna #}
            <a href="{{ url_for('edit_post', post_id=post.id) }}">Breyta pósti</a> |
        
            <a href="{{ url_for('delete_post', post_id=post.id) }}" 
                onclick="return confirm('Ertu alveg viss?')">Eyða pósti</a>
        </article>
    {% endfor %}
{% endblock %}
```

#### `templates/edit_post.html`
Þetta skjal birtir form þar sem upphaflegi textinn er þegar inni í `textarea` svo notandinn geti lagfært hann.

```html
{% extends "layout.html" %}

{% block title %}Breyta pósti{% endblock %}

{% block content %}
    <h1>Breyta pósti</h1>
    <article>
        <form method="POST">
            <label for="content">Innihald:</label><br>
            {# Birtum gamla textann inni í textarea #}
            <textarea name="content" rows="5" cols="40" required>{{ post.content }}</textarea><br>
            
            <button type="submit">Vista breytingar</button>
            <a href="{{ url_for('profile') }}">Hætta við</a>
        </form>
    </article>
{% endblock %}
```

### Lykilatriði:
*   **Update í TinyDB**: Við notum `db.update(fields, query)` eða `doc_ids` til að breyta aðeins ákveðnum reitum í skjalinu án þess að eyða því.
*   **doc_id**: Þegar við birtum póstana á prófílsíðunni verðum við að muna að geyma `doc_id` (t.d. sem `post.id`) svo rásin viti hvaða póst á að uppfæra.
*   **Aðgangsstýring**: Það er mikilvægt að athuga `author_id` á bakendanum (Python) en ekki bara fela hlekkinn í HTML, því annars gæti einhver breytt póstum annarra með því að giska á `post_id` í vefslóðinni.
*   **Sjálfvirk hreinsun**: Jinja2 sér um að **hreinsa (escape)** textann sjálfkrafa þegar hann er birtur í forminu, sem verndar gegn öryggisvandanum.

---

### Aðgangsstýring á stjórnborð

Vefstjóri er skráður í JSON gagnagrunnin með annað hlutverk en aðrir notendur `"role": "admin"`. Með `{% if session.role == 'admin' %}` skilyrðingu í **profil.html** þá tjékkar Jinja á því hvort 'admin' sé innskráður ef svo er þá hefur hann aðgang að stjórnborði vefstjóra með póst aðferð á `/admin_panel`. Til að vera 100% örugg þá athum við `session.get('role') != 'admin'`

```python
# stjórnborðið
@app.route('/admin_panel', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users_table.get((User.username == username) & (User.password == password))

    # 1. Öryggisathugun 
    if session.get('role') != 'admin':
        flash("Aðgangur ekki leyfilegur")
        return redirect(url_for('index'))

    # 2. Sækja og undirbúa notendur
    users = users_table.all()
    for u in users:
        u['id'] = u.doc_id

    # 3. Sækja og undirbúa alla pósta
    all_posts = posts_table.all()
    for p in all_posts:
        p['id'] = p.doc_id
        # Fletta upp höfundi til að sýna nafn en ekki bara ID [3]
        user = users_table.get(doc_id=p['author_id'])
        p['username'] = user['username'] if user else "Óþekktur"

    return render_template('admin_panel.html', users=users, all_posts=all_posts)

# Notandi fjarlægður
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    # 1. Öryggisathugun: Aðeins admin má eyða notendum
    if session.get('role') != 'admin':
        flash("Aðgangur bannaður: Þú verður að vera stjórnandi.")
        return redirect(url_for('index'))

    # 2. Öryggisathugun: Kom í veg fyrir að admin eyði sjálfum sér
    if user_id == session.get('user_id'):
        flash("Þú getur ekki eytt sjálfum þér á meðan þú ert innskráð(ur)!")
        return redirect(url_for('admin_panel'))

    # 3. Eyða notandanum úr TinyDB
    # Við notum doc_ids þar sem user_id kemur beint úr slóðinni [4, 5]
    users_table.remove(doc_ids=[user_id])
    
    # Valfrjálst: Hér mætti líka eyða öllum póstum sem tilheyrðu þessum notanda 
    # posts_table.remove(Query().author_id == user_id)

    # 4. Endurgjöf og flutningur aftur á stjórnborðið
    flash("Notanda hefur verið eytt.")
    return redirect(url_for('admin_panel'))

# eyða póst frá admin stjórnborði
@app.route('/delete_post_admin/<int:post_id>')
def delete_post_admin(post_id):
    # 1. Öryggisathugun fyrir admin 
    if session.get('role') != 'admin':
        flash("Þú hefur ekki leyfi til að eyða póstum annarra.")
        return redirect(url_for('index'))

    # 2. Eyðum póstinum úr posts töflunni [1]
    posts_table.remove(doc_ids=[post_id])
    
    flash("Pósti hefur verið eytt af stjórnanda.")
    return redirect(url_for('admin_panel'))
```

####  `templates/admin_panel.html`

Hönnunin á **`admin_panel.html`** byggir á því að sýna yfirlit yfir alla notendur kerfisins og bjóða upp á aðgerðir til að stýra þeim. <br>
Síðan nýtir erfðir frá `layout.html` til að viðhalda samræmdu útliti og fær gögnin send sem lista af orðasöfnum (dictionaries) frá Flask bakendanum.

### Notendastjórnun vefstjóra

Best er að nota töflu (table) til að sýna notendagögnin á skipulegan hátt. Við ítrum í gegnum `users` listann sem TinyDB skilar.

```html
{% extends "layout.html" %}

{% block title %}Stjórnborð - Umsjón{% endblock %}

{% block content %}
    <h3>Stjórnborð kerfisstjóra</h3>

    {# HLUTI 1: NOTENDASTJÓRNUN #}
    <section class="admin-section">
        <h2>Notendur</h2>
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
                        <td><span class="badge">{{ user.role }}</span></td>
                        <td>
                            {# Eyða notanda - notar doc_id úr bakenda [3, 4] #}
                            {% if user.username != session.username %}
                                <a href="{{ url_for('delete_user', user_id=user.id) }}" 
                                   class="btn-danger" 
                                   onclick="return confirm('Viltu örugglega eyða notandanum {{ user.username }}?')">
                                   Eyða notanda
                                </a>
                            {% else %}
                                <small>(Sjálfur þú)</small>
                            {% endif %}
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>
```

#### 2. Lykilatriði í hönnuninni

*   **Aðgangur að gögnum**: Inni í lykkjunni nálgast þú gildi eins og `user.username` og `user.role` með punkt-málfræði Jinja2, sem svarar til lykla í Python orðasafni.
*   **doc_id**: Við notum `user.doc_id` (sjálfgefið auðkenni í TinyDB) í `url_for` til að vita nákvæmlega hvaða notanda við ætlum að eyða eða uppfæra.
*   **Skilyrt birting**: Með því að nota `{% if user.role != 'admin' %}` tryggjum við að við séum ekki að bjóða upp á að gera einhvern að admin sem er það þegar.

### HLUTI 2: PÓSTSTJÓRNUN 

Vefstjóru hefur aðgang að öllum póstum og getur fjarlægt þá

```html

    <section class="admin-section">
        <h3>Allir póstar á spjallborði</h3>
        <table class="admin-table">
            <thead>
                <tr>
                    <th>Höfundur</th>
                    <th>Innihald</th>
                    <th>Tímasetning</th>
                    <th>Aðgerðir</th>
                </tr>
            </thead>
            <tbody>
                {% for post in all_posts %}
                    <tr>
                        <td><strong>{{ post.username }}</strong></td>
                        <td>{{ post.content | truncate(50) }}</td>
                        <td>{{ post.timestamp }}</td>
                        <td>
                            {# Eyða pósti - notar doc_id póstsins [3, 4] #}
                            <a href="{{ url_for('delete_post_admin', post_id=post.id) }}" 
                               class="btn-danger" 
                               onclick="return confirm('Eyða þessum pósti?')">
                               Eyða pósti
                            </a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>
{% endblock %}
```

**Samantekt:** `admin_panel.html` er öflugt tæki þar sem þú notar **Jinja2 lykkjur** til að lesa úr **TinyDB** og **URL building** til að framkvæma CRUD aðgerðir á notendagrunninum.

---

### Gagnagrunnurinn db.json

Hér er dæmi um hvernig **`db.json`** skráin þín á að líta út til að passa við appið sem við höfum verið að smíða. TinyDB geymir gögnin í flokkuðum töflum þar sem hver færsla fær sjálfvirkt númer (ID) sem lykil.

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

#### Útskýring á uppbyggingunni:

1.  **`users` taflan:** Hér eru notendurnir geymdir. Lykillinn `"1"` eða `"2"` er það sem við köllum **doc_id**. Við höfum bætt við `role` lyklinum til að stýra aðgangi að stjórnborðinu (admin panel) eins og við ræddum áðan.
2.  **`posts` taflan:** Hver póstur hefur `content`, `timestamp` (tímastimpil) og `author_id`. **`author_id`** verður að passa við lykilinn í `users` töflunni (t.d. póstur 1 er eftir notanda 1) svo appið geti flett upp réttu nafni á forsíðunni.
3.  **`favorites` taflan:** Hér geymum við þætti sem notendur hafa valið úr Epguides API. Við vistar titilinn og myndaslóðina frá **TVMaze** beint í skrána svo við þurfum ekki að kalla aftur í API-ið þegar notandinn skoðar prófílinn sinn.

**Athugið:** Ef þú ert að byrja með tóman gagnagrunn mun TinyDB búa þessa skrá til sjálfkrafa þegar þú notar `insert()` í fyrsta skipti í Python.

**Mikilvægt:** Vistaðu JSON skrána með **UTF-8** kóðun til að íslenskir stafir eins og „þ“ og „ð“ birtist rétt.
