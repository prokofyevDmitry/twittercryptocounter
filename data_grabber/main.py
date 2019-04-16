import tweepy
import time
from requests import sessions

# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def __init__(self, **kwargs):
        super(**kwargs)
        self.period_start = 0
        self.period_size = 30

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    auth = tweepy.OAuthHandler("hiK6NyqC8IxsoyDHsIrrAEHdS", "GMJuUdhIFIUS9taxAyEhMZyBCjdsgHU5txPiP5HQl0DPcD5zp0")
    auth.set_access_token("4233472163-uWsLlkYzpfEC9R5QZAL6ENzfvNn8pvhwDpa0gJI",
                          "CzrZf7e3p5uRYwwmQP7GIEqhzj93CUGqCc5XXedXkbVT0")
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['btc', 'eth'])
    print("hello")
    time.sleep(100)
