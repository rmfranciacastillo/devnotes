import scrapy 

class BooksSpider(scrapy.Spider): 

    name = "books"
    start_urls = ["https://books.toscrape.com/index.html"]
    allowed_domains = ["books.toscrape.com"]
    
    def parse(self, response):

        for book in response.xpath('//article'):
            yield {
                'title': book.xpath('//h3/a/text()').get()
            }
