from django.forms import ModelForm
from blog.models import Comment
from .models import BlogPost


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude =['status','isdeleted','order','created_date','last_updated_date','user']

       


#class CommentForm(ModelForm):
#    class Meta:
#        model = Comment
#        excude = ['status','order','pub_date','created_date','last_updated_date','isdeleted','blog_post']