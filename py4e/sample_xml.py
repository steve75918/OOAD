import xml.etree.ElementTree as ET

# sample data 1
data1 = '''
    <person>
        <name>Chuck</name>
        <phone>+1 734 303 4456</phone>
        <email hide="yes" />
    </person>
'''

# prase by ET
tree = ET.fromstring(data1)

print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

print('-----------------------------------------')

# sample data 2
data2 = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>
'''

stuff = ET.fromstring(data2)
user_list = stuff.findall('users/user')

print('User count:', len(user_list))
for user in user_list:
    print('Name', user.find('name').text)
    print('Id', user.find('id').text)
    print('Attribute', user.get('x'))