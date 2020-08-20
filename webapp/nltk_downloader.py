import nltk

directory = '/usr/local/share/nltk_data'

nltk.download('punkt', download_dir=directory)
nltk.download('stopwords', download_dir=directory)
nltk.download('vader_lexicon', download_dir=directory)