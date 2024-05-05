import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Nettoyage des données
def clean_tweets(tweets):
    tweets = re.sub(r'http\S+', '', tweets)  # Supprimer les URL
    tweets = re.sub(r'@\w+', '', tweets)     # Supprimer les mentions
    tweets = re.sub(r'#\w+', '', tweets)     # Supprimer les hashtags
    tweets = re.sub(r'[^\w\s]', '', tweets)  # Supprimer les caractères spéciaux
    return tweets

# Tokenisation
def tokenize_tweets(tweets):
    return word_tokenize(tweets)

# Filtration des stop-words
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('french'))
    return [token for token in tokens if token.lower() not in stop_words]
