import dataScrapper
import sys
import dataManager

def help():
    print("Usage:")
    print("> ./exe <ISO CODE>")
    print("\tWill display data for the iso code given")
    print("> ./exe <ISO CODE> save [filename.csv]")
    print("""\tWill save data for the iso code given in a csv
    in a file. Optional parameter let you precise a filename""")

page = dataScrapper.TradeData()
try:
    if sys.argv[1] == "all":
        print("all")
        page.randomSearch()
    else:
        page.searchByIso(sys.argv[1])
    dataManager = dataManager.dataManager()
except:
    exit()

try:
    if sys.argv[2] == "save":
        dataManager.csvValues(page.countries)
except:
    	dataManager.printValues(page.countries)