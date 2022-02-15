from bs4 import BeautifulSoup

from Scraping_project.locators.quotes_page_locator import QuotesPageLocators
from Scraping_project.parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, page):
        self.soup= BeautifulSoup(page, 'html.parser')
        
    @property
    def quotes(self):
        locator= QuotesPageLocators.QUOTE
        quote_tags= self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]