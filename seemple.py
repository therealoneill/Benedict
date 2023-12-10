import pandas as pd
import xml.etree.ElementTree as et

def parse_tole(root):
	attr = root.attrib

	for x in root.findall('scenario'):
		tole_info = attr.copy()
		tole_info.update(x.attrib)
		tole_info['text'] = x.find('text').text

		scenrioReplays = x.findall('scenarioReplay')
		for scenarioReplay in scenrioReplays:
			tole_info.update(scenarioReplay.attrib)

		yield tole_info

etree = et.parse('scendata.xml')
eroot = etree.getroot()
tole_data = parse_tole(eroot)
data = list(tole_data)
print(data)