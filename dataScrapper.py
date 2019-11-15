import selenium
from selenium import webdriver
from random import randint
import pycountry

# Used to get data from wits.worldbank.org and get top 5 importator
# countries for a given country
class TradeData:
    countries = []
    driver = webdriver.Chrome(executable_path=".//chromedriver")

    # This function will select the correct unit for a given amount
    def __selectUnit(self, value):
        unit = ["K", "M", "B", "T"]
        if len(value) < 4:
            return "K"
        if len(value) < 7:
            return "M"
        if len(value) < 10:
            return "B"
        if len(value) < 14:
            return "T"

    # Search 5 country randomly
    def randomSearch(self):
        countries = []
        i = 0
        while i < 5:
            country = list(pycountry.countries)[randint(
                -1, len(pycountry.countries) - 1)].alpha_3
            countries.append(country)
            i += 1
        for iso in countries:
            print(iso)
            self.searchByIso(iso)
    
    # Ping url with a given iso received as parameter and extract data
    def searchByIso(self, iso):
        self.driver.get(
            "https://wits.worldbank.org/CountryProfile/en/Country/" + iso +
             "/Year/2017/TradeFlow/Export/Partner/by-country/Product/Total")

        for i in range(0, 4):
            try:
                html = self.driver.find_element_by_id("row" + str(i) + "jqx-ProductGrid")
                country = html.find_element_by_tag_name("a")
            except:
                print("[ISO CODE ERROR] Unavailable data for " + iso + ".")
                exit()
            url = country.get_attribute("href").split('/')
            unit = self.__selectUnit(
                html.text.split("\n")[1].split('.')[0].replace(',', ''))
            self.countries.append(
                "> " + url[-3:][0] + " " + html.text.split("\n")[1].split(',')[0] + unit)