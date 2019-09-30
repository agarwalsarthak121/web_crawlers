import xml.etree.ElementTree as et

#Read from file A
treeA = et.ElementTree(file='A.xml')
rootA = treeA.getroot()

#Extract Element list that we need to copy
elemA = rootA.find('results').find('result').findall('result_data')

#Get the Element in B where we need to insert the elements
treeB = et.ElementTree(file='B.xml')
rootB = treeB.getroot()
elemB = rootB.find('results').find('result')

#Insert the elements in B
for e in elemA:
    elemB.append(e)

#Create a tree C 
treeC = et.ElementTree(rootB)

#Write all the content to a file C.xml
with open("C.xml", "wb") as fh:
    tree3.write(fh)
