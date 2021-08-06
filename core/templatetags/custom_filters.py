from django import template
import bleach

register = template.Library()

@register.filter(name='slider_count')
def slider_count(value, arg):
	return value * 77 + arg

@register.filter(name='remove_tags')
def remove_tags(value):
    return bleach.clean(value, tags=["h1", "h2", "h3", "h4", "ul", "li"])