import re
import logging
from bs4 import BeautifulSoup

from Scraping_book_project.locators.page_locator import AllBooksPageLocator
from Scraping_book_project.parsers.book_parser import BookParser

logger= logging.getLogger('scraping.all_books_page')

class AllBookPage:
    def __init__(self, page_content):
        self.soup= BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocator.BOOKS)]

    @property
    def page_count(self):
        content= self.soup.select_one(AllBooksPageLocator.PAGER).string
        pattern= 'Page [0-9]+ of ([0-9]+)'
        matcher= re.search(pattern, content)
        pages= int(matcher.group(1))
        return pages