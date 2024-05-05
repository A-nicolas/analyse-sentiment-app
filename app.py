import json
import tweepy
from fonctions import *

# Chargement du token pour l'API Twitter
with open("twitter_token.json") as file:
    data = json.load(file)

# Connexion à l'API de Twitter
client = tweepy.Client(bearer_token=data["bearer_token"])

# Requête Twitter
query = "Vinicius lang:fr -is:retweet -is:reply"
tweets_fr = client.search_recent_tweets(query=query, tweet_fields=['text'], max_results=10)

# Extraction des textes des tweets de la réponse
tweets_text = [tweet.text for tweet in tweets_fr.data]

# Nettoyage des tweets
cleaned_tweets = [clean_tweet(tweet) for tweet in tweets_text]
tokenized_tweets = [tokenize_tweet(tweet) for tweet in cleaned_tweets]
removed_stopwords = [remove_stopwords(tokens) for tokens in tokenized_tweets]

print("Nettoyage : \n")
print(cleaned_tweets)

print("\nDiviser les mots :\n")
print(tokenized_tweets)

print("\nSuppression des mots inutiles :\n")
print(removed_stopwords)


# Appel de la fonction pour sauvegarder les résultats
save_to_csv(tweets_text, removed_stopwords, 'tweets_removed_stopwords.csv')