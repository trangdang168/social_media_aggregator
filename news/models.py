from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Scrape data coming from websites
# The posts will contain images, urls and titles

class Headline(models.Model):
	title = models.CharField(max_length=200)
	image = models.URLField(max_length=200, null=True, blank=True)
	url = models.TextField(primary_key=True)
	date_posted = models.DateField()
	description = models.TextField(default='')
	# TODO check including more users
	# users = models.ManyToManyField(User)

	def __str__(self):
		return self.title

#TODO add a new model to save links we take from in the data base
PLATFORM_CHOICES = (
	('fb', 'facebook'), 
	('reddit', 'reddit') 
)
class Webpage(models.Model):
	url = models.URLField(primary_key=True)
	platform =  models.CharField(max_length=50, choices=PLATFORM_CHOICES)
	# users = models.ManyToManyField(User)

	def __str__(self):
		return self.url


