import feedparser

KEYWORDS = ["acquisition", "lawsuit", "breach"]
RSS_FEEDS = [
    "https://news.google.com/rss/search?q=company+news"
]

def check_news():
    alerts = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = entry.title.lower()
            if any(keyword in title for keyword in KEYWORDS):
                alerts.append(entry.title)
    return alerts

if __name__ == "__main__":
    results = check_news()
    for r in results:
        print("ALERT:", r)
