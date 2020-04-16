from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from time import sleep
import helper
import csv
driver = Chrome()


def main():
    print("Started operation.")
    url = "https://www.btcelectronics.com/manufacturers?pmc=CS-Preferred"
    links = helper.getcategorylinks(url, driver)
    for x in links:
        print("Processing", x)
        driver.get(x)
        sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        headline = " "
        output = [x]
        try:
            headline = soup.find('h1').text
            output.append(headline)
        except:
            output.append("N/A")
        try:
            getsec = soup.find('div', attrs={'class': 'catDesc'})
            getdesc = getsec.find_all('p')
            companyLink = getsec.find('a', attrs={'class': 'links'})['href']
            desc = ""
            for d in getdesc:
                try:
                    desc += d.text
                except:
                    pass
                try:
                    desc += d.text
                except:
                    pass
            output.append(companyLink)
            output.append(desc)

        except:
            print("No description available")
            output.append("N/A")
        with open("output.csv", 'a+', encoding='utf8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(output)
    print("Done")


if __name__ == "__main__":
    main()
