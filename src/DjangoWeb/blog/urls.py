"""
Definition of urls for blog posts.
"""

from django.conf.urls import url
from blog.models import BlogPost
from django.contrib.auth.decorators import login_required
from blog.views import blogComment

import blog.views

urlpatterns = [
    url(r'^$',
        blog.views.BlogPostListView.as_view(
            queryset=BlogPost.objects.order_by('-pub_date')[:5],
            context_object_name='latest_post_list',
            template_name='blog/index.html',),
        name='home'),

    url(r'^blog/(?P<pk>\d+)/$',
        blog.views.BlogPostDetailView.as_view(template_name='blog/details.html'),name='blogpostdetail'),

    url('blog/author/list', blog.views.AuthorBlogPostListView.as_view(template_name='blog/author_blog_post_list.html'), name='author_blog_post_list'),

    url('blog/author/view/(?P<pk>\d+)/', blog.views.AuthorBlogPostView.as_view(template_name='blog/author_blog_post_detail.html'), name='author_blog_post_view'),

    url('blog/author/new', blog.views.AuthorBlogPostCreate.as_view(template_name='blog/author_blog_post_form.html'), name='author_blog_post_new'),

    url('blog/author/edit/(?P<pk>\d+)/', blog.views.AuthorBlogPostUpdate.as_view(template_name='blog/author_blog_post_form.html'), name='author_blog_post_edit'),

    url('blog/author/delete/(?P<pk>\d+)/', blog.views.AuthorBlogPostDelete.as_view(template_name='blog/author_blog_post_confirm_delete.html'), name='author_blog_post_delete'),

     url(r'^blog/(?P<pk>\d+)/comment/create/$',blogComment,
        name='comment_create'),
]
