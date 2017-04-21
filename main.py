

import re
from xmljson import gdata
from xml.etree.ElementTree import fromstring
from json import dump
from xml.dom import minidom

import xml.etree.ElementTree as ET

with open('sample.txt') as f:
	raw_contents = f.read()

	p = re.compile(r'string m_Script = "(.*)"$')
	m = p.match(raw_contents)
	raw_contents = m.group(0)

	raw_contents = re.sub(r'\\r\\n\s*', '', raw_contents)
	raw_contents = re.sub(r'\\n\s*', '', raw_contents)
	

	root = ET.fromstring(raw_contents)

	tree = ET.ElementTree(root)
	rough_string = ET.tostring(root, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	formatted = reparsed.toprettyxml(indent="\t")

	with open('test.xml', 'w') as outfile:
		outfile.write(formatted)

	raw_contents = raw_contents.replace(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="Items.xsd"', '', 1)
	contents = gdata.data(fromstring(raw_contents))

	with open('data.json', 'w') as outfile:
		dump(contents, outfile, indent=4)