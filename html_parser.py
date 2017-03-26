import re
import urllib
from urllib.parse import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a', href=re.compile(r'/item/.*?'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    #获取标题、摘要
    def _get_new_data(self, page_url, soup):
        #新建字典
        res_data = {}
        #url
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>获得标题标签
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        print(str(title_node.get_text()))
        res_data['title'] = str(title_node.get_text())
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return None

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
