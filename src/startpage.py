#!/usr/bin/env python3
# coded by : Khaled Nassar @knassar702
# version : 1.0.0
# https://github.com/knassar702/startpage-parser

import requests
from bs4 import BeautifulSoup

class StartPage:
    def __init__(self):
        self.results = {} # {"Text":{"link":"http://google.com","Desctiopns":"blblalbal"}}
    def search(self,word,page=int(1)):
        page += 1
        for page_number in range(1,page): # number of search pages
            self.results[str(page_number)] = []
            """
            send request to startpage.com with search words and number of page
            """
            try:
                req = requests.get(f'https://www.startpage.com/do/search?q={word}&segment=startpage.brave&page={page_number}',headers={"User-agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}).content.decode()
                soup = BeautifulSoup(req, "html.parser")
                ancher = soup.find_all('div', {'class': "w-gl__result w-gl__desktop__result"}) # find div with "w-gl__result w-gl__desktop__result" class name
                """
                <div class="w-gl__result w-gl__desktop__result">
                <a href="LINK" class="w-gl__result-title result-link">LINK</a>
                <h3> TEXT</h3>
                <p class="w-gl__description">description</p> 
                """
                for i in ancher:
                    text = i.find('h3').contents[0]
                    link = i.find('a',{'class':'w-gl__result-title result-link'})['href']
                    description = i.find('p',{'class':'w-gl__description'}).contents[0]
                    self.results[str(page_number)].append({'title':text,'link':link,'description':description})
            except Exception as e:
                print(e)
            """           
s = StartPage()
s.search("Hello World")
print(s.results)
            """
        return self.results
