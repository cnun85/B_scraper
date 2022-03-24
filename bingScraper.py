import sys
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

import logging
import threading
import time
from lxml import html
import os




class BlogSpider(scrapy.Spider):
	name = 'blogspider'
	#term = 'enthec'
	
	def __init__(self, term=None):
		self.start_urls = ['https://www.bing.com/search?q={}&setlang=es'.format(term)]
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
	#print("holaaaaaaaaaaaaaaaaaaaaaaaaaa"+str(termino))
	#user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
	#start_urls = ['https://www.bing.com/search?q={}&setlang=es'.format(term)]


	def parse(self, response):
		resultado=[]
		for title in response.css('cite'):
			resultado.append(title.css('::text').get())
			yield {'title': title.css('::text').get()}

		# follow next page links
		if response.xpath("//a[@class='b_widePag sb_bp']/@href").get():
			for next_page in response.xpath("//a[@class='b_widePag sb_bp']/@href").get():
				yield response.follow(next_page, self.parse)
			
		print(resultado)
		
		with open('response.json', "w+") as outfile:
			for res in resultado:
				print(res)
				outfile.write(str(res))	
		
		#next_page = response.xpath("//a[@class='b_widePag sb_bp']/@href").get()
		
		#if next_page is not None:
		#	next_page = response.urljoin(next_page)
		#	yield scrapy.Request(next_page, callback=self.parse)

def thread_function(name,termino):
	logging.info("Thread %s: starting", name)
	time.sleep(2)
	
	runner.crawl(termino, term=name)
	
	logging.info("Thread %s: finishing", name)


if __name__ == "__main__":

	configure_logging()
	settings = get_project_settings()
	runner = CrawlerRunner(settings)
	threads = list()
	

	print(f"Arguments count: {len(sys.argv)}")
	for index, arg in enumerate(sys.argv):
		print(f"Argument {index:>6}: {arg}")
		if index!=0:
			if arg=='test':
				term='filetype:pdf test'
			else:
				term=arg
			
			logging.info("Main    : create and start thread %s.", arg)
			x = threading.Thread(target=thread_function, args=(term,BlogSpider))
			threads.append(x)
			x.start()
		
	for index, thread in enumerate(threads):
		logging.info("Main    : before joining thread %d.", index)
		thread.join()
		logging.info("Main    : thread %d done", index)
		
	#runner = CrawlerRunner(settings)
	#runner.crawl(BlogSpider)
	#runner.crawl(BlogSpider2)
	#d = runner.join()
	#d.addBoth(lambda _: reactor.stop())
	d = runner.join()

	d.addBoth(lambda _: reactor.stop())
	reactor.run()