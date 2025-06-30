import requests,re
from bs4 import BeautifulSoup

class NewsScraper:
    def __init__(self):
        self.base = "https://news.google.com"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'accept-language': "id,en-US;q=0.7,en;q=0.3",
            'referer': "https://news.google.com/",
            'x-same-domain': "1",
            'origin': "https://news.google.com",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
        }

    def directUrl(self,url):
        getdata = requests.get(url)
        getdata = BeautifulSoup(getdata.text,'html.parser').find('div',attrs={'data-n-a-id':True})

        payload = {
            'f.req': "[[[\"Fbv4je\",\"[\\\"garturlreq\\\",[[\\\"id\\\",\\\"ID\\\",[\\\"FINANCE_TOP_INDICES\\\",\\\"WEB_TEST_1_0_0\\\"],null,null,1,1,\\\"ID:id\\\",null,420,null,null,null,null,null,0,null,null,[1725841144,479645000]],\\\"id\\\",\\\"ID\\\",1,[2,3,4,8],1,0,\\\"775325150\\\",0,0,null,0],\\\""+getdata['data-n-a-id']+"\\\","+getdata['data-n-a-ts']+",\\\""+getdata['data-n-a-sg']+"\\\"]\",null,\"generic\"]]]"
        }


        response = requests.post(self.base+"/_/DotsSplashUi/data/batchexecute", data=payload, headers=self.headers)
        # print(response.text)
        url = re.search(r',\\"(.*?)\\",1', response.text).group(1)
        return url


    def getNews(self,day=1):
        search = requests.get(self.base+'/search?q=badan%20informasi%20geospasial%20when%3A'+str(day)+'d&hl=id&gl=ID&ceid=ID%3Aid')
        beauti = BeautifulSoup(search.text,'html.parser')
        artiker = beauti.find_all('article')
        news = []
        for x in artiker:
            href = x.find('a',href=True,jsname=False)
            title = href.text
            link = href['href']
            url = self.directUrl(self.base + link[1:])
            news.append((title, (url.split('?')[0] if '?' in url else url)))
        return news
# scraper = NewsScraper()
# print(scraper.getNews())

# class sentimenAnalys:
#     def __init__(self):
        