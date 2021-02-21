# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RaidforumsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_name = scrapy.Field()
    post_by = scrapy.Field()
    post_date = scrapy.Field()
    post_views = scrapy.Field()
    post_replies = scrapy.Field()
    link_to_page = scrapy.Field()
    # name = scrapy.Field()
    # name = scrapy.Field()
    pass
