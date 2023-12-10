import xml.etree.ElementTree as ET
from benedict import benedict


# create a new empty instance
#d = benedict()

# or create from data source (filepath, url or data-string) in a supported format:
# Base64, CSV, JSON, TOML, XML, YAML, query-string
#d = benedict('weekly_etl.xml', format="xml")

#d = (benedict.from_xml('new.xml'))
#print(d.find(keys="genre"))

input = 'complex.xml'
tree = ET.parse(input)
print(tree)
root = tree.getroot()
print(root.tag)
#print(root[0][1].text)
#for child in root:
#	print(child[0].tag + ": " + child[0].text, flush=True)
for child in root[0]:
	print(child.tag)

