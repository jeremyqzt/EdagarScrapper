import sqlite3
from contextlib import closing

class dbSecCikFilings():
    def __init__(self, name="EdgarCIKFiling.db"):
        self.name = name
        self.con = sqlite3.connect(self.name)
        self.__createSchemaIfNotExist()

    def __exit__(self):
        self.con.close()

    def __createSchemaIfNotExist(self):
        cursorObj = self.con.cursor()

        cursorObj.execute("""CREATE TABLE  IF NOT EXISTS [ReportsTypes] (
	[ReportTypeID] INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
	[ReportType] NVARCHAR(50)  NULL
        );""")

        cursorObj.execute("""CREATE TABLE IF NOT EXISTS [Industries] (
	[SIC] INTEGER  PRIMARY KEY NOT NULL,
	[Description] NVARCHAR(250)  NULL
        );""")

        cursorObj.execute("""CREATE TABLE IF NOT EXISTS [Companies] (
	[CompanyCIK] INTEGER  NOT NULL,
	[CompanyTicker] NVARCHAR(50)  NULL,
	[CompanyCurrentName] NVARCHAR(50)  NULL,
	[CompanyFormerNameXML] NVARCHAR(500)  NULL,
	[AddressXML] NVARCHAR(500)  NULL,
	[Phone] NVARCHAR(50)  NULL,
	IndustrySIC INTEGER,
	FOREIGN KEY(IndustrySIC) REFERENCES Industries(SIC),
	PRIMARY KEY(CompanyCIK, CompanyTicker)
        );""")

        cursorObj.execute("""CREATE TABLE IF NOT EXISTS [Reports] (
	[ReportID] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	[ReportPath] NVARCHAR(50)  NULL,
	[ReportName] NVARCHAR(250)  NULL,
	[XBRLHREF] NVARCHAR(250)  NULL,
	[FileNumber] NVARCHAR(50)  NULL,
	[FileDateString] NVARCHAR(50)  NULL,
	[CIK] INTEGER NOT NULL,
	[Ticker] NVARCHAR(50)  NULL,
	[Type] INTEGER NOT NULL,
	FOREIGN KEY(Type) REFERENCES ReportsTypes(ReportTypeID),
	FOREIGN KEY(CIK) REFERENCES Companies(CompanyTicker),
	FOREIGN KEY(Ticker) REFERENCES Companies(CompanyTicker)

        );""")

        self.con.commit()
    def insertCompany(self, vals):
        with closing(self.con.cursor()) as cursorObj:
            sql = ''' INSERT INTO Companies(CompanyTicker, CompanyCIK,
            CompanyCurrentName, CompanyFormerNameXML, AddressXML, Phone,
            IndustrySIC) VALUES (?, ?, ?, ?, ?, ?, ?)'''
            cursorObj.execute(sql, vals)
            self.con.commit()

    def getCIKFromTicker(self, ticker):
        ticker = (ticker,)
        with closing(self.con.cursor()) as cursorObj:
            sql = "SELECT * FROM Companies WHERE CompanyTicker LIKE (?)"
            #Return our tuple
            return list(cursorObj.execute(sql, ticker))[0]

    def getTickerFromCIK(self, cik):
        pass


