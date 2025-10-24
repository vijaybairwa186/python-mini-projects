# --> Build a News App Using APIs

import requests  

query = input("What type of news are you interested in today? ")
api = "dbe57b028aeb41e285a226a94865f7a7"

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)
data = r.json()

if data.get("status") != "ok":
    print("Error fetching news:", data.get("message", "Unknown error"))
else:
    articles = data.get("articles", [])
    if not articles:
        print("No articles found for your search.")
    else:
        for index, article in enumerate(articles, start=1):
            print(f"{index}. {article['title']}")
            print(article["url"])
            print("\n" + "*" * 40 + "\n")
