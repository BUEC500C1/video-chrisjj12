import keys
import tweepy
import wget
from PIL import Image, ImageDraw, ImageFont
import os
import io
import time

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_secret)

api = tweepy.API(auth)

#status = api.get_status(id="realmadrid", tweet_mode="extended")
public_tweets = api.home_timeline()
    
media_files = set()
texts = []
j = 0
for status in public_tweets:
    print(status.text)
    texts.append(status.text)
    media = status.entities.get('media', [])


    img = Image.new('RGB', (1000, 500), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 15)
    d.text((10,10), status.text, fill=(255,255,0), font = font)
    tmp_name2 = 'tweet' + str(j) + '.png'
    #print(tmp_name2)
    #img = Image.open(img)
    img.save(tmp_name2)
    j = j + 1
    #print(j)
    
    if(len(media) > 0):
        temp = wget.download(media[0]['media_url'])
        tmp_name = 'tweet' + str(j) + '.png'
        #print(tmp_name)
        im1 = Image.open(temp)
        im1.save(tmp_name)
        #media_files.add(media[0]['media_url'])
        j = j + 1
        

print(j)
time.sleep(5)
pid = os.getpid()
os.system('ffmpeg -framerate 0.5 -i '+'tweet'+'%d.png video'+str(pid)+'.avi')

   


