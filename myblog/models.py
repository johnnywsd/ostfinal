from django.db import models
from django.contrib.auth.models import User

import os
import uuid
from django.core.files.storage import default_storage as s3_storage
from myblog import constant
import html2text

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
    
    def get_create_date_str(self):
        return self.create_time.strftime(constant.DATE_FORMAT)

    def get_content_brief(self):
        content_plain_text = html2text.html2text(self.content)
        ret = content_plain_text[:constant.BRIEF_LENGTH]
        return ret 

    def get_author_full_name(self):
        return '%s %s' % (self.author.first_name, self.author.last_name)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

IMG_PATH = 'img'
def filename2uuid(instance, filename, path=IMG_PATH):
    splited = filename.split('.')
    if len(splited) > 1:
        ext = filename.split('.')[-1]
        ret = "%s.%s" % (uuid.uuid4(), ext)
    else:
        ret = "%s" % uuid.uuid4()
    #return ret
    return os.path.join(path, ret) 

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(storage=s3_storage,
            upload_to=filename2uuid, blank=True, null=True)
    post = models.ForeignKey(Post, blank=True, null=True)
# Create your models here.
