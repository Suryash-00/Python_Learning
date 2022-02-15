from Scraping_project.locators.quote_locator import Quote_Locators

class QuoteParser:
    #To find out about the data of the quote(quote content, author, tags)

    def __init__(self, parent):
        self.parent= parent

    def __repr__(self):
        return f'Quote {self.content}, by {self.author}'

    @property
    def content(self):
        locator= Quote_Locators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator= Quote_Locators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator= Quote_Locators.TAGS
        return self.parent.select_one(locator).string