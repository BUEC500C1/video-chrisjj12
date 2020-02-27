import keys
import tweepy
import wget
from PIL import Image

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_secret)

api = tweepy.API(auth)

#status = api.get_status(id="realmadrid", tweet_mode="extended")
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
media_files = set()
for status in public_tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
        
i = 0
for media_file in media_files:
   temp = wget.download(media_file)
   tmp_name = 'pic' + str(i) + '.png'
   im1 = Image.open(temp)
   im1.save(tmp_name)
   i = i + 1

#convert text to image to make video pil
   


