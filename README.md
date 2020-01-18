# EdagarScrapper
Project designed to scrap SEC's EDGAR filings

# Progress Step 1
The following file has the mapping between CIK and ticker
It should be about 14,000 - 15,000 entries in total (as of Jan/2020)
https://www.sec.gov/include/ticker.txt

Download it and store the mapping into a DB

Currently (100% Done)

# Progress Step 2
Step 2 is to implement a filing class and a filing aggregator class -> downloads certain types of filings
from the following URL. the CIK field seems to take both tickers and CIKs. 

https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=AAPL&type=10-Q&dateb=&owner=exclude&count=40&output=atom

You might then get something like:
https://www.sec.gov/Archives/edgar/data/320193/000032019319000076/0000320193-19-000076-index.htm
or
https://www.sec.gov/cgi-bin/viewer?action=view&amp;cik=320193&amp;accession_number=0000320193-19-000076&amp;xbrl_type=v

But Im not currently sure how to get the source XBRL...

Currently (10% Done)