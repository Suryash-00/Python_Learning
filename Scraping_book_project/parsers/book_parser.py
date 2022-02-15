import re
import logging
from Scraping_book_project.locators.book_locators import BookLocator

logger= logging.getLogger('scraping.book_parser')

class BookParser:
    #This class takes HTML page and find properties of item in it.
    def __init__(self, parent):
        self.parent= parent

    def __repr__(self):
        return f'<Book {self.name}, {self.price} ({self.rating} stars)>'

    RATING= {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    @property
    def name(self):
        locator= BookLocator.NAME_LOCATOR
        item_link= self.parent.select_one(locator)
        item_name= item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator= BookLocator.LINK_LOCATOR
        item_link= self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator= BookLocator.PRICE_LOCATOR
        item_price= self.parent.select_one(locator).string
        pattern= '£([0-9]+\.[0-9]+)'
        matcher= re.search(pattern, item_price)
        return float(matcher.group(1))  #To turn string into float

    @property
    def rating(self):
        locator= BookLocator.RATING_LOCATOR
        star_rating_tag= self.parent.select_one(locator)
        classes= star_rating_tag.attrs['class']
        rating_classes= [r for r in classes if r!='star-rating']
        rating_number= BookParser.RATING.get(rating_classes[0])
        return rating_number