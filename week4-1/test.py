import scrapy

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou-github'
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for course in response.css('li.public'): ###why???
            yield {
                "name": course.xpath('.//h3/a/text()').re('\n\s*(.*)'),
                "update_time": course.xpath('.//relative-time').re('\\"(.+)\\"')
            }

