from .forms import QueryForm, SubscriptionForm

def core(request):
	query_form = QueryForm()
	subscription_form =SubscriptionForm()

	return {
		'query_form': query_form,
		'subscription_form': subscription_form
	}