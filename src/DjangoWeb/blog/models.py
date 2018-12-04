"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=4000)
    content = models.TextField()
    status = models.PositiveSmallIntegerField()
    url = models.CharField(max_length=200, default=None, blank=True, null=True)
    tag = models.CharField(max_length=40, default=None, blank=True, null=True)
    order = models.FloatField(default=0)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200, default=None, blank=True, null=True)
    created_date = models.DateTimeField('date created')
    last_updated_date = models.DateTimeField('date updated')
    isdeleted = models.BooleanField()
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=200, default=None, blank=True, null=True)
    email = models.CharField(max_length=200, default=None, blank=True, null=True)
    status = models.PositiveSmallIntegerField()
    order = models.FloatField(default=0)
    pub_date = models.DateTimeField('date published')
    created_date = models.DateTimeField('date created')
    last_updated_date = models.DateTimeField('date updated')
    isdeleted = models.BooleanField()

    def __str__(self):
        if len(self.content) > 50:
            return self.content[:50] + " ..."
        self.content

    def __unicode__(self):
        return self.content
