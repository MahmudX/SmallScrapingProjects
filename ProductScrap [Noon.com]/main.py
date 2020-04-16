from selenium.webdriver import Chrome
import csv
import prodscrapper
import linkScrapper


def main():

    header = ["ID", "Name", "Rating", "Reviews", "Desc", "Spec", "Overview",
              "Price", "Brand", "Breadcrumb", "URL", "Images"]

    moviedata_csv_file = open('productData.csv', 'a+',
                              newline='', encoding="utf-8")
    writer = csv.writer(moviedata_csv_file)
    writer.writerow(header)
    print("To scrap the entire website, type \'all\' below.")
    url = input("Enter a valid url: ")

    if url != 'all':
        start = int(input("Start index: "))
        end = int(input("Ending index: "))
        urls = linkScrapper.GetProductLinks(url, start, end)
        driver = Chrome("chromedriver")
        for x in urls:
            print("Processing:",x)
            writer.writerow(prodscrapper.Scrap(x, driver))
    else:
        parentUrl = linkScrapper.GetAllValidProductUrl()
        for u in parentUrl:
            urls = linkScrapper.GetProductLinks(u, 1, 10000000000000000000000)
            driver = Chrome("chromedriver")
            for x in urls:
                print("Processing:", x)
                writer.writerow(prodscrapper.Scrap(x, driver))

    driver.close()


if __name__ == "__main__":
    main()
