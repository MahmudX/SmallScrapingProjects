from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep


# def getcategorylinks():
#     driver.get(
#         "https://www.connectorsupplier.com/compro/btc-electronic-components-inc/")
#     sleep(5)
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     getsec = soup.find('div', attrs={'class': 'product_links'})
#     getlinks = getsec.find_all('a')
#     output = []
#     for x in getlinks:
#         if x['href'] not in output:
#             output.append(x['href'])
#             print(x['href'])
#     driver.close()

def getcategorylinks(url,driver):
    driver.get(url)
    sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    getsec = soup.find('div', attrs={'class': 'category-listing'})
    getlinks = getsec.find_all('a')
    output = []
    for x in getlinks:
        if x['href'] not in output:
            output.append(x['href'])
    return output
