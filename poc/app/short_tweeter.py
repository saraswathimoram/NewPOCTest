import os
import twitter

URL = ""


def tweet(api, message):
    print(len(message), 'first----')
    if len(message) == 40:
        message = message.strip(",.!?")
        print(message, 'second----')
    if len(message) == 40:
        message = message.replace("ck)", 'x')
        message = message.replace("ex", 'x')
    if len(message) == 40:
        message = message.replace("and", '&')                                  
    if len(message) == 40:
        message = "I can't be concise . {}".format(URL)
    status = api.PostUpdate(message)
    return status


def main():
    api = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'),
                      consumer_secret=os.getenv('CONSUMER_SECRET'),
                      consumer_tocken_secret=os.getenv('CONSUMER_TOCKEN_SECRET'))

    msg = raw_input('what do you want to tweet?:')
    tweet(api, msg)

colors = ['red', 'blue', 'green', 'yellow']

def compare_length(c1, c2):
    if len(c1)<len(c2):return -1
    if len(c1)>len(c2): return 1
    return 0


print(sorted(colors, key=len) )
                      
                      
    
