# Mynet scraper

Mynet scraper is a Python Class for the information of stocks on the mynet site.
Mynet stocks site: [Mynet](https://finans.mynet.com/borsa/hisseler/)

Below is a python commands for example usage.

## Installation

1. Clone the project from GitHub to copy it to your local computer:

```bash
git clone https://github.com/furkancankay/WebScrappingExcercise/blob/main/ScrapMynet.py
cd mynet
```

2. Create and Activate the Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

If you want to install with makefile

```bash
make make_env
```

3. Command line to set up the requirements

```bash
pip install -r requirements.txt
```

If you want to install with makefile

```bash
make install_requirements
```

4. Run the Application

```bash
python main.py
```

If you want to install with makefile

```bash
make run
```

## Usage example

```python
#
if(__name__ == '__main__'):
    while True:
        MynetHisseBilgileri().showAllStocksNames()                        # User can see all brands
        chosenBrand = input('Enter which you want brand: ')               # Then brand's name taking
        brandsLink = MynetHisseBilgileri().getStocksLinks(chosenBrand)    # From brand's name, it is taking the brand's link
        StockData = MynetHisseBilgileri().takeDataFromLink(brandsLink)    # From brand's Link, it is taking the brand's datas
        MynetHisseBilgileri().saveAsAJsonFile(StockData)                  # And the datas can be save as a json file
        breaker = input('Press "e" to exit or press anything: ')
        if(breaker == "e"):
            break
```
