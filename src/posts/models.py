from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import uuid

# Create your models here.

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length = 120)
	#slug = models.SlugField(unique=False, null=True)
	image = models.ImageField(upload_to=upload_location,
			 null=True, blank=True,
			 width_field="width_field",
			 height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=0)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id":self.id})
#		return "/posts/%s/" %(self.id)

	class Meta:
		ordering = ["-timestamp", "-updated"]


class Blog(models.Model):
	name = models.CharField(max_length=100)
	tag_line = models.TextField()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100)
	email = models.TextField()

	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.name

class Tags(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Entry(models.Model):
	blog = models.ForeignKey(Blog)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	author = models.ManyToManyField(Author)
	tags = models.ManyToManyField(Tags)
	n_comments = models.IntegerField()
	n_pingbacks = models.IntegerField()
	rating = models.IntegerField()


	def __unicode__(self):
		return self.headline

	def __str__(self):
		return self.headline













