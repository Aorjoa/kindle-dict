import xml.etree.ElementTree as ET
import io
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("etlex.xml", parser=parser )
root = tree.getroot()

f = io.open('dict.txt','w', encoding='utf8')
def writeFile(strParam):
    f.write(unicode(strParam))
oldWord = ""
for doc in root.findall("Doc"):
    try:
        word = doc.find("esearch").text
        if oldWord != word:
            writeFile("\r\n" + word + "\t")
            oldWord = word
        writeFile("(" + doc.find("ecat").text + ") " + doc.find("tentry").text + "<br>") 
        entryThai = doc.find("ethai").text
        writeFile("<b><i>" + entryThai + "</i></b><br>")
        syn = doc.find("esyn").text
        if(syn):
            writeFile("Syn : " + syn + "<br>")
    except AttributeError:
        pass
    
f.close()
print("SUCCESS")