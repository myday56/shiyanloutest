# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']
    # @property 
    # def starts_urls(self):
    #     url_tmpl = 'https://github.com/shiyanlou?tab=repositories'
        

    def parse(self, response):
        repos = response.xpath('//div[@class="col-9 d-inline-block"]')
        for repo in repos:
            item = ShiyanlouItem({
                'repo_name' : repo.xpath('.//h3/a/text()').re_first('\\n\\s*(.+)'),
                'update_time' : repo.xpath('.//relative-time').re_first('<relative-time datetime="(.{20})')
            })
            yield item
        for url in response.xpath('//div[@class="pagination"]/a[contains(text(),"Next")]'):
            yield response.follow(url,callback=self.parse)
