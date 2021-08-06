from django import forms
from .models import Query, Subscription

class QueryForm(forms.ModelForm):
	class Meta:
		model = Query
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(QueryForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
		self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone'})
		self.fields['website'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Website'})
		self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message'})

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(SubscriptionForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})