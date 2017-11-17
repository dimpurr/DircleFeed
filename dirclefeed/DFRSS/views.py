from django.shortcuts import render
from django.http import HttpResponse
from .models import RSSList, RSSListSource

def index(request):
	latest_rss_list = RSSList.objects.order_by('-create_date')[:5]
	json_latest_rss_list = ""
	for r in latest_rss_list:
		json_latest_rss_list += '''{ list_slug: "%(list_slug)s", list_title: "%(list_title)s" }, ''' % { "list_slug": r.list_slug, "list_title": r.list_title }
	json_output = '{ latest_rss_list: {' + json_latest_rss_list + '} }'
	return HttpResponse(json_output)

def user_view(request, user_id):
	return HttpResponse("You're looking at user %s." % user_id)

def list_view(request, list_name):
	return HttpResponse("You're looking at rss list %s." % list_name)