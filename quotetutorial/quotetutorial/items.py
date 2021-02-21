# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#Extracted data -->> Temporary containers (Items) --> Store in Database/others

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    pass
