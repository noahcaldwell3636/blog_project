from django import forms
from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    '''
    Creates a form for the admin to fillout when creating a new post. The input
    fields will be used to create a post model.
    '''
    # the input fields in Meta will inherit properties from the ModelForm class 
    class Meta:
        # specify model for the ModelForm class
        model = Post
        # specify what input fields will need to be rendered as inputs on the 
        # html page 
        fields = ('author','title', 'text')
        # the widget variable is used to override django input form defaults
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'textinputclass'}
            ),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent'
            }),
        }

class TagForm(forms.ModelForm):
    '''
    Creates a comment form from the commment model. Inputs will be generated for
    use in html, that will then be submitted to create a comment model in the 
    database.
    '''
    class Meta:
        # choose what model will be created in the form
        model = Tag
        # choose what input are needed from the user
        fields = ('name', )
        # ovverride defaults for the input forms
        widgets = {
            # 'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'name': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    '''
    Creates a comment form from the commment model. Inputs will be generated for
    use in html, that will then be submitted to create a comment model in the 
    database.
    '''

    class Meta:
        # choose what model will be created in the form
        model = Comment
        # choose what input are needed from the user
        fields = ('text', )
        # ovverride defaults for the input forms
        widgets = {
            # 'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea bg-white'}),
        }


