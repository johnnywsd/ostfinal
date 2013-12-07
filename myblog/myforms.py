from django import forms

class PostForm(forms.Form):
    #id = forms.IntegerField()
    title = forms.CharField(max_length=400)
    content = forms.CharField(required=False)
    tags = forms.CharField(required=False)
    blog_id = forms.IntegerField()
