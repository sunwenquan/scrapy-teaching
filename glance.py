import warnings

import scrapy
from scrapy.http.request import Request
from scrapy.utils.deprecate import method_is_overridden


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def start_requests(self):
        requests = []
        for url in self.start_urls:
            req = Request(url,dont_filter=True)
            requests.append(req)
        return requests


    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url, dont_filter=True)

    def parse(self, response):
        print('2.',type(response))  # <class 'scrapy.http.response.html.HtmlResponse'>

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        print('3',next_page)
        if next_page is not None:
            temp = response.follow(next_page, self.parse)
            print(type(temp))  # <class 'scrapy.http.request.Request'>
            yield temp
