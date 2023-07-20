from selenium import webdriver
from bs4 import BeautifulSoup


class MynetHisseBilgileri:
    def __init__(self):
        self.driver = webdriver.Safari()
        self.url = 'https://finans.mynet.com/borsa/hisseler/'
        self.driver.get(self.url)
        self.page_source = self.driver.page_source
        self.soup = BeautifulSoup(self.page_source, 'html.parser')
    def getStocksLinks(self,name):
        if(name == ''):
            name = input('Enter a brand that you want: ')
        else:
            pass
        tbodyBrands = self.soup.select('span.hide-m')
        for i in range(len(tbodyBrands)):
            if(tbodyBrands[i].text == name):
                self.links = self.soup.select('tbody > tr > td > strong > a')
                return self.links[i]['href']
    def showAllStocksNames(self):
        tbodyBrands = self.soup.select('span.hide-m')
        for i in range(len(tbodyBrands)):
            print(tbodyBrands[i].text)
    def takeDataFromLink(self, url):
        self.driver.get(url) 
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        datas = soup.select('.flex-list-2-col')
        brand = soup.select('div.flex-list-heading > h2')
        table = datas[0] if datas else None
        if table:
            rows = table.find_all('li')
            print(f'\n\nBrand name: ({brand[0].text})')
            item_id = 1 
            dictionary = {"id": item_id, "brand": brand[0].text, "veriler": []}
            for row in rows:
                span_labels = row.find_all('span')
                label = span_labels[0].text.strip()
                value = span_labels[1].text.strip()
                print(f"{label}: {value}")
                dictionary["veriler"].append({label: value})
                item_id += 1 
            return dictionary

brands = MynetHisseBilgileri().showAllStocksNames()
brandName = input('Enter which you want brand: ')
link = MynetHisseBilgileri().getStocksLinks(brandName)
start = MynetHisseBilgileri().takeDataFromLink(link)
