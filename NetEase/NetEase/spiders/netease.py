# -*- coding: utf-8 -*-
import scrapy
from NetEase.items import NeteaseItem

class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['163.com']
    start_urls = ['http://hr.163.com/position/list.do?currentPage=1']

    def parse(self, response):

    	node_lists=response.xpath("//*[@class='position-tb']/tbody/tr")

    	for node in node_lists:

    		item=NeteaseItem()

    		if node.xpath("./td[2]"):
    			item['positionName']=node.xpath("./td[1]/a/text()").extract()[0]
    			item['positionLink']="http://hr.163.com"+node.xpath("./td[1]/a/@href").extract()[0]
    			item['positionType']=node.xpath("./td[2]/text()").extract()[0]
    			item['workType']=node.xpath("./td[3]/text()").extract()[0]
    			item['workLocation']=node.xpath("./td[4]/text()").extract()[0]
    			item['positionNumber']=''.join(node.xpath("./td[5]/text()").extract()).strip()
    			item['publishTime']=node.xpath("./td[6]/text()").extract()[0]

    			yield item

    	if ''.join(response.xpath("/html/body/div[2]/div/div[2]/div/div/a[9]/@class").extract()) !='disabled':
    		url=response.xpath("/html/body/div[2]/div/div[2]/div/div/a[9]/@href").extract()[0]
    		yield scrapy.Request("http://hr.163.com/position/list.do"+url,callback=self.parse)









#//*[@id="position-table-45927"]/tbody/tr[23]


#/html/body/div[2]/div/div[2]/div/div/a[9] 
#/html/body/div[2]/div/div[2]/div/div/a[1]