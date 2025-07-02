from flask import Flask, request, jsonify, Response
import csv
import io
from func import NewsScraper, NewsSentiment

app = Flask(__name__)

@app.route('/news')
def getNews():
    arg = request.args.get('when')
    type_ = request.args.get('type', 'json')

    when = int(arg) if arg else 1

    init = NewsScraper()
    news = init.getNews(day=when)

    pos, net, neg = 0, 0, 0
    result = []

    for title, url in news:
        full_text, mentions = init.getMention(url)
        sentiment_title = NewsSentiment().analys(title)

        if sentiment_title['label'] == "positif":
            pos += 1
        elif sentiment_title['label'] == "negatif":
            neg += 1
        else:
            net += 1

        mention_data = []
        for x in mentions:
            sentimentM = NewsSentiment().analys(x)
            if sentimentM['label'] == "positif":
                pos += 1
            elif sentimentM['label'] == "negatif":
                neg += 1
            else:
                net += 1

            mention_data.append({
                "text": x,
                "sentiment": sentimentM['label']
            })

        result.append({
            "title_text": title,
            "title_sentiment": sentiment_title['label'],
            "url": url,
            "full_text": full_text,
            "mentions": mention_data
        })

    if type_.lower() == "csv":
        # Buat CSV dari result
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Title", "Title Sentiment", "URL", "Full Text", "Mention Text", "Mention Sentiment"])

        for item in result:
            if not item['mentions']:  # Kalau tidak ada mention, tetap tulis 1 baris
                writer.writerow([
                    item["title_text"],
                    item["title_sentiment"],
                    item["url"],
                    item["full_text"],
                    "", ""
                ])
            else:
                for mention in item['mentions']:
                    writer.writerow([
                        item["title_text"],
                        item["title_sentiment"],
                        item["url"],
                        item["full_text"],
                        mention["text"],
                        mention["sentiment"]
                    ])

        csv_data = output.getvalue()
        output.close()

        return Response(
            csv_data,
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=news_sentiment.csv"}
        )
    
    # Default: JSON response
    return jsonify({
        "positif": pos,
        "negatif": neg,
        "netral": net,
        "result": result
    })


@app.route('/monitor')
def monitor():
    return 

if __name__ == '__main__':
    app.run(debug=True)
