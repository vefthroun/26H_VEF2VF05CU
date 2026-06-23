# Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

| Method  |	Description |
| --- | --- |
| clear()	| Removes all the elements from the dictionary | 
| copy()	| Returns a copy of the dictionary | 
| fromkeys()	| Returns a dictionary with the specified keys and value | 
| get()	| Returns the value of the specified key | 
| items()	| Returns a list containing a tuple for each key value pair | 
| keys()	| Returns a list containing the dictionary's keys | 
| pop()	| Removes the element with the specified key | 
| popitem()	| Removes the last inserted key-value pair | 
| setdefault()	| Returns the value of the specified key. If the key does not exist: insert the key, with the specified value | 
| update()	| Updates the dictionary with the specified key-value pairs | 
| values()	| Returns a list of all the values in the dictionary | 

---

## Dagsetningar með timestamp

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