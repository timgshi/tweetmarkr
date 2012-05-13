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
	for tweet in collection.find().sort('created_at', 1).limit(1):
		tweets.append(tweet)
	
	returnMap = {}
	returnMap['Name'] = 'Tim'
	returnMap['Friend'] = 'Jason'
	return HttpResponse(json.dumps(tweets, default=json_util.default), mimetype="application/json")
