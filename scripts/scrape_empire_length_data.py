from bs4 import BeautifulSoup
from selenium import webdriver


class Scraper:
    def __init__(self, url):
        self.url = url

    def get_empire_tables(self):

        driver = webdriver.Firefox()

        driver.get(self.url)
        page_source = driver.page_source

        soup = BeautifulSoup(page_source, 'lxml')

        print(soup)

if __name__ == '__main__':
    url = "https://247wallst.com/special-report/2021/12/25/the-longest-lived-empires-in-history/"
    scraper = Scraper(url)
    scraper.get_empire_tables()
