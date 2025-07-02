import requests,re
from datetime import datetime,timedelta
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
            # 'referer': "https://news.google.com/",
            'x-same-domain': "1",
            # 'origin': "https://news.google.com",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
        }

    def directUrl(self,url):
        try:
            raw = requests.get(url,headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "accept-language": "id,en-US;q=0.7,en;q=0.3",
                "accept-encoding": "gzip, deflate, br, zstd",
                "upgrade-insecure-requests": "1",
                "service-worker-navigation-preload": "true",
                "cookie": "OTZ=8146905_28_28__28_",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "priority": "u=2",
                "te": "trailers"
                }).text
            getdata = BeautifulSoup(raw,'html.parser').find('div',attrs={'data-n-a-id':True})

            payload = {
                'f.req': "[[[\"Fbv4je\",\"[\\\"garturlreq\\\",[[\\\"id\\\",\\\"ID\\\",[\\\"FINANCE_TOP_INDICES\\\",\\\"WEB_TEST_1_0_0\\\"],null,null,1,1,\\\"ID:id\\\",null,420,null,null,null,null,null,0,null,null,[1725841144,479645000]],\\\"id\\\",\\\"ID\\\",1,[2,3,4,8],1,0,\\\"775325150\\\",0,0,null,0],\\\""+getdata['data-n-a-id']+"\\\","+getdata['data-n-a-ts']+",\\\""+getdata['data-n-a-sg']+"\\\"]\",null,\"generic\"]]]"
            }
            response = requests.post(self.base+"/_/DotsSplashUi/data/batchexecute", data=payload, headers=self.headers)
            # print(response.text)
            url = re.search(r',\\"(.*?)\\",1', response.text).group(1)
            return url
        except Exception as e:
            # print((str(e)+' '+raw))
            # print(url)
            return url
        
    def getNews(self,_from=None,day=1,url=True):
        if _from:
            from_date = datetime.strptime(_from, '%Y/%m/%d')
            today = datetime.today()

            # Hitung selisih hari
            day = (today - from_date).days
        search = requests.get(self.base+'/search?q=badan%20informasi%20geospasial%20when%3A'+str(day)+'d&hl=id&gl=ID&ceid=ID%3Aid')
        beauti = BeautifulSoup(search.text,'html.parser')
        artiker = beauti.find_all('article')
        news = []
        for x in artiker:
            href = x.find('a',href=True,jsname=False)
            time = x.find('time',{'datetime':True}).get('datetime')
            time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
            time = time.strftime('%d/%m/%Y') 
            title = href.text
            link = href['href']
            if url:
                try:
                    url = self.directUrl(self.base + link[1:])
                except:
                    news.append((title, self.base + link[1:],time))
                news.append((title, (url.split('?')[0] if '?' in url else url),time))
            else:
                news.append(title)
        return news

    def _splitP(self,html):
        soup = BeautifulSoup(html,'html.parser')
        results = []

        for p in soup.find_all('p'):
            if not p.find_parent('p'):
                nested = p.find_all('p')
                if nested:
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
    def cnn(self,_from='2025/06/01',day=False):
        now = datetime.today()
        if day:
            _from = now - timedelta(days=day)

            _from = _from.strftime('%Y/%m/%d') 

        page = requests.get('https://www.cnnindonesia.com/api/v3/search?query=badan informasi geospasial&idtype=1&start=0&limit=30&fromdate='+_from+'&todate='+now.strftime('%Y/%m/%d'))
        # print(page.url)
        data = page.json()['data']
        # print(data)
        news = [ (x['strjudul'],x['url']) for x in data]
        return news
    
    def detik(self,_from,day=False):
        page = requests.get('https://www.detik.com/search/searchall?query=badan%20informasi%20geospasial&result_type=latest&fromdatex=25/06/2025&todatex=02/07/2025',headers=self.headers)
        beauti_page = BeautifulSoup(page.text,'html.parser').find_all('article')
        news = []
        for x in beauti_page:
            x = x.find('a',href=True)
            news.append((x['dtr-ttl'],x['href']))
        return news
    
    def kompas(self):
        page = requests.get('https://search.kompas.com/search?q=geospasial',headers=self.headers)
        b_page = BeautifulSoup(page.text,'html.parser').find_all('div',{'class':'articleItem'})
        news = []
        for x in b_page:
            title = x.find('h2').text
            url = x.find('a').get('href')
            # print(title,urls)
            news.append((title,url))
        return news



class NewsSentiment:
    def __init__(self):
        self.translator = Translator()
    def clean_text(self,text):
    # Ubah ke huruf kecil
        text = text.lower()
        
        # Hapus URL
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Hapus mention dan hashtag
        text = re.sub(r'@\w+|#\w+', '', text)
        
        # Hapus angka
        text = re.sub(r'\d+', '', text)
        
        # Hapus tanda baca
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Hapus whitespace berlebih
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Hapus stopwords
        words = text.split()
        # words = [word for word in words if word not in stop_words]
        
        return ' '.join(words)
    def analys(self, text):
        text = text.strip()
        text = self.clean_text(text)
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
    
    def analys2(self,text):
        pass


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
# print(scraper.cnn())
# print(scraper.getMention('https://www.tempo.co/politik/badan-informasi-geospasial-pastikan-4-nama-pulau-aceh-tetap-sama-1825484'))

# class sentimenAnalys:
#     def __init__(self):
        