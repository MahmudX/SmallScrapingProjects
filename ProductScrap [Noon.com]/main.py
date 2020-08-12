from selenium.webdriver import Firefox
import csv
import prodscrapper
import linkScrapper
from tqdm import tqdm


def main():

    header = ["ID", "Name", "Rating", "Reviews", "Desc", "Spec", "Overview",
              "Price", "Brand", "Breadcrumb", "URL", "Images"]

    moviedata_csv_file = open('productData.csv', 'a+',
                              newline='', encoding="utf-8")
    writer = csv.writer(moviedata_csv_file)
    writer.writerow(header)
    print("To scrap the entire website, type \'all\' below. To scrap a signle product info type \'product\'")
    url = input("Enter a valid listing url: ")

    if url != 'all':
        start = int(input("Start index: "))
        end = int(input("Ending index: "))
        urls = linkScrapper.GetProductLinks(url, start, end)
        driver = Firefox()
        for x in urls:
            print("Processing:", x)
            writer.writerow(prodscrapper.Scrap(x, driver))
    elif url == 'product':
        while True:
            produrl = input("Enter a valid product URL:")
            writer.writerow(prodscrapper.Scrap(produrl, driver))
            t = input("Done. Press ENTER to scrap next product. Type exit() to exit the loop.")
            if t == "exit()":
                break
    else:
        parentUrl = linkScrapper.GetAllValidProductUrl()
        for u in tqdm(parentUrl):
            urls = linkScrapper.GetProductLinks(u, 1, 10000000000000000000000)
            driver = Firefox()
            for x in tqdm(urls):
                print("Processing:", x)
                writer.writerow(prodscrapper.Scrap(x, driver))

    driver.close()


if __name__ == "__main__":
    main()
