import json
import msgpack
import os

#variant = 39

with open('products_39.json') as f:
    data = json.load(f)

    products = dict()

    for item in data:
        if item['name'] in products:
            products[item['name']].append(item['price'])
        else:
            products[item['name']] = list()
            products[item['name']].append(item['price'])

    result = list()

    for name, prices in products.items():
        sumPrice = 0
        maxPrice = prices[0]
        minPrice = prices[0]
        size = len(prices)
        for price in prices:
            sumPrice += price
            maxPrice = max(maxPrice, price)
            minPrice = min(minPrice, price)

        result.append({
            'name': name,
            'max': maxPrice,
            'min': minPrice,
            'avr': sumPrice / size
        })

    with open('products_result.json', 'w') as r_json:
        r_json.write(json.dumps(result))

    with open('products_result.msgpack', 'wb') as r_msgpack:
        r_msgpack.write(msgpack.dumps(result))

print(f"json    = {os.path.getsize('products_result.json')}")
print(f"msgpack = {os.path.getsize('products_result.msgpack')}")