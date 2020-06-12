from urllib.request import urlopen
from bs4 import BeautifulSoup
# Needs urllib.request, BeautifulSoup, lxml.

class WebParser():

    def getHtml(self, url):
        if str(type(url)) == "<class 'str'>":
            html = urlopen(url)
            bsObject = BeautifulSoup(html, "html.parser")
            return html, bsObject
        else:
            print("Error: Url Must be String!")
            pass
        pass

    def getItemByTag(self, bsObject, tagname):
        if str(type(tagname)) == "<class 'str'>":
            result = bsObject.find(tagname)
            return result
        else:
            print("Error: tagname Must be String!")
            pass
        pass

    def getItemsByTag(self, bsObject, tagname):
        if str(type(tagname)) == "<class 'str'>":
            result = bsObject.find_all(tagname)
            return result
        else:
            print("Error: tagname Must be String!")
            pass
        pass

    def getItemByClass(self, bsObject, objtype, classname):
        if str(type(classname)) == "<class 'str'>":
            result = bsObject.find(objtype, class_=classname)
            return result
        else:
            print("Error: classname Must be String!")
            pass
        pass

    def getItemsByClass(self, bsObject, objtype, classname):
        if str(type(classname)) == "<class 'str'>":
            result = bsObject.find_all(objtype, class_=classname)
            return result
        else:
            print("Error: classname Must be String!")
            pass
        pass

    def getItemById(self, bsObject, objtype, idname):
        if str(type(idname)) == "<class 'str'>":
            result = bsObject.find(objtype, id_=idname)
            return result
        else:
            print("Error: idname Must be String!")
            pass
        pass
    
    def getItemsById(self, bsObject, objtype, idname):
        if str(type(idname)) == "<class 'str'>":
            result = bsObject.find_all(objtype, id_=idname)
            return result
        else:
            print("Error: idname Must be String!")
            pass
        pass
    
    def getAttributes(self, bsObject, attributename):
        if str(type(attributename)) == "<class 'str'>":
            attribute = bsObject.get(attributename)
            return attribute
        else:
            print("Error: attributename Must be String!")
            pass
        pass
    pass

