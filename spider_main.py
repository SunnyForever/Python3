#coding:utf8
import time, datetime

from maya_Spider import url_manager, html_downloader, html_parser, html_outputer


class Spider_Main(object):
    #初始化操作
    def __init__(self):
        #设置url管理器
        self.urls = url_manager.UrlManager()
        #设置HTML下载器
        self.downloader = html_downloader.HtmlDownloader()
        #设置HTML解析器
        self.parser = html_parser.HtmlParser()
        #设置HTML输出器
        self.outputer = html_outputer.HtmlOutputer()

    #爬虫调度程序
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break

                count = count + 1
            except:
                print('craw failed')

        self.outputer.output_html()

if __name__ == '__main__':
    #设置爬虫入口
    root_url = 'http://baike.baidu.com/view/21087.htm'
    #开始时间
    print('开始计时..............')
    start_time = datetime.datetime.now()
    obj_spider = Spider_Main()
    obj_spider.craw(root_url)
    #结束时间
    end_time = datetime.datetime.now()
    print('总用时：%ds'% (end_time - start_time).seconds)
