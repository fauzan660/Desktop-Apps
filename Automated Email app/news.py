from langdetect import detect
import requests
from pprint import pprint

class NewsFeed():
    api_key = "58c09a0d9a064c319751d0af44047322"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.to_date = to_date
        self.from_date = from_date
        self.language = language

    def get(self):
        url = f"https://newsapi.org/v2/everything?qInTitle={self.interest}&from={self.from_date}&to={self.to_date}&language={self.language}&apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        count = 1
        for article in articles:
            email_body += f"{count}) {article['title']}\n{article['url']}\n\n"
            count += 1


        return email_body


news_feed = NewsFeed(interest='nasa', from_date= '2023-08-14', to_date='2023-08-15', language="en")
print(news_feed.get())




