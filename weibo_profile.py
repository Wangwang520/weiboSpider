# -*- coding:utf-8 -*-
import  requests,json
from lxml import etree
import os
from setting import spider_Request
from weibo_comments import Weibo_comments

class Weibo_profile:

    def __init__(self,id):
        self.id = id
        self.start_url = 'https://weibo.cn/'
        self.fist_url = self.start_url + id 
        self.file_name =  id +"/" + "profile-comments.json"
        self.spider_Request = spider_Request()
        if os.path.exists(id):
            if os.path.exists(self.file_name):
                os.remove(self.file_name)
        else:
            os.mkdir(id)

    
    def get_next_url(self,content):
        e_html=etree.HTML(content)
        next_url =  e_html.xpath('//*[@id="pagelist"]/form/div/a[text()="下页"]/@href')
    
        if len(next_url)!= 0:
            return self.start_url + next_url[0]
        else:
            return None

    def get_follows(self,content):
        e_html=etree.HTML(content)
        content = e_html.xpath("//div[contains(@id,'M')]//span[@class='ctt']")
        comment = e_html.xpath("//div[@class='c']//a[contains(text(),'评论')and not(contains( text(),'原文评论'))]/@href")

        
        
        list = []
        for i in range(len(content)):
            dic = {}
            try:
                dic["content"] = content[i].xpath('string(.)')
            except:
                dic["content"] = ''

            try:
                comment_url = comment[i]
            except:
                comment_url = ''
                     
            #dic["time"] = time[i]
            spider_comments = Weibo_comments( comment_url)
            comments = spider_comments.run()
            dic["comments"] = comments
            #print(comments)
            self.save_file(dic)
            #list.append(dic)
       
        return list
    
    def save_file(self,content_dic):
        content_json = json.dumps(content_dic,ensure_ascii=False)
        with open(self.file_name,"a",encoding="utf-8") as fp:
            fp.write(content_json)
            fp.write("\n")
                
       
        print("save ok !!!")


    def run(self):
        next_url = self.fist_url
        while next_url is not None:
            content_html = self.spider_Request.parse_url(next_url)
            self.get_follows(content_html)
            #self.save_file(content)
            next_url = self.get_next_url(content_html)
            
if __name__ == "__main__":
    #传入一个账户的id
    weibo = Weibo_profile('2803301701')
    weibo.run()
    

