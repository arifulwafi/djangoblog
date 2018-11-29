"""
Definition of views.
"""

from blog.models import BlogPost
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from os import path

import json

class BlogPostListView(ListView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['title'] = 'BlogPosts'
        context['year'] = datetime.now().year
        return context

class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)
        context['title'] = 'BlogPost'
        context['year'] = datetime.now().year
        return context

class AuthorBlogPostListView(ListView):
    model = BlogPost

class AuthorBlogPostView(DetailView):
    model = BlogPost

class AuthorBlogPostCreate(CreateView):
    model = BlogPost
    fields = ['title']
    success_url = reverse_lazy('author_blog_post_list')

class AuthorBlogPostUpdate(UpdateView):
    model = BlogPost
    fields = ['title', 'short_description', 'content']
    success_url = reverse_lazy('author_blog_post_list')

class AuthorBlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('author_blog_post_list')