from django.forms.widgets import HiddenInput
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm, CommentForm, TagForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView,
                                  FormView,)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import OperationalError
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError



class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post
    template_name = "post_detail"

    def get_queryset(self):
        try:
            return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        except OperationalError:
            pass
        


class PostDetailView(DetailView):
    model = Post

    # is/ should this be handled in the SIDEBAR function in my_tags.py?
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            context['featured_list'] = Post.objects.filter(featured=True)
        except OperationalError:
            context['featured_list'] = None
        return context


class AddTagFormView(FormView):
    form_class = TagForm


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = reverse_lazy('post_list')
    success_url = reverse_lazy('post_list')
    form_class = PostForm
    model = Post

    def get_form_kwargs(self):
        kwargs = super(CreatePostView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

   


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """View for editing and updating an exisiting post.

    Args:
        LoginRequiredMixin: django authentication mixin
        UpdateView:django update view
    """    
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm
    model = Post


    def get_context_data(self, **kwargs):
            context = super(UpdateView, self).get_context_data(**kwargs)
            try:
                context['tag_form'] = TagForm
            except OperationalError:
                pass
            return context


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'post_list.html'

    model = Post

    def get_queryset(self):
        try:
            return Post.objects.filter(published_date__isnull=True).order_by('created_date')
        except OperationalError:
            pass

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(
        request,
        'blog/comment_form.html',
        { # context data
            'form': form,
            'user': request.user,
        }
    )


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=pk)