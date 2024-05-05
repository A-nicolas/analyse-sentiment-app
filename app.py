# import json

# with open("./twitter_token.json") as file:
#     data = json.load(file)

# print(data["bearer_token"])

from fonctions import *

tweets = """ Il ressemble au footballeur VINICIUS » Ptdrrrrrrrrr 
SPORT 🔵 Real Madrid : « Vinicius est à un niveau très élevé », prévient Rodrygo ! /

👉 Lire l'article :  https://t.co/FbBrEoW1br https://t.co/C6lNz8ov5D

Oui j’ai bien aimé comment le Barça a arrêté le Real et Vinicius en 3 rencontres cette saison 🤣 https://t.co/3EyZJUTCnz

Supercoupe d’Espagne, le premier but de Vinicius est littéralement le même. Le défenseur était l’Abruti Suprême Araujo. Quel Barça ? https://t.co/daCsJFgbKI

Je pense que vous vous rendez pas compte à QUEL POINT Vinicius est devenu fort mdrrrrr sa palette offensive est encore plus impressionnante que l’année dernière c’est de la folie https://t.co/bImhlO2dAv

Il peut gagner la LDC même 50x c’est une dinguerie de mettre Neymar et Vinicius dans la même phrase https://t.co/Au1OjGnCDJ

Vinicius vs Bayern🤩

Motm performance https://t.co/7GoajEpWXl

Vinicius 🇧🇷 est le Brésilien le plus décisif dans l’histoire de la Ligue des Champions. 

⚽️ | 31 buts et passes décisives
👕 | 33 matchs
⏳ | 3 dernières années

NIVEAU BALLON D’OR. 🥶 https://t.co/8Aswp3LWOs

La qualité de la passe de Toni Kroos à Vinicius #BAYRMA révèle l'importance des mathématiques dans la vie.

Un jour il va falloir parler de la saison de vinicius jr 🇧🇷
21 but et 11 passe décisives cette saison
31 G/A https://t.co/HlSiLp5Vsw
"""

cleaned_tweets = clean_tweets(tweets)
tokenized_tweets = tokenize_tweets(cleaned_tweets)
removed_stopwords = remove_stopwords(tokenized_tweets)

print("Nettoyage : \n")
print(cleaned_tweets)

print("\nDiviser les mots :\n")
print(tokenized_tweets)

print("\nSuppression des mots inutiles :\n")
print(removed_stopwords)