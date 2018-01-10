from scrapy.spider import Spider
from jianshu.items import JianshuItem
class JianshuSpider(Spider):
    name = 'jianshu'
    box = []
    for num in range(200):
        pages = 'http://www.jianshu.com/c/263e0ef8c3c3?order_by=commented_at&page={0}'.format(num)
        box.append(pages)
    start_urls = box
    def parse(self, response):
        item = JianshuItem()
        articles = response.xpath("//ul[@class='note-list']/li")
        for article in articles:
            item['author'] = article.xpath('.//div[@class="info"]/a/text()').extract()[0]
            item['title'] = article.xpath('.//div[@class="content"]/a/text()').extract()[0]
            item['times'] = article.xpath('.//div[@class="info"]/span/@data-shared-at').extract()[0]
            url = article.xpath('.//div[@class="content"]/a/@href').extract()[0]
            item['url'] = 'http://www.jianshu.com' + url
            admire = article.xpath('.//div/div[2]/span[2]/text()').extract()
            item['admire'] = ''.join(admire)
            likes = article.xpath('.//div/div[2]/span[1]/text()').extract()
            item['likes'] = ''.join(likes)
            yield item