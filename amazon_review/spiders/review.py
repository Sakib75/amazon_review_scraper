import scrapy
from ..items import AmazonReviewItem
from scrapy.loader import ItemLoader

class ReviewSpider(scrapy.Spider):
    name = 'review'
    start_urls = ['https://www.amazon.com/Nintendo-Console-Resolution-802-11ac-Surround/product-reviews/B07RGFF98S/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1']
    page_no = 1
    def parse(self, response):
        
        reviews = response.xpath("//div[@data-hook='review']")
        print(len(reviews))
        if(len(reviews)):
            product_title = response.xpath("//h1/a/text()").getall()[-1]
            product_url = response.xpath("//h1/a/@href").get()
            for review in reviews:
                loader = ItemLoader(item=AmazonReviewItem(), selector=review,response=response)
                loader.add_value('product_title',product_title)
                loader.add_value('product_url',product_url)
                loader.add_xpath('name','./div/div/div/a/div[2]/span/text()')
                loader.add_xpath('rating','./div/div/div[2]/a/i/span/text()')
                loader.add_xpath('review_short','./div/div/div[2]/a[2]/span/text()')
                loader.add_xpath('review_long','./div/div/div[4]/span/span/text()')
                loader.add_xpath('name','./div/div/div/a/div[2]/span/text()')
                yield loader.load_item()
            self.page_no = self.page_no + 1
            yield scrapy.Request(url=f"https://www.amazon.com/Nintendo-Console-Resolution-802-11ac-Surround/product-reviews/B07RGFF98S/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={self.page_no}",callback=self.parse,headers={'Referer':None})
