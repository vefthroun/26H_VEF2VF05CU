## JSON

[JSON](https://realpython.com/python-json/) er vinsælt opið gagnaskiptasnið. Uppbygging samanstendur af eigindi (key) og gildi (value) pörum. JSON er notað með ýmsum forritunarmálum. 

<details>
<summary>JSON málskipan</summary>
<br>
  
 * key/value parasamband
 * {}, slaufusvigi eru utan um JSON object og innri objecta
 * key verður að vera með **tvöföldum gæsalöppum** og vera strengur
 * key/value parasambönd eru aðgreind með kommu
 * Ekki hægt að commenta í JSON skrá
 * JSON skráarsnið er með .json endingu
 * Þú getur notað JSONLint til að validate JSON. http://jsonlint.com/ 

</details>

<details>
<summary> Kóðadæmi</summary>
<br>

1. [JSON sýnidæmi](JSON/2_JSON_EXAMPLES.json)
1. [JSON í Dictionary](JSON/3_JsonToDictionary.py)
1. [Dictionary í JSON](JSON/4_dictionaryToJson.py)
1. [Að lesa úr JSON skrá](JSON/5_lesa_skra.py)
1. [Að skrifa í skrá](JSON/6_skrifaSkra.py)
1. [Að skrifa í JSON skrá](JSON/6_skrifa_Json_skra.py)
1. [Að lesa úr JSON skrá hýst á Github (https) með urllib](JSON/7_urllib_request.py)
1. [Að sækja JSON frá API](JSON/API.py) 

<!-- 
1. Flask: [Að skila JSON](JSON/Flask_return_JSON.py)
1. Flask: [Að skila JSON með Jsonify](JSON/jsonify.py)
1. [Að vinna úr dictionary sem kemur frá API](JSON/8_dictionary_API.py)
-->

</details>

<details>
<summary>Bjargir</summary>

* [CRUD aðgerðir með dictionary](https://www.freecodecamp.org/news/everything-you-need-to-know-about-python-dictionaries/)
* [CRUD aðgerðir með JSON skrá](https://tecadmin.net/crud-operations-on-json-files-with-python/#google_vignette)
* [JSON Support in Flask](https://tedboy.github.io/flask/interface_api.json_support.html#module-flask.json)
* [Python's urllib.request for HTTP Requests](https://realpython.com/urllib-request/)
* [Working with JSON data](https://www.youtube.com/watch?v=9N6a-VLBa2I) _(YouTube)_
* [Append to JSON file using Python](https://www.geeksforgeeks.org/append-to-json-file-using-python/)
* [CRUD aðgerðir með Flask og JSON](https://github.com/oritzio/flask_crud_json)
* [REST API CRUD operations, beginners guide](https://medium.com/@mathur.danduprolu/building-restful-apis-with-flask-a-beginners-guide-to-crud-operations-part-2-7-4ff74083a3ee)
* [Fixing the SSL CERTIFICATE_VERIFY_FAILED Error](https://realpython.com/urllib-request/#fixing-the-ssl-certificate_verify_failed-error), hér er dæmi um [kóðalausn](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni4/JSON/certifi_fix.PNG)
<!-- 
og [Certify](https://certifi.io/)
-->

</details>


---

### API
[API](https://www.youtube.com/watch?v=s7wmiS2mSXY) (application programming interface) stendur fyrir forritunarviðmót. API er notað til að sækja gögn á milli kerfa, [nánar um API](https://zapier.com/learn/apis/chapter-1-introduction-to-apis/). Hér [Postman VSCode viðbót](JSON/VSC_Postman/README.md) til að prófa að gera API fyrirspurnir.

<!--
> [xmltodict 0.13.0](https://pypi.org/project/xmltodict/) _Makes working with XML feel like you are working with JSON_
-->

<details>
<summary>Að búa til sinn eigin REST API <em>(ítarefni)</em></summary>
<br>
  
One of the most popular ways to build APIs is the REST architecture style. Python provides some great tools not only to get data from REST APIs but also to build your own Python REST APIs.
- [Python and REST APIs: Interacting With Web Services](https://realpython.com/api-integration-in-python/)
- [Creating Web APIs with Python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)
- [REST API using Flask in 7 minutes](https://towardsdatascience.com/launch-your-own-rest-api-using-flask-python-in-7-minutes-c4373eb34239) 

</details>


---


### Dagsetningar 

`'timestampApis': '2021-02-04T22:50:15.468'  # Timestamp format: yy-MM-dd HH:mm:ss,SSS`

Dæmi um lausn 
1. get date (string) from JSON data (Api)
2. String to Datetime Object with datetime.strptime()
3. Convert Python Datetime to a String, datetime_string = datetime_object.strftime(format_string)

_Það væri einnig hægt að nota strengjavinnslu og regex til að fá íslenska dagsetningu_

<details>
<summary>Bjargir</summary>
<br>

- [Datetime timestamp](https://www.programiz.com/python-programming/datetime/timestamp-datetime)
- [How to properly use datetime in your Python code](https://medium.com/better-programming/demystifying-python-datetime-module-with-examples-352e6cc72efc)
- [Python Datetime Tutorial: Manipulate Times, Dates, and Time Spans](https://www.dataquest.io/blog/python-datetime-tutorial/)

</details>
