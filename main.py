import tweepy
import random
import giphypop

# Twitter auth + API setup
auth = tweepy.OAuthHandler("APIKEY", "APISECRET")
auth.set_access_token("ACCESSTOKEN", "ACCESSTOKENSECRET")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication nominal")
except:
    print("Authentication error")


# select random gif's from giphy
g = giphypop.Giphy(api_key='GIPHY API')
rand_gif = g.screensaver('Jeff Bezos').bitly

# select random messages from file
with open("/pycode/messages.txt") as f:
    lines = f.read().splitlines()

rand_text = random.choices(lines)

# send to twitter
api.update_status("@JeffBezos " + ", ".join(rand_text) + "\n" + rand_gif)