import os
import enum

import xml.etree.ElementTree as ET
from urllib.request import urlretrieve

class supportedFilings(enum.Enum):
    tenQ = 0
    tenK = 1


    def __str__(self,
                strRepr = ["10-Q", "10-K"]
                ):
        return strRepr[self.value]


class filingManifest():
    def __init__(self, cikTickerPair, fileType = supportedFilings.tenQ, dirPrefix="."):
        self.originPair = cikTickerPair
        self.fileType = fileType
        self.dirPrefix = dirPrefix
        self.url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&type=10-Q&dateb=&owner=exclude&count=40&output=atom" %(self.originPair.ticker)
        self.dirName = "%s\%s\%s" %(self.dirPrefix, self.originPair.ticker, str(self.fileType))
        self.name = "%s\%s" %(self.dirName, "manifest.xml")

    def __exit__(self):
        pass

    def _prepareDir(self):
        os.makedirs(os.path.dirname(self.name), exist_ok=True)

    def retrieveManifest(self):
        self._prepareDir()
        urlretrieve(self.url, self.name)
        self._readManifest()

    def _readManifest(self):
        ns = {"ns" : "http://www.w3.org/2005/Atom"}
        self.manifestXML = ET.parse(self.name).getroot()
        self.companyInfo = self.manifestXML.findall("./ns:company-info", ns)[0]
        self.cik = self.companyInfo.findall("./ns:cik", ns)[0].text



