"""In this project, we will scrap some stock values and save from mynet.com."""

import json
from selenium import webdriver
from bs4 import BeautifulSoup

class MynetHisseBilgileri:
    """Necessary values are drawn with the beautifulsoup library as initial values."""
    def __init__(self):
        self.driver = webdriver.Safari()
        self.url = 'https://finans.mynet.com/borsa/hisseler/'
        self.driver.get(self.url)
        self.page_source = self.driver.page_source
        self.soup = BeautifulSoup(self.page_source, 'html.parser')
    def get_stocks_links(self,name:str):
        """Its takes brand's name."""
        if name == '':
            name = input('Enter a brand that you want: ')
        else:
            pass
        tbodybrands = self.soup.select('span.hide-m')
        for i,brand in enumerate(tbodybrands):
            if brand.text == name:
                links = self.soup.select('tbody > tr > td > strong > a')
                return links[i]['href']


    def show_all_stocks_names(self):
        """Fetches the links from the names of the shares."""
        tbodybrands = self.soup.select('span.hide-m')
        for i in tbodybrands:
            print(i.text)

    def take_data_from_link(self, url):
        """Pulls stock data from links."""
        self.driver.get(url)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        datas = soup.select('.flex-list-2-col')
        brand = soup.select('div.flex-list-heading > h2')
        table = datas[0] if datas else None
        if table:
            rows = table.find_all('li')
            print(f'\n\nBrand name: ({brand[0].text})\n')
            dictionary = {"brand": brand[0].text, "veriler": []}
            for row in rows:
                span_labels = row.find_all('span')
                label = span_labels[0].text.strip()
                value = span_labels[1].text.strip()
                print(f"{label}: {value}")
                dictionary["veriler"].append({label: value})
            return dictionary
    def save_as_a_jsonfile(self, datas):
        """Saves data as json."""
        try:
            with open("HisseVerileri.json", "r", encoding="utf-8") as dosya:
                data_list = json.load(dosya)
            for item in data_list:
                if item['brand'] == datas['brand']:
                    item['veriler'] = datas['veriler']
                    break
            else:
                data_list.append(datas)
        except FileExistsError:
            data_list = [datas]

        with open("HisseVerileri.json", "w", encoding="utf-8") as dosya:
            json.dump(data_list, dosya, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    while True:
        MynetHisseBilgileri().show_all_stocks_names()
        chosenBrand = input('Enter which you want brand: ')
        brandsLink = MynetHisseBilgileri().get_stocks_links(chosenBrand)
        StockData = MynetHisseBilgileri().take_data_from_link(brandsLink)
        MynetHisseBilgileri().save_as_a_jsonfile(StockData)
        breaker = input('Press "e" to exit or press anything: ')
        if breaker == "e":
            break
