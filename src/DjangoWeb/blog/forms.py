from django.forms import ModelForm
from .models import BlogPost


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude =['status','isdeleted','order','created_date','last_updated_date','user']