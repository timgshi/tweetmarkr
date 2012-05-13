from django.http import HttpResponse
import json

def tweet(request):
	returnMap = {}
	returnMap['Name'] = 'Tim'
	return HttpResponse(json.dumps(returnMap), mimetype="application/json")
