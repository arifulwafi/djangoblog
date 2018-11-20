"""
Definition of urls for accounts.
"""

from django.conf.urls import url

import account.views

urlpatterns = [
    url(r'^account/signup$', account.views.signup, name='signup'),
]
