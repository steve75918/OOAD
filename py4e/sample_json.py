import json

# sample data 1
data1 = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

# prase by lib.json
tree = json.loads(data1)

print('Name:', tree["name"])
print('Email hide:', tree["email"]["hide"])

print('-----------------------------------------')

# sample data 2
data1 = '''[
    {
        "id":"001",
        "x":"2",
        "name":"Chuck"
    },
    {
        "id":"009",
        "x":"7",
        "name":"Chuck"
    }
]'''

# prase by lib.json
tree = json.loads(data1)

print('User counts:', len(tree))

for branch in tree:
    print('Name:', branch["name"])
    print('Id:', branch["id"])
    print('Attribute:', branch["x"])
