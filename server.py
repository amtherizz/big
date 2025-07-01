from flask import Flask, render_template,jsonify,request
from func import NewsScraper, NewsSentiment
app = Flask(__name__)

@app.route('/news')
def getNews():
    arg = request.args.get('when')
    if arg:
        when = arg
    else: when = 1
    init = NewsScraper()
    news = init.getNews(day=when)
    result = []
    pos = 0
    net = 0
    neg = 0
    for title, url in news:
        full_text, mentions = init.getMention(url)
        sentiment_title = NewsSentiment().analys(title)
        if sentiment_title=="positif":
            pos +=1
        elif sentiment_title=='negatif':
            neg +=1
        else:
            net +=1
        mention_data = []
        for x in mentions:
            sentimentM = NewsSentiment().analys(x)
            if sentimentM=="positif":
                pos +=1
            elif sentimentM=='negatif':
                neg +=1
            else:
                net +=1

            mention_data.append({
                "text": x,
                "sentiment": sentimentM 
            })

        result.append({
            'full_text':full_text,
            "title": title,
            "url": url,
            "sentiment_title": sentiment_title,
            "mentions": mention_data
        })
    result = {
        'negatif':neg,
        'positif':pos,
        'netral':net,
        'result':result
    }

    return jsonify(result)

@app.route('/monitor')
def monitor():
    return 

if __name__ == '__main__':
    app.run(debug=True)
