import pandas as pd
import xml.etree.ElementTree as et

# Load xml into parser
tree = et.parse('scendata.xml')
# Get the root
root = tree.getroot()
print(root)

#Initalize an empty list
data = []

#define a recursive function to parse the xml tree
def parse_element(element, item):
	if len(list(element)) == 0:
		item[element.tag] = element.text

	else:
		for child in list(element):
			parse_element(child, item)

# iterate through the xml tree and parse the elements

for child in root:
	item = {}
	parse_element(child, item)
	data.append(item)

#print(data)

df = pd.DataFrame(data)
#print(df)

output = 'elemesez.csv'
df.to_csv(output)