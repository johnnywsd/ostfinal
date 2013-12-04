from django import forms

class PostForm(forms.Form):
    #id = forms.IntegerField()
    title = forms.CharField(max_length=400)
    content = forms.CharField()
