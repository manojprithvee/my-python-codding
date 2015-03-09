import tweepy
import json

ckey = 'iYpcvZA2wHNXNxXQawdO40XcZ' #supply the appropriate value
csecret = 'EsESAMjtUNfIlmfeOOMJERK7bjjn3sP9B1QPRa7Wfrv7rtmFQu' 
atoken = '379887843-e2ZDlyIanxmU4Gpm51c2KneMzGxD4jtFGpKzgvte'
asecret = 'KNmLE1qlFRY2YdG7qgz2hIwBKFOtTl0rO5VxJTGAsjeXW'

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)
f=open('tweet.json','a')
m={}
f.write('{"Tweets":[')
for tweet in tweepy.Cursor(api.search, q=('cwc15')).items():
	print m
	m={}
	m['Name']=str(tweet.author.name.encode('utf8'))
	m['Screen_name']=str(tweet.author.screen_name.encode('utf8'))
	m['Created_at']=str(tweet.created_at)
	m['Tweet']=str(tweet.text.encode('utf8'))
	m['Retweeted']=str(tweet.retweeted)
	m['Favorited']=str(tweet.favorited)
	m['Location']=str(tweet.user.location.encode('utf8'))
	m['Time_Zone']=str(tweet.user.time_zone)
	m['Geo']=str(tweet.geo)
	f.write(str(json.dumps(m))+",\n")
f.write("]}")
f.close()
