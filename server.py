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


        mention_data = []
        for x in mentions:
            sentimentM = NewsSentiment().analys(x)
            # if sentimentM['label'] == "positif":
            #     pos += 1
            # elif sentimentM['label'] == "negatif":
            #     neg += 1
            # else:
            #     net += 1

            mention_data.append({
                "text": x,
                "sentiment": sentimentM['label']
            })
        sentiment_all = NewsSentiment().analys(' '.join([title,' '.join(mentions)]))

        if sentiment_all['label'] == "positif":
            pos += 1
        elif sentiment_all['label'] == "negatif":
            neg += 1
        else:
            net += 1
        result.append({
            "title_text": title,
            "title_sentiment": sentiment_title['label'],
            "all_sentiment":sentiment_all,
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
    return """
    <html>
    <head>
        <title>Dashboard Monitoring Sentiment</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { font-family: Arial; margin: 40px; }
            #chart-container { width: 700px; margin-bottom: 40px; }
            .info-box, .mention-box {
                border: 1px solid #ccc;
                padding: 10px;
                background: #f9f9f9;
                margin-top: 10px;
                display: none;
                max-width: 600px;
            }
            .title-item {
                margin: 4px 0;
                cursor: pointer;
                color: blue;
            }
            .mention-item {
                font-size: 14px;
                margin-left: 10px;
            }
        </style>
    </head>
    <body>
        <h2>Sentiment Analysis Dashboard</h2>
        <div id="chart-container">
            <canvas id="sentimentChart"></canvas>
        </div>

        <div class="info-box" id="titleBox">
            <strong>Judul Berita:</strong>
            <div id="titleList"></div>
        </div>

        <div class="mention-box" id="mentionBox">
            <strong>Mentions:</strong>
            <div id="mentionList"></div>
        </div>

        <script>
            let fullData = null;

            async function fetchData() {
                const response = await fetch('/news');
                const data = await response.json();
                fullData = data.result;

                const ctx = document.getElementById('sentimentChart').getContext('2d');
                const chart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['Positif', 'Netral', 'Negatif'],
                        datasets: [{
                            label: 'Jumlah Sentimen',
                            data: [data.positif, data.netral, data.negatif],
                            backgroundColor: ['#4caf50', '#ffeb3b', '#f44336']
                        }]
                    },
                    options: {
                        responsive: true,
                        onClick: (evt, elements) => {
                            if (!elements.length) return;
                            const index = elements[0].index;
                            const label = chart.data.labels[index];
                            showTitles(label.toLowerCase());
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: 'Distribusi Sentimen Berita'
                            },
                            legend: { display: false }
                        }
                    }
                });
            }

            function showTitles(sentiment) {
                const titleBox = document.getElementById("titleBox");
                const titleList = document.getElementById("titleList");
                const mentionBox = document.getElementById("mentionBox");
                const mentionList = document.getElementById("mentionList");

                titleList.innerHTML = "";
                mentionBox.style.display = "none";
                mentionList.innerHTML = "";

                const filtered = fullData.filter(item => item.title_sentiment === sentiment);
                filtered.forEach((item, idx) => {
                    const div = document.createElement("div");
                    div.className = "title-item";
                    div.innerHTML = `<a href="${item.url}" target="_blank">${item.title_text}</a>`;
                    div.dataset.index = idx;
                    div.onclick = () => showMentions(filtered[div.dataset.index].mentions);
                    titleList.appendChild(div);
                });

                titleBox.style.display = "block";
            }

            function showMentions(mentions) {
                const mentionBox = document.getElementById("mentionBox");
                const mentionList = document.getElementById("mentionList");
                mentionList.innerHTML = "";

                if (!mentions || mentions.length === 0) {
                    mentionList.innerHTML = "<i>Tidak ada mention</i>";
                } else {
                    mentions.forEach(m => {
                        const div = document.createElement("div");
                        div.className = "mention-item";
                        div.innerHTML = `• ${m.text} <b>(${m.sentiment})</b>`;
                        mentionList.appendChild(div);
                    });
                }

                mentionBox.style.display = "block";
            }

            fetchData();
        </script>
    </body>
    </html>
    """



if __name__ == '__main__':
    app.run(debug=True)
