import scrapy

class LoginSpeeeiderSpider(scrapy.Spider):
    name = 'login_spider'

    start_urls = ['https://www.shiyanlou.com/login']

    def parse(self, response):
   
        csrf_token = response.xpath('//div[@class="login-body"]//input[@id="csrf_token"]/@value').extract_first()
        #self.logger.info(csrf_token)
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'csrf_token': csrf_token,
           
                'login': '1084772020@qq.com',
                'password': 'woaini123456',
            },
            callback=self.aftaer_login
        )

    def aftaer_login(self, response):
      
        return [scrapy.Request(
            url='https://www.shiyanlou.com/user/736362/',
            callback=self.parse_aftaer_login
        )]

    def parse_aftaer_login(self, response):
      
        return {
            'lab_count': response.xpath('(//span[@class="info-text"])[2]/text()').re_first('[^\d]*(\d*)[^\d]*'),
            'lab_minutes': response.xpath('(//span[@class="info-text"])[3]/text()').re_first('[^\d]*(\d*)[^\d]*')
        }
