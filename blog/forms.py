from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['post', 'approved']

	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
		self.fields['website'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Website'})
		self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message'})