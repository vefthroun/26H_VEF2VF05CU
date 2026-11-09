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


- Textinn er auðskiljanlegur fyrir fólk og auðvelt er fyrir tölvukerfi að vinna úr honum og þýða yfir í forritunarmál. [1](https://www.opc-router.com/what-is-json/), [2](https://da.wikipedia.org/wiki/JSON)
- Þótt nafnið  (JavaScript Object Notation) innihaldi JavaScript er hægt að nota JSON í nánast öllum helstu forritunarmálum (t.d. Python, C++, Java, PHP). [1] (https://www.youtube.com/watch?v=KdweixONFyA), [2] (https://www.youtube.com/watch?v=cj3h3Fb10QY), [3] (https://da.wikipedia.org/wiki/JSON)

#### Algeng notkun

- Vefþjónustur (APIs): Samskipti á milli vefþjóna ogvafra eða smáforrita (apps).
- Gagnagrunnar: NoSQL gagnagrunnar (e.g. MongoDB) nota JSON eða svipuð snið beint til að geyma gögn.
- Stillingarskrá (Configuration files): Forrit nota JSON oft til að geyma stillingar eða valkosti. [1](https://www.oracle.com/database/what-is-json/). 


