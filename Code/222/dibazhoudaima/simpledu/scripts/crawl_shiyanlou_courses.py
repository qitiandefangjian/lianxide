
import scrapy

class CoursesSpider(scrapy.Spider):

    name = 'courses'

    start_urls = ['https://www.shiyanlou.com/bootcamp/']

    def parse(self, response):
        for course in response.css('div.col-4'):
            yield {
                'name': course.css('div.course-body p::text').extract_first().strip(),
                'description': course.css('div.course-body p.course-desc::text').extract_first().strip(),
                'image_url': course.css('div.course-header img::attr(src)').extract_first().strip()
            }
