import json
import simplejson as json
import csv

headers = ['INDEX', 'TIMESTAMP', 'TWEET', 'USER NAME', 'ID', 'USER LOCATION', 'USER DESCRIPTION', 'FOLLOWER COUNT', 'VERIFIED STATUS', 'FRIENDS COUNT', 'STATUSES COUNT', 'CREATION TIME', 'GEO ENABLED', 'LOCATION', 'REPLY COUNT', 'RETWEET COUNT', 'LIKE COUNT', 'HASHTAGS', 'USERS MENTIONED SCREENNAME', 'USERS MENTIONED NAME', 'USERS MENTIONED ID', 'RETWEETED', 'FAVORITED', 'LANGUAGE', 'SEARCHTAG']
x =1
content = {}

with open('datasettest.csv', 'a') as csvfile:
    csv.DictWriter(csvfile, fieldnames=headers).writeheader()
tweets_filename = 'greenbay2.txt'
tweets_file = open(tweets_filename, 'r')

for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            content['created_at'] = []
            content['text'] = []
            content['user'] = {}
            content['user']['name'] = []
            content['user']['screenname'] = []
            content['user']['location'] = []
            content['user']['description'] = []
            content['user']['follower_count'] = []
            content['user']['verified'] = []
            content['user']['friends_count'] = []
            content['user']['statuses_count'] = []
            content['user']['created_at'] = []
            content['user']['geo_enabled'] = []
            content['place'] = []
            content['reply_count'] = []
            content['retweet_count'] = []
            content['favorite_count'] = []
            content['entities'] = {}
            content['entities']['hashtags'] = {}
            content['entities']['hashtags']['text'] = []
            content['entities']['user_mentions'] = {}
            content['entities']['user_mentions']['screenname'] = []
            content['entities']['user_mentions']['name'] = [] 
            content['entities']['user_mentions']['id'] = []
            content['entities']['user_mentions']['id_str'] = []
            content['favorited'] = []
            content['retweeted'] = []
            content['lang'] = []
            content['searchtag'] = []
            content['created_at'].append(tweet['created_at'])
            content['text'].append(tweet['text'])
            content['user']['name'].append(tweet['user']['name'])
            content['user']['screenname'].append(tweet['user']['screen_name'])
            content['user']['location'].append(tweet['user']['location'])
            content['user']['description'].append(tweet['user']['description'])
            content['user']['follower_count'].append(tweet['user']['followers_count'])
            content['user']['verified'].append(tweet['user']['verified'])
            content['user']['friends_count'].append(tweet['user']['friends_count'])
            content['user']['statuses_count'].append(tweet['user']['statuses_count'])
            content['user']['created_at'].append(tweet['user']['created_at'])
            content['user']['geo_enabled'].append(tweet['user']['geo_enabled'])
            content['place'].append(tweet['place'])
            content['reply_count'].append(tweet['reply_count'])
            content['retweet_count'].append(tweet['retweet_count'])
            content['favorite_count'].append(tweet['favorite_count'])
            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
            content['entities']['hashtags']['text'].append(hashtags)
            screenname = []
            name = []
            ids = []
            id_str = [] 
            for user in tweet['entities']['user_mentions']:
                screenname.append(user['screenname'])
                name.append(user['name'])
                ids.append(user['id'])
                id_str.append(user['id_str'])
            content['entities']['user_mentions']['screenname'].append(screenname)
            content['entities']['user_mentions']['name'].append(name)
            content['entities']['user_mentions']['id'].append(ids)
            content['entities']['user_mentions']['id_str'].append(id_str)
            content['retweeted'].append(tweet['retweeted'])
            content['favorited'].append(tweet['favorited'])
            content['lang'].append(tweet['lang'])
            content['searchtag'].append('GBvsKC')
  
            
            # print(content)
            
            with open('datasettest.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet['created_at'], 'TWEET':tweet['text'], 'USER NAME':tweet['user']['name'], 'ID':tweet['user']['screen_name'], 'USER LOCATION':tweet['user']['location'], 'USER DESCRIPTION':tweet['user']['description'], 'FOLLOWER COUNT':tweet['user']['followers_count'], 'VERIFIED STATUS':tweet['user']['verified'], 'FRIENDS COUNT':tweet['user']['friends_count'], 'STATUSES COUNT':tweet['user']['statuses_count'], 'CREATION TIME':tweet['user']['created_at'], 'GEO ENABLED':tweet['user']['geo_enabled'], 'LOCATION':tweet['place'], 'REPLY COUNT':tweet['reply_count'],'RETWEET COUNT':tweet['retweet_count'], 'LIKE COUNT':tweet['favorite_count'], 'HASHTAGS':tweet['entities']['hashtags']['text'], 'USERS MENTIONED SCREENNAME':screenname , 'USERS MENTIONED NAME':name , 'USERS MENTIONED ID':id_str, 'RETWEETED':tweet['retweeted'], 'FAVORITED':tweet['favorited'], 'LANGUAGE':tweet['lang'], 'SEARCHTAG':content['searchtag']}
                writer.writerow(row)
                x = x+1
                hashtags=[]
                for hashtag in tweet['entities']['hashtags']:
                    hashtags.append(hashtag['text'])
            with open('datajsontest.txt', 'a') as outfile:
                json.dump(content, outfile)
                print(content)
            
    except:
        continue

with open('datajson.txt', 'a') as file:
    json.dumps(content)