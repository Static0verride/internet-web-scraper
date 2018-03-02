from BlackWidow import *

html = {"http://www.web.stanford.edu/class/cs221/"}
html = {"https://www.washingtonpost.com/news"}
my_header = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
username = ''
password = ''
domain = ''

link = html.pop()

my_spider = BlackWidow(link, my_header)

my_spider.go_spider_go()
