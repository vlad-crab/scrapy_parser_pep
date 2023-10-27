import scrapy
import re

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        numerical_index_table = response.css(
            '#numerical-index'
        ).css('a.reference')
        for url in numerical_index_table:
            yield response.follow(url, callback=self.parse_pep)

    def parse_pep(self, response):
        h1 = response.css('#pep-content > h1::text').get()
        number = h1.split(' ')[1]
        name = re.search(r'.* – (?P<name>.*)$', h1).group(1)
        dl = response.css('#pep-content > dl')
        status = dl.css('dt:Contains("Status") + dd').css('abbr::text').get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
