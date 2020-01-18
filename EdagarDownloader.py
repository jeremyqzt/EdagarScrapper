from dbUtils.dbTable import *
from CIKTickerPair import *
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
        for i in self.tickerCIK.tickerCIKGenerator():
            #Methods to download other filings!
            testTuple = i + ("test", "", "" , "", "")
            print(testTuple)
            self.db.insertCompany(testTuple)

test = EdgarDownloader()
test._createCIKTickerMap()
