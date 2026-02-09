# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#

import xml.dom.minidom as md


# use the parse() function to load and parse an XML file
doc = md.parse('samplexml.xml')

# print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName)

# get a list of XML tags from the document and print each one
skills = doc.getElementsByTagName('skill')
print('Skill count:', skills.length)

for s in skills:
  print(s.getAttribute('name'))
    
# create a new XML tag and add it into the document
newskill = doc.createElement('skill')
newskill.setAttribute('name', 'AWS')
doc.firstChild.appendChild(newskill)

skills = doc.getElementsByTagName('skill')
print('Skill count:', skills.length)

for s in skills:
  print(s.getAttribute('name'))