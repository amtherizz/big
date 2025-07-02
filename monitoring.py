from func import NewsScraper

init = NewsScraper()

news = init.getNews()
for title,url,waktu in news:
    _,men = init.getMention(url)
    isiitu = " ".join(men)