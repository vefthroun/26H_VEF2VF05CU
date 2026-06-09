### Cookies
Cookies are stored on the client’s computer as text files. The aim is to remember and track data that is relevant to customer usage for better visitor experience and website statistics. Cookies also store the expiration time, path, and domain name of its website.

* cookie expires at the end of the browser session or as soon as the browser window is closed. 
* cookies are stored at client side and are not encrypted in any way. 
* Never store confidential information in cookies (XSS vulnerabilities).

1. [Flask cookies](https://flask.palletsprojects.com/en/3.0.x/quickstart/#cookies)
1. [Get and set cookies with Flask](https://pythonbasics.org/flask-cookies/) 
1. [Cookies kóðasýnidæmi frá kennara]()

---

### Sessions
Sessions in essence are used to remember information from one request to another when the user is navigating in your application. Sessions work by storing a cryptographically signed cookie on the users browser and decoding it on every request. 

1. [Flask sessions](https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions)
1. [Sessions in Flask](https://testdriven.io/blog/flask-sessions/)
1. [Session-based Authentication in flask](https://syscrews.medium.com/session-based-authentication-in-flask-d43fe36afc0f)
1. [Sessions authentication kóðasýnidæmi](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni3/Sessions/session_auth.py)

---

### Aðgangsstýring með Session

> Framhald af Form dæmi

Til að tryggja að aðeins skráðir nemendur hafi aðgang að `profile.html` þarf að nota **session** hlutinn í Flask til að geyma auðkenni notandans á milli beiðna. 

Hér er útfærslan skipt í bakenda (Python) og framenda (HTML).

### 1. Bakendinn: Flask og Session
Í Flask þarf fyrst að skilgreina `secret_key` svo hægt sé að nota session. Í rásinni (route) fyrir `/profile` er athugað hvort auðkenni notandans sé til staðar í session og hvort það auðkenni finnist í nemendalistanum þínum.

```python
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'Lykillinn_að_vefsíðunni' # Nauðsynlegt fyrir session

# Nemendalistinn (eins og í fyrra dæmi)
nemendur = {
    "1": {"nafn": "Jón Jónsson", "netfang": "jon@skoli.is"},
    "2": {"nafn": "Anna Önnu", "netfang": "anna@skoli.is"}
}

@app.route('/profile')
def profile():
    # 1. Athuga hvort notandi sé skráður inn í session
    user_id = session.get('user_id')
    
    # 2. Athuga hvort user_id sé í nemendalistanum
    if not user_id or user_id not in nemendur:
        # Ef ekki, senda notanda á forsíðu (aðgangur lokaður)
        return redirect(url_for('index'))
    
    # 3. Sækja gögn nemandans og birta síðuna
    nemandi = nemendur[user_id]
    return render_template('profile.html', nemandi=nemandi)

# Dæmi um hvernig notandi yrði "skráður inn" (t.d. eftir form)
@app.route('/login/<id>')
def login(id):
    if id in nemendur:
        session['user_id'] = id # Geymir ID í session hjá notanda
    return redirect(url_for('profile'))
```

### 2. Framendinn: templates/profile.html
Í HTML skránni færðu gögnin í gegnum `nemandi` breytuna sem var send með `render_template`. Jinja2 sér um að birta þau á öruggan hátt.

```html
<!DOCTYPE html>
<html lang="is">
<head>
    <meta charset="UTF-8">
    <title>Mínar síður</title>
</head>
<body>
    <h1>Velkomin(n) á þinn prófíl</h1>
    
    <div class="profile-card">
        <p><strong>Nafn:</strong> {{ nemandi.nafn }}</p>
        <p><strong>Netfang:</strong> {{ nemandi.netfang }}</p>
    </div>

    <hr>
    <p><a href="{{ url_for('index') }}">Aftur á forsíðu</a></p>
</body>
</html>
```

### Hvernig þetta virkar:
*   **Vörður við hliðið:** Þegar notandi reynir að skoða `/profile`, kíkir Flask í „vafrakökuna“ (session) hans. Ef þar finnst ekki gilt `user_id` sem passar við lykil í `nemendur` orðasafninu, hleypir kerfið honum ekki inn og sendir hann annað með `redirect`.
*   **Öryggi:** Þar sem Flask skrifar undir session-kökuna með leyndarlyklinum þínum (`secret_key`), getur notandinn séð ID-ið sitt en ekki breytt því í ID hjá öðrum nemanda án þess að kerfið taki eftir því.
*   **Aðgangsstýring:** Með því að nota `if user_id not in nemendur` er tryggt að jafnvel þó einhver sé með ID í session, þá verði það að vera til staðar í núverandi nemendalista til að síðan birtist.

---

### Innskráning

1. HTML Innskráningarform (templates/login.html)
Formið þarf að nota POST aðferðina svo gögnin sendist ekki í vefslóðinni og inntaksreitirnir þurfa að hafa name eigindi sem Flask notar til að bera kennsl á gögnin

```
<form method="POST">
    <label for="user_id">Sláðu inn nemenda-ID:</label>
    <input type="text" id="user_id" name="user_id" required>
    <button type="submit">Skrá inn</button>
</form>

<!-- Sýna villuskilaboð ef innskráning tekst ekki -->
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      <p style="color: red;">{{ message }}</p>
    {% endfor %}
  {% endif %}
{% endwith %}

```
---

### Útskráning

Að hanna útskráningarhnapp (logout) í Flask er tiltölulega einfalt ferli sem byggir á því að eyða auðkenni notandans úr **session** hlutnum. Þegar upplýsingarnar eru horfnar úr session, þekkir kerfið notandann ekki lengur sem innskráðan og vísar honum frá læstum síðum eins og `profile.html`.

Hér er hvernig þú útfærir þetta skref fyrir skref:

### 1. Bakendinn: Útskráningarrás (Route)
Þú þarft að búa til nýja rás í Python kóðanum þínum sem sér um að hreinsa session-ið. Best er að nota `.pop()` aðferðina á session orðasafnið til að fjarlægja `user_id`.

```python
from flask import session, redirect, url_for, flash

@app.route('/logout')
def logout():
    # Fjarlægir user_id úr session ef það er til staðar
    session.pop('user_id', None)
    
    # Gefa notanda endurgjöf
    flash('Þú hefur verið skráð(ur) út.')
    
    # Senda notanda aftur á forsíðu eða innskráningarsíðu
    return redirect(url_for('index'))
```

### 2. Framendinn: Hnappurinn í HTML
Þú getur sett útskráningarhnappinn hvar sem er í sniðmátunum þínum, til dæmis í `profile.html` eða í leiðsögustiku (navigation bar). Notaðu `url_for()` til að búa til rétta vefslóð á logout rásina.

**Dæmi í profile.html:**
```html
<p>Velkomin(n), {{ nemandi.nafn }}!</p>

<!-- Útskráningarhnappur sem lítur út eins og tengill -->
<a href="{{ url_for('logout') }}">Skrá út</a>

<!-- Eða sem raunverulegur hnappur inni í formi (öruggara fyrir ríkar aðgerðir) -->
<form action="{{ url_for('logout') }}">
    <button type="submit">Útskráning</button>
</form>
```

### 3. Hvernig þetta virkar saman
1.  **Notandi smellir:** Þegar smellt er á hnappinn kallar vafrinn á `/logout` vefslóðina.
2.  **Session hreinsað:** Flask keyrir `logout()` fallið og eyðir `user_id` úr vafraköku notandans.
3.  **Tilvísun:** Kerfið notar `redirect()` til að senda notandann á aðra síðu.
4.  **Aðgangur lokast:** Þar sem `user_id` er ekki lengur í session, mun `if not user_id` skilyrðið í `/profile` rásinni (sem við bjuggum til áðan) nú vísa notandanum frá ef hann reynir að fara þangað aftur.

**Góð ráð:**
*   **Feedback:** Notaðu `flash()` til að staðfesta útskráningu svo notandinn viti að aðgerðin tókst.
*   **Clear All:** Ef þú ert með margar breytur í session sem þú vilt hreinsa í einu, geturðu notað `session.clear()` í stað þess að nota `.pop()` fyrir hverja og eina.
