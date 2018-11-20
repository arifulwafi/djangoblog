"""
Definition of urls for blog posts.
"""

from django.conf.urls import url
from blog.models import BlogPost

import blog.views

urlpatterns = [
    url(r'^$',
        blog.views.BlogPostListView.as_view(
            queryset=BlogPost.objects.order_by('-pub_date')[:5],
            context_object_name='latest_post_list',
            template_name='blog/index.html',),
        name='home'),
    url(r'^blog/(?P<pk>\d+)/$',
        blog.views.BlogPostDetailView.as_view(
            template_name='blog/details.html'),
        name='blogpostdetail'),
]
