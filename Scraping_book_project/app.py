import requests
import logging
from Scraping_book_project.pages.all_books_page import AllBookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG, filename='logs.txt')
logger= logging.getLogger('scraping')
logger.info("Loading books list...")

page_content= requests.get('http://books.toscrape.com').content
page= AllBookPage(page_content)

books= page.books

for page_num in range(1, page.page_count):
    url= f"http://books.toscrape.com/catalogue/page-{page_num+1}.html"
    page_content= requests.get(url).content
    page= AllBookPage(page_content)
    books.extend(page.books)