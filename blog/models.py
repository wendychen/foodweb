from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')		# a link to another model
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_tate = models.DateTimeField(blank = True, null = True)

	def publish(self):
		sef.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title