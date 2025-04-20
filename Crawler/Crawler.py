#!/usr/bin/env python
import requests
import re
import urllib.parse

class Scanner:
    def __init__(self,url):
        self.session=requests.Session()
        self.target_url=url
        self.target_links=[]

    def extract_links(self,url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', str(response.content))

    def crawl(self,url=None):
        if url==None:
            url=self.target_url
        href_links = self.extract_links(url)
        for link in href_links:

            link = urllib.parse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]
            
            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

target_url="http://192.168.56.130/dvwa/"
data_dict={"username":"admin","password":"password","Login":"submit"}
vul_scanner=Scanner(target_url)
vul_scanner.session.post("http://192.168.56.130/dvwa/login.php",data=data_dict)
vul_scanner.crawl()