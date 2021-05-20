# Install virtual env:  
# python3 -m venv env
# source env/bin/activate
# pip install scrapy 
# scrapy runspider quotes_spider.py -o quotes.json -s LOG_FILE=quotes.log
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/page/1/']
    allowed_domains = ['quotes.toscrape.com']
    # rules = [
        # Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),
        # callback='parse_items', follow=True),
    # ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
