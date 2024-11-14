import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://' + domain for domain in allowed_domains]
    status_selector = 'dt:contains("Status") + dd abbr::text'
    pep_link_selector = (
        '//section[@id="index-by-category"]//'
        r'a[re:test(., "^\d+$")]//@href'
    )

    def parse(self, response):
        # Поиск тега <a>, содержащего в теле только цифру
        for link in response.xpath(self.pep_link_selector).getall():
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.css('h1.page-title::text').get().
            split(' – ', 1))
        number = number.split(' ')[-1]
        data = {
            'number': number,
            'name': name,
            'status': response.css(self.status_selector).get()
        }
        yield PepParseItem(data)
