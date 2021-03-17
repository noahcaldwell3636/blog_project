from django import template
from blog.forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Post

register = template.Library()

@login_required
@register.inclusion_tag('blog/_comment_form.html')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return {"form": form, "post": post}


@register.inclusion_tag('blog/_sidebar.html')
def sidebar():
    featured_list = Post.objects.filter(featured=True)
    return {'featured_list': featured_list}


@register.inclusion_tag('blog/_social_link_group.html')
def social_link_group():
    featured_list = Post.objects.filter(featured=True)
    return {'featured_list': featured_list}