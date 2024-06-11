from django.contrib import admin
from .models import CustomUser, Post, Comment, Project, Version

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(Version)

