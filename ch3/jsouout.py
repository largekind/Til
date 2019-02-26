import json,time

price = {
    "data": "1131-31-32",
    "price": {
        "Apple": 80,
        "Orange": 120,
        "Banana": 99
    }
}

s = json.dumps(price)
print(s)