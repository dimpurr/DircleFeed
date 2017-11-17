from django.db import models

class RSSList(models.Model):
	# core
	list_slug = models.SlugField(max_length=200, unique=True, primary_key=True)
	list_title = models.CharField(max_length=200)
	# timestamps
	create_date = models.DateTimeField('create date')
	last_modified_date = models.DateTimeField('last modified date')
	# tools
	def __str__(self):
		return self.list_title

class RSSListSource(models.Model):
	# core
	source_title = models.CharField(max_length=200)
	url = models.URLField(max_length=200)
	# relations
	from_list = models.ForeignKey(RSSList, on_delete=models.CASCADE)
	# timestamps
	create_date = models.DateTimeField('create date')
	# tools
	def __str__(self):
		return self.source_title