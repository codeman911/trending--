from twython import Twython
from collections import Counter

# supply the appropriate value
consumer_key = 'pHu1hsFsrt2HUlWVbNMO04x8b'
consumer_key_secret = '9oTsintSfGPrBXAWKl3Z5Z63kKsOuAyiRC5vQ7dklHfOCC6R3X'
ascess_key = '707978481699676160-F231vH2Jugm5e3qvv5Eu5ktCFaXb5l4'
ascess_key_secret = 'xGsteJxnroL8YOMCUtn4mc0LGraMSucuziIkFG1KP3F70'

#Create a Twython instance with your application keys and the users OAuth tokens

t = Twython(app_key=consumer_key,
            app_secret=consumer_key_secret,
            oauth_token=ascess_key,
            oauth_token_secret=ascess_key_secret)

#taking title of the blog post/ new article/ tweet from user
title=input("Enter the title \n")

#defining method tranding_hashtag for trending hashtags related to title
def trending_hashtag(title):
    search = t.search(q=title, count=100000)
    tweets = search['statuses']

    # converting list of tweets into string
    tweet = str(tweets)
    mystring ="".join(tweet)

    # fetching hashtags from tweet
    lst = list([word for word in mystring.split() if word.startswith('#')])

    #counting occurance of related hashtags in tweets
    count = Counter(lst)
    x = count.most_common()

    print("Trending hashtags for "+title, "are"+"\n")

    #getiing trending hashtags with number of occurance
    for i in x:
        print(i)

#callling method for  trending hashtags
trending_hashtag(title)



