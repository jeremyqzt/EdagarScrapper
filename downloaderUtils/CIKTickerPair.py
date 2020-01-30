from urllib.request import urlretrieve

class CIKTickerInitializer():
    def __init__(self):
        self.url = "https://www.sec.gov/include/ticker.txt"
        self.name = "ticker.txt"
        urlretrieve(self.url, self.name)
        self._readFile()

    def __exit(self):
        self.f.close()

    def _readFile(self):
        self.f = open(self.name, "r", encoding='utf-8-sig')

    def tickerCIKGenerator(self):
        for line in self.f:
            pair = line.split()
            if len(pair) < 2:
                continue
            yield (pair[0], pair[1])

