from .models import Post, commets
from django import  forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner', 'pub_date']
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = commets
        exclude = ['user_id', 'post_id']
  

class UpdateCaptionForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner', 'pub_date','userpost',]
  