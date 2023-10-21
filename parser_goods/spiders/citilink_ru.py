import scrapy
from scrapy.http import HtmlResponse


class CitilinkRuSpider(scrapy.Spider):
    name = "citilink_ru"
    allowed_domains = ["citilink.ru"]
    #start_urls = "https://www.citilink.ru/search/?text=химия+для+бассейнов"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)        
        self.start_urls = ["https://www.citilink.ru/search/?text=химия+для+бассейнов"]

    def parse(self, response:HtmlResponse):

        links = response.xpath("//a[contains(@class, 'product-card__name')]/@href")
        for link in links:
            yield response.follow(link, callback=self.parse_goods)

    def parse_goods(self, response:HtmlResponse):
        print(f'\n\n####\n\n{response.url}\n\n####\n\n')



