from dbUtils.dbTable import *
from downloaderUtils.CIKTickerPair import *
from downloaderUtils.FilingsManifest import *


class CIKTickerPair:
    def __init__(self, dbTuple):
        self.ticker = dbTuple[0]
        self.cik = dbTuple[1]


class EdgarDownloader():
    def __init__(self):
        self.tickerCIK = CIKTickerInitializer()
        self.db = dbSecCikFilings()
        self._seedSupportedFilings()

    def __exit__(self):
        pass

    def _seedSupportedFilings(self):
        pass

    def _createCIKTickerMap(self):
        dest = "EdagarData"
        for i in self.tickerCIK.tickerCIKGenerator():
            #Methods to download other filings!
            testTuple = i + ("test", "", "" , "", "")
            #print(testTuple)
            pair = CIKTickerPair(i)
            manifest = filingManifest(pair, supportedFilings.tenQ, dest).retrieveManifest()

            self.db.insertCompany(testTuple)

test = EdgarDownloader()
test._createCIKTickerMap()
