import scrapy

class A1stillumparsSpider(scrapy.Spider):
    name = "A1stillumpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/samara/category/potolocnye-svetilniki"]

    def parse(self, response):
        illuminations = response.css('div._Ud0k')
        for illum in illuminations:
            yield {
                'name': illum.css('div.lsooF span::text').get(),
                'price': illum.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(illum.css('a::attr(href)').get())
            }
