import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    '''
    Паук для парсинга документов PEP.

    status_selector     CSS-селектор для поиска значения статуса в
                        коде страницы;
    pep_link_selector   XPath-селектор, для получения ссылок на документы PEP.
                        Ссылки берутся из таблиц на основной странице.
                        Т.к. в одной строке таблицы указывается несколько
                        ссылок на один документ, осуществляется поиск тега
                        <a>, текст которого содержит только цифры - номер PEP.
    '''
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]
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
