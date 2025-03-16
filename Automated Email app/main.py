import yagmail
import pandas
from news import NewsFeed


df = pandas.read_excel("people1.xlsx")


for index, row in df.iterrows():
    news_feed = NewsFeed(row['interest'], "2023-08-14", "2023-08-15")

    email = yagmail.SMTP(user="fauzantahir660@gmail.com", password="nzqctvzcwynykkcj")
    email.send(to="fauzantahir110@gmail.com",
               subject=f"{row['interest']} latest news",
               contents=f"{row['name']} check the latest news on {row['interest']} today \n \n {news_feed.get()} ")