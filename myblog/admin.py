from django.contrib import admin
from myblog.models import *

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
