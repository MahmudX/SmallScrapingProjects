from bs4 import BeautifulSoup
from time import sleep
import json

def Scrap(url, driver):
    na = "N/A"
    driver.get(url)
    sleep(1)

    # Get Overview
    soup = BeautifulSoup(driver.page_source, "html.parser")
    try:
        overview = soup.find_all('li', attrs={'class': 'jsx-1889249662'})
        over = []
        for x in overview:
            over.append(x.text)
        overview = ", ".join(over)
        if len(overview) == 0:
            overview = na
    except:
        overview = na

    try:
        driver.find_elements_by_class_name("react-tabs__tab")[1].click()
        soup = BeautifulSoup(driver.page_source, "html.parser")
    except:
        pass

    # Get Rating and reviews
    try:
        rating = soup.find(
            'p', attrs={"class": "jsx-2756475694 scoreTag"}).text
    except:
        rating = na

    try:
        reviews = soup.find(
            'p', attrs={"class": "jsx-2756475694 counter"}).text
    except:
        reviews = na

    # Get Breadcrumb
    try:
        breadcrumb = soup.find_all(
            'span', attrs={'class': 'jsx-447347517 crumb'})
        crumbs = []
        for x in breadcrumb:
            crumbs.append(x.text)
    except:
        crumbs = na
    breadcrumb = " > ".join(crumbs)

    # Get script
    scripts = soup.find_all(
        'script', attrs={'class': 'next-head', 'type': 'application/ld+json'})
    for x in scripts:
        try:
            sku = json.loads(x.text)
            ID = sku['sku']
            name = sku['name'].replace('Shop', '')
            desc = sku['description']
            brand = sku['brand']['name']
            producturl = sku['offers']["url"]
            images = sku['image']
            price = str(sku["offers"]['price']) + " " + \
                sku["offers"]['priceCurrency']
            break
        except:
            pass
    try:
        table = soup.find_all("tr", attrs={'class': "jsx-1537324451"})
        spec = []
        for x in table:
            s = x.find_all('td')
            spec.append((s[0].text + " : " + s[1].text))
        spec = ", ".join(spec)
    except:
        spec = na
    single = [ID, name, rating, reviews, desc, spec, overview,
              price, brand, breadcrumb, producturl]
    for x in images:
        single.append(x)
    return single



