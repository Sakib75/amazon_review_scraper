# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join

def parse_url(url):
    return "https//amazon.com" + url

class AmazonReviewItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    product_title = scrapy.Field(output_processor=TakeFirst())
    product_url = scrapy.Field(output_processor=TakeFirst(),input_processor=MapCompose(parse_url))
    rating = scrapy.Field(output_processor=TakeFirst())
    review_short = scrapy.Field(output_processor=TakeFirst())
    review_long = scrapy.Field(output_processor=Join(),input_processor=MapCompose(str.strip))

