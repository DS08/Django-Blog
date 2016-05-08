from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 120)
	image = models.FileField(null=True, blank=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = False, auto_now_add = True)
	timestamp = models.DateTimeField(auto_now = True,auto_now_add = False)

	def __unicode__(self):
		return self.title




	def get_absolute_url(self):
		return reverse("blog:detail",kwargs={"id":self.id})
		#return ("/blog/detail/"+str(self.id)+"/")