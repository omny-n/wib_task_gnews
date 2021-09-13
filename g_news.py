from GoogleNews import GoogleNews
import csv
googlenews = GoogleNews(lang='en', region='US')
googlenews.set_period('30d')
googlenews.set_encode('utf-8')
googlenews.get_news('RUSSIA')

with open('articles1.csv', mode='w', encoding='UTF8', newline='') as f:
    fieldnames = ['title', 'desc', 'date', 'datetime', 'link', 'img', 'media', 'site']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    articles_list = googlenews.results()
    writer.writerows(articles_list)



