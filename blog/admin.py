# BLOG - ADMIN.PY
from django.contrib import admin
from .models import Post, Comment

# REGISTER ALL BLOG MODELS HERE 
admin.site.register(Post)
admin.site.register(Comment)
