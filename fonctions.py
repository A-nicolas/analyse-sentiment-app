import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv


# Nettoyage des tweets
def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)  # Supprimer les URL
    tweet = re.sub(r'@\w+', '', tweet)     # Supprimer les mentions
    tweet = re.sub(r'#\w+', '', tweet)     # Supprimer les hashtags
    tweet = re.sub(r'[^\w\s]', '', tweet)  # Supprimer les caractères spéciaux
    return tweet

# Tokenisation
def tokenize_tweet(tweet):
    return word_tokenize(tweet)

# Filtration des stop-words : mots inutiles
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('french'))
    return [token for token in tokens if token.lower() not in stop_words]

# Fonction pour sauvegarder les résultats au format CSV
def save_to_csv(tweets,removed_stopwords, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Tweet", "Removed Stopwords"])  # Écriture de l'en-tête
        for i in range(len(tweets)):
            writer.writerow([tweets[i], ' '.join(removed_stopwords[i])])  # Écriture du tweet et des stopwords supprimés


