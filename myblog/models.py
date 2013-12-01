from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, related_name="creator_blogs")
    authors = models.ManyToManyField(User, related_name="author_blogs")
    followers = models.ManyToManyField(User, related_name="follower_blogs",
            null=True, blank=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=400)
    content = models.TextField(blank=True, null=True)
    #comments = models.OneToManyField(Comment)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

# Create your models here.
