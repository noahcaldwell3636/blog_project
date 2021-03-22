# BLOG - ADMIN.PY
from django.contrib import admin
from .models import Post, Comment, Tag

# REGISTER ALL BLOG MODELS HERE 
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
