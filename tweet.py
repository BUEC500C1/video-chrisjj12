import keys
import tweepy
import wget
from PIL import Image, ImageDraw, ImageFont
import os
import io

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_secret)

api = tweepy.API(auth)

#status = api.get_status(id="realmadrid", tweet_mode="extended")
public_tweets = api.home_timeline()
    
media_files = set()
texts = []
i = 0
for status in public_tweets:
    #print(status.text)
    texts.append(status.text)
    media = status.entities.get('media', [])
    #texts.append(status.text)
    
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10), "hi", fill=(255,255,0))
     
    img.save('pil_text.png')


    
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
        


for media_file in media_files:
   temp = wget.download(media_file)
   tmp_name = 'pic' + str(i) + '.png'
   im1 = Image.open(temp)
   im1.save(tmp_name)
   i = i + 1

pid = os.getpid()
os.system('ffmpeg -framerate 0.5 -i '+'pic'+'%d.png video'+str(pid)+'.avi')

#ffmpeg -r 60 -f image2 -s 1920x1080 -i pic%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4
#convert text to image to make video pil
   


