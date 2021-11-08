# Register your models here.
from django.contrib import admin
from gymlog.models import Post, Comment, Gym

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Gym)