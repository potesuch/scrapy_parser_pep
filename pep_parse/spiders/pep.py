import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']
    count = 0

    def parse(self, response):
        rows = response.css('#numerical-index tbody tr')
        for row in rows:
            pep_link = row.css('a[href^="pep-"]::attr(href)').get()
            self.count += 1
            yield response.follow(pep_link, self.parse_pep)

    def parse_pep(self, response):
        pep_content = response.css('#pep-content')
        pep_title = pep_content.css('h1::text').get()
        number, name = pep_title.split('–', 1)
        number = number.replace('PEP', '')
        status = pep_content.css(
            'dt:contains("Status") + dd abbr::text'
        ).get()
        yield PepParseItem(number=number, name=name, status=status)
