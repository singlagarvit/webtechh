from django.contrib import admin
from .models import Query, Subscription

class QueryAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone', 'created_on']

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'created_on']

admin.site.register(Query, QueryAdmin)
admin.site.register(Subscription, SubscriptionAdmin)