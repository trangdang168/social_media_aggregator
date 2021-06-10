
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

import requests
from bs4 import BeautifulSoup  as  BSoup
from facebook_scraper import get_posts

from news.models import Headline, Webpage
from news.forms import WebpageForm

# requests.packages.urllib3.disable_warnings()


def news_list(request):
	webpages = Webpage.objects.all()
	headlines = Headline.objects.all()
	context = {
		'object_list': headlines,
		'webpage_list': webpages,
	}

	# delete post when butten is pressed
	if request.POST and 'delete_page' in request.POST:
		# get the page url and delete the page
		page_to_delete = request.POST['delete_page_url']
		Webpage.objects.get(url=page_to_delete).delete()
	return render(request, "news/home.html", context)

def scrape(request):

	saved_posts = Headline.objects.all()
	facebook_pages = Webpage.objects.filter(platform='fb')

	for page in facebook_pages:
		page_id = page.url.split("/")[-1]
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

	# reddit
	return redirect("../")

def manage(request):
	# should turn up a page with a form

	if request.POST and 'form_type' in request.POST:

		# if the form webpage is submitted
		if request.POST.get("form_type") == 'add_form':
		
			form_p = WebpageForm(request.POST)
			if form_p.is_valid():
				form_p.save()
		return redirect("../")
	else:
		form_p = WebpageForm()

	context = {
		"webpages": Webpage.objects.all(),
		"form": form_p,
	}

	return render(request, 'news/manage.html', context)



