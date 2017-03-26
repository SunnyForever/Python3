import urllib
import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        #伪装成浏览器访问，直接访问的话csdn会拒绝
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        #构造请求
        req = urllib.request.Request(url,headers=headers)
        #访问页面
        response = urllib.request.urlopen(req)
        #python3中urllib.read返回的是bytes对象，不是string,得把它转换成string对象，用bytes.decode方法
        return response.read().decode()
