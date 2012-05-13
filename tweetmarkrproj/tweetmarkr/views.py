from django.http import HttpResponse
import json
import pymongo
from pymongo import Connection
from bson import json_util

def tweet(request):
	mongoConnection = Connection()
	db = mongoConnection.tweets
	collection = db.tweets
	tweets = []
	for tweet in collection.find().sort('created_at', -1).limit(5):
		tweets.append(tweet)
	
	returnMap = {}
	returnMap['tweets'] = tweets
	returnMap['count'] = len(tweets)
	return HttpResponse(json.dumps(returnMap, default=json_util.default), mimetype="application/json")
