from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

ACCESS_TOKEN = '1011923027896950784-XADbxELP2NGD2gtxK2u7YnIqeLzp8e'
ACCESS_SECRET = 'QhRE61KYpKlcgCrXviLrJnK3wvKAa45gxOPLubAz6pPvI'
CONSUMER_KEY = 'gf4RSmZ6mTV5N8xO4cj4tKY23'
CONSUMER_SECRET = 'QLb301Nh190mAXuCTcK4IejmdOlxUV0p9DT9GpgTa3SvXKiEvE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,
compression=True)
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)
    
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status_code):
        if status_code == 420:
            return False

class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,compression=True)
    stream = Stream(auth, l)
    stream.filter(track=["LakeShow"])