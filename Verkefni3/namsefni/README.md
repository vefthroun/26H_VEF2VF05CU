## JSON málskipan

[JSON](https://realpython.com/python-json/) er vinsælt opið gagnaskiptasnið. Uppbygging samanstendur af eigindi (key) og gildi (value) pörum. 

 * {}, slaufusvigi eru utan um JSON hlut {object} og innri hluti
 * key verður að vera með **tvöföldum gæsalöppum** og er strengur
 * key aðgreinist frá value með tvípunkti **:**
 * key/value parasambönd eru aðgreind með kommu
 * Ekki hægt að commenta í JSON skrá
 * JSON skráarsnið er með .json endingu

```json

{
	"aðgangslykill": [
			{
			"key1": "value1",
			"key2": "value2"
		}, {
			"key1": "value3",
			"key2": "value4"
		}
	]
}
```

JSON er notað með ýmsum forritunarmálum og þú getur notað JSONLint til að validate JSON. http://jsonlint.com/ 

- [JSON kóðadæmi](JSON/README.md)
- [JSON & Python CRUD dæmi](namsefni/pyCrudExamples/README.md)

---


