from django import forms
from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    '''
    Creates a form for the admin to fillout when creating a new post. The input
    fields will be used to create a post model.
    '''
    # basically did te init func to pass in the username of the person logged in
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(PostForm, self).__init__(*args, **kwargs)
        widget_subattrs = self.fields['author'].widget.attrs
        widget_subattrs['value'] = self.request.user.username

    # the input fields in Meta will inherit properties from the ModelForm class 
    class Meta:
        # specify model for the ModelForm class
        model = Post
        # specify what input fields will need to be rendered as inputs on the 
        # html page 
        fields = ('author', 'title', 'image', 'featured', 'summary', 'text', )
        # customize widgets... labels are customized in the html and css files        
        widgets = {
            'author': forms.TextInput(attrs={
                    'class': 'editable medium-editor-textarea input-post-content margin-bottom-1per',
                    'disabled': "true",
                }
            ),
            'title': forms.TextInput(attrs={
                    'class': 'editable medium-editor-textarea input-post-content margin-bottom-1per',
                }
            ),
            # 'image': forms.ImageField(),
            'featured': forms.CheckboxInput(attrs={
                    'class': 'size-check margin-bottom-1per vert-center'
                }
            ),
            'summary': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea input-post-content margin-bottom-1per'
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea input-post-content margin-bottom-1per' 
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
        fields = ('title', )
        # ovverride defaults for the input forms
        widgets = {
            '': forms.TextInput(attrs={'class': 'form-control'}),
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


