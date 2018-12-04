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
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from os import path
from .forms import BlogForm

import json


class BlogPostListView(ListView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['title'] = 'Blog Posts'
        context['year'] = datetime.now().year
        return context

class BlogPostDetailView(DetailView):
    model = BlogPost


    def get_context_data(self, **kwargs):
        context = super(BlogPostDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Post Detail'
        context['year'] = datetime.now().year
        return context

class AuthorBlogPostListView(ListView):
    model = BlogPost
    
    def get_queryset(self):
        return BlogPost.objects.filter(user_id=self.request.user.id)


class AuthorBlogPostView(DetailView):
    model = BlogPost

class AuthorBlogPostCreate(CreateView):
    template_name = "blog/author_blog_post_form.html"
    form_class = BlogForm

    def form_valid(self,form):
        form.instance.status = 1
        form.instance.isdeleted = False
        form.instance.created_date = datetime.now()
        form.instance.last_updated_date = datetime.now()
        form.instance.user_id = self.request.user.id
        return super(AuthorBlogPostCreate,self).form_valid(form)

    success_url = reverse_lazy('blog:author_blog_post_list')
    

class AuthorBlogPostUpdate(UpdateView):
    template_name = "blog/author_blog_post_form.html"
    model = BlogPost
    form_class = BlogForm

    def form_valid(self,form):
        form.instance.status = 1
        form.instance.isdeleted = False
        form.instance.created_date = datetime.now()
        form.instance.last_updated_date = datetime.now()

        return super(AuthorBlogPostUpdate,self).form_valid(form)

    success_url = reverse_lazy('blog:author_blog_post_list')

class AuthorBlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:author_blog_post_list')