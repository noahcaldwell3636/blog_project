# django imports
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
# my imports
from . import forms
from . import models
# allows reference to the current logged in user
from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    """Returns a response containing a list of Post Models
    with their author/user and group.

    Args:
        ((SelectRelatedMixin)) allows to preload a query of the post's
        foreign keys so a query does not need to be made each time it is
        referenced. Its purpose is to improve performance.
        ((generic.ListView)): queries a list of post models that can be referenced
        in the html tag 'object_list'
    """

    model = models.Post # will listview the post model
    select_related = ("user", "group") # will query foreign keys to be referenced


class UserPosts(generic.ListView):
    """Return a list of all the posts for the current/logged
    in user.

    Args:
        ((generic.ListView)):  queries a list of post models authored by the 
        current user. The query can be referenced in the html tag 'object_list'.
    """

    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        """Return a query of all the current user's posts, ensuring that
        the user actually exists."""
        try: 
            # check that current user exists
            self.post_author = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            # error if user is not found
            raise Http404
        else:
            # return query of all the users posts
            return self.post_author.posts.all()

    def get_context_data(self, **kwargs):
        """Allows for extra information to be returned that is
        not already being provided by the gereic view. This
        case the django method will provide author of the each post."""
        context = super().get_context_data(**kwargs)
        context["post_author"] = self.post_author
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    """[summary]

    Args:
        SelectRelatedMixin ([type]): [description]
        generic ([type]): [description]

    Returns:
        [type]: [description]
    """

    model = models.Post
    select_related = ("user", "group")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('message','group')
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
