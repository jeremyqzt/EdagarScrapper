import datetime
import math
import urllib.request

class EdagerDownloader():
    def __init__(self, start=1994):
        self.IndexUrl = "https://www.sec.gov/Archives/edgar/daily-index"
        self.time = datetime.datetime.now()
        self.startDate = start

    def _createURLs(self):
        retUrls = []
        Quarters = ["QTR1", "QTR2", "QTR3", "QTR4"]

        retUrls.append(self.IndexUrl + "/1994/QTR3/")
        retUrls.append(self.IndexUrl + "/1994/QTR4/")
        #1994 has to be manually created as it only has QTR3/4
        for i in range(self.startDate + 1, self.time.year):
            for qtr in Quarters:
                retUrls.append("%s/%d/%s/" %(self.IndexUrl, i, qtr))

        curYearQtrs = math.ceil(self.time.month / 4)
        for i in range (1, curYearQtrs + 1):
                retUrls.append("%s/%d/%s/" %(self.IndexUrl, self.time.year, Quarters[i-1]))
        return (retUrls)

    def _dlIndexFiles(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        print(text)

test = EdagerDownloader()
array = test._createURLs()
test._dlIndexFiles('https://www.sec.gov/Archives/edgar/daily-index/2019/QTR4/')





