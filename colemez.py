import pandas as pd
import xml.etree.ElementTree as et

def transform_xml(xml_doc):
	attr = xml_doc.attrib
	for xml in xml_doc.iter('scenario'):
		dict = attr.copy()
		dict.update(xml.attrib)

		yield dict


# Load xml into parser
etree = et.parse('scendata.xml')
# Get the root
eroot = etree.getroot()

# Will print all attributes in the scenario brackets
#print(eroot.attrib)

# Will print scenario (just the name)
#print(eroot.tag)

# Will print nothing as it has no text
#print(eroot.text)

#Call function
trans = transform_xml(eroot)
#Need to convert the generator
#print(trans)
#convert into a list and print
#print(list(trans))

#Convert into a dataframe
tr_df = pd.DataFrame(list(trans))
print(tr_df.head())
print(tr_df.shape)