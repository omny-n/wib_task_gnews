import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('articles.csv', 'r') as f:
    reader = csv.reader(f)
    text = " ".join(cat[0] for cat in reader)

wordcloud = WordCloud(max_words=50, 
                      collocations = False, 
                      background_color = 'white').generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()