from re import search
import scrapy
from scrapy_playwright.page import PageMethod
from bestsellers.bestsellers_urls import get_urls
from bestsellers.items import BestsellersItem
from logging import getLogger

logger = getLogger("Bestsellers")

class AmazonBestsellersSpider(scrapy.Spider):
    name = "amazon_bestsellers"
    allowed_domains = ["amazon.com.br"]
    

    def start_requests(self):
        urls = get_urls(self.categories)
        for url in urls:
            yield scrapy.Request(
                url, 
                meta={
                    "playwright": True,
                    "playwight_page_methods": [
                        PageMethod("wait_for_selector", "body"),
                        PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight * 0.85)")
                    ]
                }
            )

    def parse(self, response):
        # 'response' contains the page as seen by the browser
        hrefs = response.css('div.zg-grid-general-faceout>div>a::attr(href)').getall()
        for href in hrefs:
            item = BestsellersItem()
            item["id"] = search(r"/dp/([A-Z0-9]+)", href).groups()[0]
            yield item



