import json

data = {'name':'aryan','age':9,'meal':{'bf':'poha','lunch':'soya chunks'},'interest':['Pool','Sleeping',69]}
#json_data = json.dumps(data)
json_data = json.dumps(data,indent=4,sort_keys=True)
#print(json_data)

"""with open('data.json','w') as e:
    json.dump(data,indent=4,sort_keys=True)"""


load_data =  json.loads(json_data)
print(load_data)