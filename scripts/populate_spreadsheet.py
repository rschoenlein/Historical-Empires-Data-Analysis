import csv
from scrape_empire_length_data import Scraper

class Populater:
    def __init__(self, dict):
        self.dict = dict

    def populate_spreadsheet(self):
        print(self.dict.keys())
        print(self.dict.values())

        print(type(self.dict))
        with open('empire_lengths.csv', 'w+') as output:
            writer = csv.writer(output)
            for key, value in self.dict.items():
                writer.writerow([key, value])

if __name__ == '__main__':
    url = "https://247wallst.com/special-report/2021/12/25/the-longest-lived-empires-in-history/"
    scraper = Scraper(url)
    pop = Populater(scraper.get_empire_tables())
    pop.populate_spreadsheet()
