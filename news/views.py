
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin

import requests
from bs4 import BeautifulSoup  as  BSoup
from facebook_scraper import get_posts
# import praw
from datetime import datetime, timedelta 

from news.models import Headline, Webpage
from news.forms import WebpageForm


# requests.packages.urllib3.disable_warnings()
DAYS_KEPT_POST = 10 # number of days the posts will be kept in the database

#@login_required
def news_list(request):
	"""
	Generate the newsfeed and the list of webpages the user is following based on 
	the current database.
	Also handle the removal of a current website.
	"""
	webpages = Webpage.objects.all()
	headlines = Headline.objects.all()
	context = {
		'object_list': headlines,
		'webpage_list': webpages,
	}

	# delete post when button is pressed
	if request.POST and 'delete_page' in request.POST:
		page_to_delete = request.POST['delete_page_url']
		Webpage.objects.get(url=page_to_delete).delete()

	return render(request, "news/home.html", context)

def scrape(request):
	"""
	Clean up the posts database and fetch the most current posts
	from the websites.
	Currently can only handle facebook
	"""

	saved_posts = Headline.objects.all()

	# everytime we scrape new posts, we delete old posts in headlines 
	old_posts = Headline.objects.filter(date_posted__gte=datetime.now()-timedelta(days=DAYS_KEPT_POST))
	for old_post in old_posts:
		old_post.delete()

	facebook_pages = Webpage.objects.filter(platform='fb')
	# issues with the reddit scrapping account

	for page in facebook_pages:
		page_id = page.url
		if page_id[-1]=="/":
			page_id = page_id[:-1]
		page_id = page_id.split("/")[-1]
		facebook_posts = get_posts(page_id, pages=3)
		for post in facebook_posts:
			link = post['post_url']
			image_src = post['image']
			title = post['username']
			new_headline = Headline()

			new_headline.title = title
			new_headline.url = link

			new_headline.image = image_src
			new_headline.description = post['post_text']
			new_headline.date_posted = post['time']
			new_headline.id = link

			if new_headline in saved_posts:
				continue
			new_headline.save()


	"""
	reddit = praw.Reddit(client_id='WlN5eTWA0QknHw', client_secret='9T5wUs71FRn2yyWkM7P-XXFvSJgaAQ', 
					user_agent='User-Agent: website:social_media_aggregator:v0.0.0 (by /u/SneezingFridge)', 
					redirect_uri="http://localhost:8080" )
	# haven't done reddit yet because of complex authentication
	reddit_pages = Webpage.objects.filter(platform='reddit')
	for page in reddit_pages:
		page_name = page.url
		if page_name[-1]=="/":
			page_name = page_name[:-1]
		page_name = page_name.split('/')[-1]
		posts = reddit.subreddit('MachineLearning').hot(limit=10)
		for post in posts:
			print(post.title)

		for post in posts:
			new_headline = Headline()
			new_headline.title = post.title
			new_headline.url = post.url
			new_headline.image = "https://upload.wikimedia.org/wikipedia/vi/thumb/b/b4/Reddit_logo.svg/1200px-Reddit_logo.svg.png"
			new_headline.description = post.selftext
			new_headline.date_posted = datetime.now()
			new_headline.id = link
			if new_headline in saved_posts:
				continue
			new_headline.save()
	"""
	return redirect("../")

def manage(request):
	"""
	Presents the user with a form to add more links to follow. 
	"""
	# should turn up a page with a form

	if request.POST and 'add_form' in request.POST:
		# if the form webpage is submitted
		
		form_p = WebpageForm(request.POST)
		if form_p.is_valid():
			form_p.save()
		
	elif request.POST and 'back_form' in request.POST:
		return redirect("../")

	else:
		form_p = WebpageForm()

	context = {
		"webpages": Webpage.objects.all(),
		"form": form_p,
	}

	return render(request, 'news/manage.html', context)

#class NewsListByUser(LoginRequiredMixin, View):
#
#	def get_queryset(self):
#		return Headline.objects.filter(newsreader=self.request.user)

