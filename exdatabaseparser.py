# NASA/IPAC Extragalatic Database Parser
# This package requires requests and beautifulsoup4

from webparser import WebParser

class ExDBManager():

    galaxyname = None
    url = None
    CrossIdent = []
    RA = None
    Dec = None
    RA_DEG = None
    Dec_DEG = None
    Z = [] # 값, 오차
    VHelio = [] #km/s
    VCMB = [] #km/s
    HubbleDistance = [] #Mpc
    ObjectType = None
    Morphoogy = None
    ActivityType = None
    OtherClassification = None
    Passband = None
    Diameter = None #kpc
    A_lambdaV = None
    A_lambdaK = None

    webParser = WebParser()
    html = None
    bsobj = None

    def __init__(self, galaxyname):
        self.galaxyname = galaxyname
        self.url = "https://ned.ipac.caltech.edu/byname?objname=" + str(galaxyname)
        self.html, self.bsobj = self.webParser.getHtml(self.url)
        self.getData()
        pass

    def printData(self):
        print('<Information Table Of ' + self.galaxyname + '>')
        print('--------------------------')
        print('SUCCESSFUL GET: ' + self.url)
        print('--------------------------')
        print('[Cross-Identifications]')
        for item in self.CrossIdent:
            print('- ' + item)
        print('')
        print('[Coordinates for Preferred Position]')
        print('> Equatorial (J2000)')
        print('RA: ' + self.RA)
        print('Dec: ' + self.Dec)
        print('RA(in Deg): ' + self.RA_DEG)
        print('Dec(in Deg): ' + self.Dec_DEG)
        print('')
        print('[Preferred Redshift & Derived Quantities] - H0 = 67.8 km/s/Mpc')
        print('z: ' + self.Z[0] + ' +/- ' + self.Z[1])
        print('V(Helio, km/s): ' + self.VHelio[0] + ' +/- ' + self.VHelio[1])
        print('V(CMB, km/s): ' + self.VCMB[0] + ' +/- ' + self.VCMB[1])
        print('')
        print('[Classifications]')
        print('Object Type: ' + self.ObjectType)
        print('Morphology: ' + self.Morphoogy)
        print('Other: ' + self.OtherClassification)
        print('')
        print('[Angular & Physical Diameters]')
        print('Passband: ' + self.Passband)
        print('Diameter(kpc): ' + self.Diameter)
        print('')
        print('[Foreground Galatic Extinction]')
        print('A_lambda [mag] V: ' + self.A_lambdaV)
        print('A_lambda [mag] K: '+ self.A_lambdaK)
        pass

    def returnDataList(self):
        return [self.CrossIdent, self.RA, self.Dec, self.RA_DEG, self.Dec_DEG,
        self.Z, self.VHelio, self.VCMB, self.HubbleDistance, self.ObjectType,
        self.Morphoogy, self.ActivityType, self.Passband, self.Diameter, self.A_lambdaV,
        self.A_lambdaK]

    def getData(self):
        tr = self.webParser.getItemByClass(self.bsobj, 'tr', 'ov_insiderow ov_inside_crosid_row')
        obj = self.webParser.getItemsByTag(tr, 'span')
        for item in obj:
            self.CrossIdent.append(item.text.strip())
            pass
        
        tr = self.webParser.getItemByClass(self.bsobj, 'tr', 'ov_insiderow ov_inside_coord_row')
        obj = self.webParser.getItemsByTag(tr, 'td')
        
        span = self.webParser.getItemsByTag(obj[0], 'span')
        if str(type(span[0])) == "<class 'bs4.element.Tag'>":
            self.RA = span[0].text.strip()
            pass
        if str(type(span[1])) == "<class 'bs4.element.Tag'>":
            self.Dec = span[1].text.strip()
            pass
        
        span = self.webParser.getItemsByTag(obj[1], 'span')
        if str(type(span[0])) == "<class 'bs4.element.Tag'>":
            self.RA_DEG = span[0].text.strip()
            pass
        if str(type(span[1])) == "<class 'bs4.element.Tag'>":
            self.Dec_DEG = span[1].text.strip()
            pass

        tr = self.webParser.getItemByClass(self.bsobj, 'tr', 'ov_insiderow ov_inside_redshift_row')
        obj = self.webParser.getItemsByTag(tr, 'td')

        span = self.webParser.getItemsByTag(obj[0], 'span')
        if str(type(span[0])) == "<class 'bs4.element.Tag'>":
            self.Z.append(span[0].text.strip())
            pass
        if str(type(span[1])) == "<class 'bs4.element.Tag'>":
            self.Z.append(span[1].text.strip())
            pass

        span = self.webParser.getItemsByTag(obj[1], 'span')
        if str(type(span[0])) == "<class 'bs4.element.Tag'>":
            self.VHelio.append(span[0].text.strip())
            pass
        if str(type(span[1])) == "<class 'bs4.element.Tag'>":
            self.VHelio.append(span[1].text.strip())
            pass

        span = self.webParser.getItemsByTag(obj[3], 'span')
        if str(type(span[0])) == "<class 'bs4.element.Tag'>":
            self.VCMB.append(span[0].text.strip())
            pass
        if str(type(span[1])) == "<class 'bs4.element.Tag'>":
            self.VCMB.append(span[1].text.strip())
            pass

        span = self.webParser.getItemsByTag(obj[4], 'span')
        if str(type(span[0])) == "<class 'bs4.element.Tag'>":
            self.HubbleDistance.append(span[0].text.strip())
            pass
        if str(type(span[1])) == "<class 'bs4.element.Tag'>":
            self.HubbleDistance.append(span[1].text.strip())
            pass

        tr = self.webParser.getItemByClass(self.bsobj, 'tr', 'ov_insiderow ov_inside_classification_row')
        obj = self.webParser.getItemsByTag(tr, 'td')

        span = self.webParser.getItemByTag(obj[0], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.ObjectType = span.text.strip()
            pass

        span = self.webParser.getItemByTag(obj[1], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.Morphoogy = span.text.strip()
            pass

        span = self.webParser.getItemByTag(obj[3], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.ActivityType = span.text.strip()
            pass

        span = self.webParser.getItemByTag(obj[5], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.OtherClassification = span.text.strip()
            pass

        tr = self.webParser.getItemByClass(self.bsobj, 'tr', 'ov_insiderow ov_inside_sizes_row')
        obj = self.webParser.getItemsByTag(tr, 'td')

        span = self.webParser.getItemByTag(obj[0], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.Passband = span.text.strip()
            pass

        span = self.webParser.getItemByTag(obj[3], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.Diameter = span.text.strip()
            pass

        span = self.webParser.getItemByTag(obj[4], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.A_lambdaV = span.text.strip()
            pass

        span = self.webParser.getItemByTag(obj[5], 'span')
        if str(type(span)) == "<class 'bs4.element.Tag'>":
            self.A_lambdaK = span.text.strip()
            pass
        pass
    pass

if __name__ == '__main__':
    print('NASA/IPAC Extragalatic Database Search')
    print('======================================')
    print('Type Object Name to Search : ')
    name = str(input())
    print('')
    print('Searching... Please Wait for A Moment.')
    print('')
    manager = ExDBManager(name)
    manager.printData()
    print('')
    print("Search Finished. When you're done with your work, please Press Enter.")
    name = input()
    pass
