import requests,re
from bs4 import BeautifulSoup
from textblob import TextBlob
from googletrans import Translator
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
        try:
            raw = requests.get(url).text
            getdata = BeautifulSoup(raw,'html.parser').find('div',attrs={'data-n-a-id':True})

            payload = {
                'f.req': "[[[\"Fbv4je\",\"[\\\"garturlreq\\\",[[\\\"id\\\",\\\"ID\\\",[\\\"FINANCE_TOP_INDICES\\\",\\\"WEB_TEST_1_0_0\\\"],null,null,1,1,\\\"ID:id\\\",null,420,null,null,null,null,null,0,null,null,[1725841144,479645000]],\\\"id\\\",\\\"ID\\\",1,[2,3,4,8],1,0,\\\"775325150\\\",0,0,null,0],\\\""+getdata['data-n-a-id']+"\\\","+getdata['data-n-a-ts']+",\\\""+getdata['data-n-a-sg']+"\\\"]\",null,\"generic\"]]]"
            }
            response = requests.post(self.base+"/_/DotsSplashUi/data/batchexecute", data=payload, headers=self.headers)
            # print(response.text)
            url = re.search(r',\\"(.*?)\\",1', response.text).group(1)
            return url
        except Exception as e:
            print((str(e)+' '+raw))
            return(str(e)+' '+raw)


    def getNews(self,day=1):
        search = requests.get(self.base+'/search?q=badan%20informasi%20geospasial%20when%3A'+str(day)+'d&hl=id&gl=ID&ceid=ID%3Aid')
        beauti = BeautifulSoup(search.text,'html.parser')
        artiker = beauti.find_all('article')
        news = []
        for x in artiker:
            href = x.find('a',href=True,jsname=False)
            title = href.text
            link = href['href']
            try:
                url = self.directUrl(self.base + link[1:])
            except:
                news.append((title, self.base + link[1:]))
            news.append((title, (url.split('?')[0] if '?' in url else url)))
        return news

    def _splitP(self,html):
        soup = BeautifulSoup(html,'html.parser')
        results = []

        for p in soup.find_all('p'):
            # Ambil hanya tag <p> yang parent-nya bukan <p>
            if not p.find_parent('p'):
                # Ambil semua <p> anak (nested), jika ada
                nested = p.find_all('p')
                # Kalau ada nested, ambil teks p luar tanpa nested, lalu nested-nya satu per satu
                if nested:
                    # Ambil teks p luar hanya sampai sebelum nested
                    outer_text = p.decode_contents().split('<p>')[0].strip()
                    if outer_text:
                        results.append(BeautifulSoup(outer_text, 'html.parser').get_text(strip=True))
                    for child in nested:
                        results.append(child.get_text(strip=True))
                else:
                    results.append(p.get_text(strip=True))
        return results
    
    def getMention(self,url):
        try:
            html = requests.get(url).text
            if 'Just a moment' in html:
                return 'cloudflare',[]
            split = self._splitP(html)
            return '\n'.join(split),[x.strip() for x in split if 'badan informasi geospasial' in x.lower() or "BIG" in x]
        except Exception as e:
            return 'error '+str(e),[]

class NewsSentiment:
    def __init__(self):
        self.translator = Translator()

    def analys(self, text):
        text = text.strip()
        translated = self.translator.translate(text, src='id', dest='en').text
        blob = TextBlob(translated)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            label = "positif"
        elif polarity < -0.1:
            label = "negatif"
        else:
            label = "netral"
        return {
            "label": label,
            "score": round(polarity, 3)
        }


class tempMail:
    base = 'http://129.158.196.208:8087/api/v1/email'
    def getMail(self):
        res = requests.get(self.base+'/add/dynamic/v2?pro=true').json()
        return res['mailAddress']
    def getBox(self,mail):
        res = requests.get(self.base+'/html-inbox/v2?name='+mail).json()
        for x in res:
            if x["subject"] =="Your verification code":
                code =  re.search(r'>(\d{6})<',x["content"]).group(1)
                return code
# scraper = NewsScraper()
# print(scraper.getMention('https://www.tempo.co/politik/badan-informasi-geospasial-pastikan-4-nama-pulau-aceh-tetap-sama-1825484'))

# class sentimenAnalys:
#     def __init__(self):
        