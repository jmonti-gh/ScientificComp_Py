''' XML (eXtended Markup Language) -Web Services: XML Schema 
Parsing XMLs. Reading its data - examples '''

# ISO 8601 Date/Time Format: 2023-01-29T09:45:59Z (UTC/GMT/Zulu)
# <xs:element name="start" type="xs.date"/>  -  <start>2023-01-29</start>
# <xs:element name="startdate" type="xs.dateTime"/>  - <startdate> ... </startdate>

# We talk XML inside Python w/'ElementTree'
import xml.etree.ElementTree as ET

# XML example that normally is gona come somwhere from the network
data = '''
<person>
    <name>Martha</name>
    <phone type="intl">+54 261 420 314</phone>
    <email hide="yes"/>
</person> '''

# diff text phone content with:
#   <phone type="intl">
#       +54 261 420 314
#   </phone>


print('\n~~~~~~~ XML case: Only one register ~~~~~~~')
# Parse the XML-string and obtain an object (kind of a tree version of the XML)
tree = ET.fromstring(data)
print('  ', tree, type(tree), '\n')
# We can query tree to pull data from it w/.find() method lool for a tag
# it finds everithing (tag, text, all), choose to see only the text
print('Name:', tree.find('name').text) 
print('Phone:', tree.find('phone').text) 
# To see child <email> attribute (can .get() any of the attributes)
print("email 'hide' attr.:", tree.find('email').get('hide'))
# Ther is only one 'text" but "attributes" several
print()

# Other example w/ more data
# xml.etree.ElementTree as ET, just imported above
inpxml = '''
<stuff>                        
    <users>
        <user x="2">
            <id>001</id>
            <name>Quique</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Pedro</name>
        </user>
         <user x="9">
            <id>052</id>
            <name>Guille</name>
        </user>
    </users>
</stuff> '''
# single tag in the outside <stuff>, complex type of users: 3 users objs. (a list)

print('\n~~~~~~~ XML case: more than one register ~~~~~~~')
elmstf = ET.fromstring(inpxml)       # ElementTree obj.
print('  ', elmstf, type(elmstf), '\n')
lst = elmstf.findall('users/user')
print('lst:', lst, type(lst), type(lst[0]))
print('Users count:', len(lst))
print()
print('{:^3}  {:^8}  {:^6}  {:^8}'.format('','--Name--', '--Id--', '--x attr--'))
cnt = 0
for it in lst:
    cnt += 1
    print('{:>3}   {:<8} {:>5}  {:>6}'.format(cnt, it.find('name').text,
     it.find('id').text, it.get('x')))
print()

