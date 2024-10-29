from django import forms

from posts.models import Post


class BasePost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('updated_at', 'author')

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }

        help_texts = {
            'image_url': 'Share your funniest furry photo URL!'
        }

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        }


class CreatePost(BasePost):
    pass


class EditPost(BasePost):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''


class DeletePost(BasePost):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['readonly'] = True
