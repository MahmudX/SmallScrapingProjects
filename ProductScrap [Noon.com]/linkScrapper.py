from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import csv
from time import sleep
import json
driver = Chrome("chromedriver")
allcatlist = ["https://www.noon.com/uae-en/electronics",
              "https://www.noon.com/uae-en/beauty", "https://www.noon.com/uae-en/fashion", "https://www.noon.com/uae-en/home-kitchen", "https://www.noon.com/uae-en/sports-outdoors", "https://www.noon.com/uae-en/toys", "https://www.noon.com/uae-en/baby", "https://www.noon.com/uae-en/grocery", "https://www.noon.com/uae-en/automotive-store", "https://www.noon.com/uae-en/tools-and-home-improvement-store", "https://www.noon.com/uae-en/book-store", "https://www.noon.com/uae-en/pet-store", "https://www.noon.com/uae-en/stationery", "https://www.noon.com/uae-en/music-movies-and-tv-shows-store"]

urls_all = ["https://www.noon.com/uae-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905",
            "https://www.noon.com/uae-en/electronics-and-mobiles/mobiles-and-accessories/accessories-16176",
            "https://www.noon.com/uae-en/electronics-and-mobiles/computers-and-accessories/tablets",
            "https://www.noon.com/uae-en/electronics-and-mobiles/computers-and-accessories/routers",
            "https://www.noon.com/uae-en/electronics-and-mobiles/computers-and-accessories/data-storage",
            "https://www.noon.com/uae-en/inputdevices", "https://www.noon.com/uae-en/electronics-and-mobiles/software-10182",
            "https://www.noon.com/uae-en/electronics-and-mobiles/computers-and-accessories/laptop-accessories/bags-and-cases-16607/sleeves-and-slipcases-23672",
            "https://www.noon.com/uae-en/laptops-best-selling-ae", "https://www.noon.com/uae-en/electronics-and-mobiles/portable-audio-and-video/headphones-24056",
            "https://www.noon.com/uae-en/all-speakers", "https://www.noon.com/uae-en/home-and-kitchen/home-appliances-31235",
            "https://www.noon.com/uae-en/electronics-and-mobiles/wearable-technology", "https://www.noon.com/uae-en/electronics-and-mobiles/camera-and-photo-16165",
            "https://www.noon.com/uae-en/electronics-and-mobiles/television-and-video/televisions", "https://www.noon.com/uae-en/electronics-and-mobiles/television-and-video/home-theater-systems-19095",
            "https://www.noon.com/uae-en/electronics-and-mobiles/television-and-video/projectors", "https://www.noon.com/uae-en/electronics-and-mobiles/accessories-and-supplies/audio-and-video-accessories-16161",
            "https://www.noon.com/uae-en/electronics-and-mobiles/video-games-10181/gaming-console",
            "https://www.noon.com/uae-en/electronics-and-mobiles/video-games-10181/games-34004", "https://www.noon.com/uae-en/electronics-and-mobiles/wearable-technology/virtual-reality-headsets/gaminghub",
            "https://www.noon.com/uae-en/electronics-and-mobiles/video-games-10181/gaming-accessories", "https://www.noon.com/uae-en/electronics-and-mobiles/portable-audio-and-video",
            "https://www.noon.com/uae-en/beauty-and-health/beauty/fragrance", "https://www.noon.com/uae-en/beauty-and-health/beauty/makeup-16142", "https://www.noon.com/uae-en/nails-20024",
            "https://www.noon.com/uae-en/beauty-and-health/beauty/hair-care", "https://www.noon.com/uae-en/beauty-and-health/beauty/skin-care-16813",
            "https://www.noon.com/uae-en/beauty-tools-and-accessories", "https://www.noon.com/uae-en/beauty-and-health/beauty/personal-care-16343",
            "https://www.noon.com/uae-en/mens-grooming", "https://www.noon.com/uae-en/beauty-and-health/health",
            "https://www.noon.com/uae-en/toys-and-games", "https://www.noon.com/uae-en/sports-and-outdoors/outdoor-recreation/camping-and-hiking-16354",
            "https://www.noon.com/uae-en/sports-and-outdoors/cycling-16009", "https://www.noon.com/uae-en/sports-and-outdoors/other-sports", "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328",
            "https://www.noon.com/uae-en/sports-and-outdoors/boating-and-water-sports", "https://www.noon.com/uae-en/sports-and-outdoors/racquet-sports-16542",
            "https://www.noon.com/uae-en/build-your-own-gym", "https://www.noon.com/uae-en/sports-and-outdoors/team-sports",
            "https://www.noon.com/uae-en/sports-and-outdoors/leisure-sports-and-games", "https://www.noon.com/uae-en/beauty-and-health/health/sports-nutrition",
            "https://www.noon.com/uae-en/automotive", "https://www.noon.com/uae-en/tools-and-home-improvement", "https://www.noon.com/uae-en/office-supplies",
            "https://www.noon.com/uae-en/books", "https://www.noon.com/uae-en/fashion/men-31225", "https://www.noon.com/uae-en/fashion/women-31229",
            "https://www.noon.com/uae-en/view-all-kids-clothing", "https://www.noon.com/uae-en/fashion/luggage-and-bags", "https://www.noon.com/uae-en/jewellery-store", "https://www.noon.com/uae-en/bau-watches-eyewear",
            "https://www.noon.com/uae-en/pet-supplies", "https://www.noon.com/uae-en/grocery-store?limit=150", "https://www.noon.com/uae-en/home-and-kitchen/bath-16182", "https://www.noon.com/uae-en/home-and-kitchen/bedding-16171",
            "https://www.noon.com/uae-en/home-and-kitchen/furniture-10180", "https://www.noon.com/uae-en/home-appliances", "https://www.noon.com/uae-en/home-and-kitchen/home-decor", "https://www.noon.com/uae-en/home-and-kitchen/household-supplies"
            "https://www.noon.com/uae-en/home-and-kitchen/kids-home-store", "https://www.noon.com/uae-en/home-and-kitchen/patio-lawn-and-garden", "https://www.noon.com/uae-en/home-and-kitchen/storage-and-organisation",
            "https://www.noon.com/uae-en/tools-and-home-improvement", "https://www.noon.com/uae-en/home-and-kitchen/kitchen-and-dining", "https://www.noon.com/uae-en/kitchenappliances",
            "https://www.noon.com/uae-en/baby-products"
            ]


def GetAllValidProductUrl():
    return urls_all


def GetProductLinks(url, start, end):
    driver.get(url)
    Links = []
    prev = ''
    for x in range(start, end):
        try:
            driver.get(url+'?page='+str(x))
            if driver.current_url == prev:
                break
            else:
                prev = driver.current_url
        except:
            break

        soup = BeautifulSoup(driver.page_source, "html.parser")
        prodContainer = soup.find_all(
            'div', attrs={'class': 'jsx-3152181095 productContainer'})
        for x in prodContainer:
            link = 'https://www.noon.com'+x.find('a')['href']
            Links.append(link)
    driver.close()
    return Links
