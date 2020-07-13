# -*- coding:utf-8 -*-
import  requests,json,os
from lxml import etree
from setting import spider_Request

#爬取微博的粉丝，传入微博的id号
class Weibo_fans:

    def __init__(self,id):
        self.id = id
        self.start_url = 'https://weibo.cn/'
        self.fist_url = self.start_url + id +'/fans'
        self.spider_Request = spider_Request()
        self.file_name =  id +"/" + "fans.json"

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
        follows_name = e_html.xpath("//table//td[2]//a[1]/text()")
        follows_id = e_html.xpath("//table//td[2]//a[1]/@href")
        #print(follows_name)
        
        list = []
        for i in range(len(follows_name)):
            dic = {}
            dic["name"] = follows_name[i]
            dic["id"] = follows_id[i].split('/')[-1]
            
            list.append(dic)
       
        return list
    
    def save_file(self,fans_list):
        
        with open(self.file_name,"a",encoding="utf-8") as fp:
            for fans in fans_list:
                fans_json = json.dumps(fans,ensure_ascii=False)
                fp.write(fans_json)
                fp.write(",\n")
        
        print("save ok !!!")


    def run(self):
        next_url = self.fist_url
        while next_url is not None:
            content = self.spider_Request.parse_url(next_url)
            follows = self.get_follows(content)
            self.save_file(follows)
            next_url = self.get_next_url(content)
        
        

if __name__ == "__main__":
    #传入一个账户的id
    weibo = Weibo_fans('2803301701')
    weibo.run()

