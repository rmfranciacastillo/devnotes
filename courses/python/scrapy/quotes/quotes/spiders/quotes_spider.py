# Install virtual env:  
# python3 -m venv env
# source env/bin/activate
# pip install scrapy 
# scrapy runspider quotes_spider.py -o quotes.json -t json
# You can run the scraper with an argument:
#   scrapy crawl quotes -O quotes-humor.json -a tag=humor

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# class QuotesSpider(scrapy.Spider):
    # name = "quotes"
    # start_urls = [
        # 'http://quotes.toscrape.com/page/1/',
    # ]

    # def parse(self, response):
        # for quote in response.css('div.quote'):
            # yield {
                # 'text': quote.css('span.text::text').get(),
                # 'author': quote.css('small.author::text').get(),
                # 'tags': quote.css('div.tags a.tag::text').getall(),
            # }

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
            # # next_page = response.urljoin(next_page)
            # # yield scrapy.Request(next_page, callback=self.parse)
            # yield response.follow(next_page, callback=self.parse)
