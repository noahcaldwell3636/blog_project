'''
POSTS - VIEWS.py
Fetches all basic user 'post' data from the database so it may
be referenced as html tags.
'''

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

    Inherited:
        ((SelectRelatedMixin)) Preloads a query of the post's
        specified foreign keys. Its purpose is to improve performance.
        ((generic.ListView)): queries a list of post models that can be 
        referenced in the html tag 'object_list'
    """

    model = models.Post # will listview the post model
    select_related = ("author", "group") # will query foreign keys to be referenced


class UserPosts(generic.ListView):
    """Return a list of all the posts for the current/logged
    in user.

    Inherited:
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
    """Returns the details of a particular post.

    Inherited:
        ((SelectRelatedMixin)): Preloads a query of the post's
        specified foreign keys. Its purpose is to improve performance.
        ((generic.DetailView)): Returns the object the view is operating upon.
        In this case, it woulld be the post the user has selected.
    """

    model = models.Post
    select_related = ("author", "group")

    def get_queryset(self):
        """TODO Currently confused as to why this queryset needs to
        be filtered."""
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    """Returns a form for the user to create a post.

    Inherited:
        ((LoginRequiredMixin)) : By default will send the user 
        to the login page if they are not authorized. You can 
        modify any parameters of AccessMixin for customizations.
        ((SelectRelatedMixin)) : Preloads a query of the post's
        specified foreign keys. Its purpose is to improve performance.
        ((generic.CreateView)) : Displays a form for creating an object
        with built in validation errors.
    """
    fields = ('message','group')
    model = models.Post

    def form_valid(self, form):
        """Called when a valid form is posted. In this case,
        the current user is saved as the new post's author along
        with the information captured in the form."""
        self.object = form.save(commit=False) # gets form instance but doesnt commit save so changes can still be made
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    """Allows the user to delete a post.

    Inherited:
        ((LoginRequiredMixin)) : Ensures the user must be logged in to delete a post.
        ((SelectRelatedMixin)) : Preloads specifed model's ForeignKeys in order to
        improve performance.
        ((generic.DeleteView)) : provides functionality for deleting a model, a post
        in this case.
    """
    model = models.Post
    select_related = ("author", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
