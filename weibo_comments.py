# -*- coding:utf-8 -*-
import  requests,json,os
from lxml import etree
from setting import spider_Request

#这个类用来爬取微博评论
#传入一条微博的评论链接，即可爬出所有
class Weibo_comments:
    def __init__(self,url):
        self.url = url
        self.start_url = 'https://weibo.cn'
        self.fist_url = self.url
        self.spider_Request = spider_Request()

        
    
   # def get_redict_url(self,content):
   #     e_html=etree.HTML(content)
   #     url_content = e_html.xpath('//meta[@http-equiv="refresh"]/@content')[0]
   #     print(url_content)
   #     redict_url = re.search(r'[a-zA-z]+://[^\s]*',url_content).group()    
   #     return redict_url.split("'")[0]
    
    #这个函数用来寻找评论页的下一页
    def get_next_url(self,content):
        e_html=etree.HTML(content)
        next_url =  e_html.xpath('//*[@id="pagelist"]/form/div/a[text()="下页"]/@href')
    
        if len(next_url)is  not  0:
            return self.start_url + next_url[0]
        else:
            return None

    #解析页面，返回一个列表
    def get_follows(self,content):
        e_html=etree.HTML(content)
        comment_div = e_html.xpath("//div[contains(@id,'C')]")

        list = []
        for i in range(len(comment_div)):
            dic = {}
            dic["author"] = comment_div[i].xpath("./a/text()")[0]
            dic["id"] = comment_div[i].xpath("./a/@href")[0].split("/")[-1]
            comment_span= comment_div[i].xpath(".//span[@class='ctt']")
            dic["content"] =comment_span[0].xpath("string(.)").strip()
            
            list.append(dic)
           
        return list
    
    #将数据保存到一个json文件
    def save_file(self,comments):
        with open("comments.json","a",encoding="utf-8") as fp:
            comment_json = json.dumps(comments,ensure_ascii=False)
            fp.write(comment_json)
            fp.write("\n")

    #爬虫的逻辑，返回一个包含所有评论的列表
    def run(self):
        comments = []
        next_url = self.fist_url
        while next_url is not None:
            content = self.spider_Request.parse_url(next_url)
            follows = self.get_follows(content)
            #self.save_file(follows)
            for f in follows:
                comments.append(f)
            next_url = self.get_next_url(content)
        
        return comments
        
        

if __name__ == "__main__":
    #传入一个微博的评论链接
    weibo = Weibo_comments('https://weibo.cn/comment/JarUH3iUO?uid=2803301701&rl=1#cmtfrm')
    weibo.run()

