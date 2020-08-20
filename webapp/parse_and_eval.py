import nltk
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.data.path.insert(0, '/usr/local/share/nltk_data')

def get_and_parse(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article

def vader(article):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(article.text)
