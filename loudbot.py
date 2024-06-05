import tweepy
import time

consumer_key = 'Coloque seu token'
consumer_secret = 'Coloque seu token'
access_token = 'Coloque seu token'
access_token_secret = 'Coloque seu token'

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