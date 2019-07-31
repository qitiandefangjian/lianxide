# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem

class UsersSpider(scrapy.Spider):
    name = 'users'
    
    @property
    def start_urls(self):
        return ('https://www.shiyanlo'
         'u.com/user/{}/'.format(i) for i in range(525000,524800, -10))
    def parse(self,response):
        yield UserItem({
            'name': response.css('span.username::text').extract_first(default='1'),
            'type': response.css('a.member-icon img.user-icon::attr(title)').extract_first(default='ptyonghu'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(default='1'),
            'school_job': response.xpath('//div[@class="userinof-banner-status"]/span[2]/text()').extract_first(default='1'),
            'join_date': response.css('span.join-date::text').extract_first(default='1'),
            'level': response.css('span.user-level::text').extract_first(default='1'),
            'learn_courses_num': response.css('span.latest-learn-num::text').extract_first(default='1')
        })     
