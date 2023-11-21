from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Scraper:
    def __init__(self, url):
        self.url = url

    def get_empire_tables(self):


        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)

        driver.get(self.url)
        page_source = driver.page_source

        soup = BeautifulSoup(page_source, 'lxml')


        empire_lengths = {}
        length_elems = [a for a in soup.find_all('span', attrs={'class': 'value-bullet'}) if 'Span:' in a.get_text()]
        name_elems = soup.find_all('span', attrs={'class': 'title-bullet'})

        print(length_elems)

        for n, l in zip(name_elems, length_elems):
            n_text = n.get_text()
            l_text = l.get_text()
            empire_lengths[n_text] = l_text

        print(empire_lengths)

if __name__ == '__main__':
    url = "https://247wallst.com/special-report/2021/12/25/the-longest-lived-empires-in-history/"
    scraper = Scraper(url)
    scraper.get_empire_tables()
