import json
#testing converting from python list object to json format

locations = [
{'city':'Moscow', 'address':1111, 'email':'ema11', 'phone':'ph23'},
{'city':'Chelyabinsk', 'address':22, 'email':'ema11', 'phone':'ph23'},
{'city':'Chelyabinsk', 'address':22, 'email':'ema11', 'phone':'ph23'},
]

data = json.dumps(locations)
print(data)