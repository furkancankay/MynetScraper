import json
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Safari()
driver.set_window_size(900, 1000)
url = 'https://finans.mynet.com/borsa/hisseler/'
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
links = soup.select('body > section > div.row > div.col-12.col-lg-8.col-content > div:nth-child(3) > div > div > div.table-scrollable-mobil > div > table > tbody > tr > td:nth-child(1) > strong > a')


data_list = []
with open("HisseVerileri.json", "w",encoding="utf-8") as dosya:
    json.dump(data_list, dosya, ensure_ascii=False)
data_list = json.load(open("HisseVerileri.json"))

for id, link in enumerate(links):
    driver.get(link.get('href'))
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    datas = soup.select('.flex-list-2-col')
    brand = soup.select('div.flex-list-heading > h2')
    table = datas[0] if datas else None
    if table:
        rows = table.find_all('li')
        print(f'\n\n{id+1}. Hissenin verileri ({brand[0].text})')
        dictionary = {"id": id+1, "brand": brand[0].text, "veriler": []} 
        for row in rows:
            span_labels = row.find_all('span')
            label = span_labels[0].text.strip()
            value = span_labels[1].text.strip()
            print(f"{label}: {value}")
            dictionary["veriler"].append({label: value})  
        
    data_list.append(dictionary) 
    with open("HisseVerileri.json", "w",encoding="utf-8") as dosya:
        json.dump(data_list, dosya, ensure_ascii=False, indent=4)

driver.quit()


