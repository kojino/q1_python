API Services diagnostic quiz for Friday, October 14th:
:one: What is the `type` of each of the variables `body` and `content` in the following code snippet?
```http = httplib2.Http()
response, body = http.request(url, "GET")
content = json.loads(body)
```
content: dict
body: string

Now imagine you receive the following JSON document as `body`:
```{
    "firstName": "Grace",
    "lastName": "Hopper",
    "age": 107,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": 10021
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "212-555-1234"
        },
        {
            "type": "mobile",
            "number": "646-555-4567"
        }
    ]
}
```
:two: How would you access Grace Hopper’s postal code? (Write your response as a Python code snippet.)
try:
    content['address']['postalCode']
except KeyError as error:
    print error.message + "key not found"

:three: How would you access her mobile phone number? (Write your response as a Python code snippet.)

for number in content['phoneNumbers']:
    try:
        if number['type'] == 'mobile':
            print number['number']
    except KeyError as error:
        print error.message + "key not found"
