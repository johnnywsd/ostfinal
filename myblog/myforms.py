from django import forms

class PostForm(forms.Form):
    #id = forms.IntegerField()
    title = forms.CharField(max_length=400)
    content = forms.CharField(required=False)
    tags = forms.CharField(required=False)
    blog_id = forms.IntegerField()

class BlogForm(forms.Form):
    name = forms.CharField(max_length=400)
    author_emails = forms.CharField(required=False)
    blog_id = forms.IntegerField(required=False)
