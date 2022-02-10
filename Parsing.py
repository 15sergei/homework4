# Парсинг. Веб страница https://www.expertcen.ru/article/ratings/luchshie-smartfoni-samsung.html
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

url = "https://www.expertcen.ru/article/ratings/luchshie-smartfoni-samsung.html"
page = requests.get(url).text
soup = BeautifulSoup(page, features="html.parser")
headline = soup.find('h1').get_text()
p_tags = soup.find_all('p')
p_tags_text = [tag.get_text().strip() for tag in p_tags]
sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
article_text = ' '.join(sentence_list)
summary = summarize(article_text, ratio=0.3)
print(f"Length of original article: {len(article_text)}")
print(f"Length of summary: {len(summary)}")
print(f"Headline: {headline}")
print(f"Article summary:\n{summary}")
