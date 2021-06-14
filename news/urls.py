from django.urls import path
from news.views import scrape, news_list, manage

urlpatterns = [
	path('scrape/', scrape, name="scrape"),
	path('', news_list, name="acc-home"),
	path('manage/', manage, name="manage"),
]