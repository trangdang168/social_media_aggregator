import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup  as  BSoup
from facebook_scraper import get_posts
from django.http import HttpResponseRedirect

from news.models import Headline

requests.packages.urllib3.disable_warnings()


def news_list(request):
	headlines = Headline.objects.all()
	context = {
		'object_list': headlines,
	}
	return render(request, "news/home.html", context)

def scrape(request):

	saved_posts = Headline.objects.all()

	# facebook	
	face_book_pages = ["ChrisBrecheensWritingAboutWriting", "Parapenquyenchinh"]
	for page in face_book_pages:
		facebook_posts = get_posts(page, pages=3)
		for post in facebook_posts:
			link = post['post_url']
			if link in saved_posts:
				continue

			image_src = post['image']
			title = post['username']
			new_headline = Headline()
			new_headline.title = title
			new_headline.url = link
			if image_src:
				new_headline.image = image_src
			else:
				new_headline.image = "https://png.pngtree.com/thumb_back/fh260/background/20200821/pngtree-sky-blue-solid-color-background-wallpaper-image_396578.jpg"
			new_headline.description = post['post_text']
			new_headline.date_posted = post['time']
			new_headline.id = link
			new_headline.save()

	# reddit
	return redirect("../")

def manage(request):
	# should turn up a page with a form
	pass



