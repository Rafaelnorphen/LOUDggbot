import tweepy
import time

consumer_key = 'n1Lz1rmL5Xyz5ASxeBbV8VoIv'
consumer_secret = 'IiItxiA6853E3Zh4eGS0k5gliIbja6yrObjzFMEMdJuODdK9xa'
access_token = '1795526040875393024-Pj8r02ati8yo4zrA9zue7f6oMnTU1B'
access_token_secret = 'aMta9p4QOhVPJ6KwSBFPzEGyQw9WSiYhXywMIWtncyny8'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def check_mentions(api, keywords, since_id):
    print("Procurando menções...")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if any(keyword in tweet.text.lower() for keyword in keywords):
            print(f"Respondendo ao tweet {tweet.id} de {tweet.user.name}")
            api.update_status(
                status="Olá! Obrigado por me mencionar!",
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
    return new_since_id

def main():
    since_id = 1
    while True:
        since_id = check_mentions(api, ["@LOUDggbot"], since_id)
        time.sleep(15)  # Verifica menções a cada 15 segundos

if __name__ == "__main__":
    main()