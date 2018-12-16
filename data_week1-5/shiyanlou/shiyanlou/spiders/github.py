# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        repos = response.xpath('//div[@class="col-9 d-inline-block"]')
        for repo in repos:
            item = ShiyanlouItem()
            item['repo_name'] = repo.xpath('.//div[@clacc="d-inline-block mb-1"]/text()').extract_first()
            item['update_time'] = repo.xpath('.//div[@class=""]/text()').extract_first()
            yield item
