# -*- coding:utf-8 -*-
import random,requests,time
class spider_Request:

    def __init__(self):
        agent1 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
        agent2 = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
        agent3 = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
        agent4='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 '
        agent5='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
        
        
        self.Cookie = ''


        self.list_agent = [agent1, agent2, agent3,agent4,agent5]
        self.session = requests.session()

    #发送请求，获取响应  
    def parse_url(self,url):
        print(url) 
        time.sleep(0.5)
        agent = random.choice(self.list_agent)
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':agent ,
            'Cookie': self.Cookie,
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'

        }
        response = self.session.get(url,headers=self.headers) 
            #response.encoding = response.apparent_encoding
            #print(response.text)
        return response.content