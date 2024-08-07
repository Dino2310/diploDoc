from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def split_url(addr, i):
    return addr.split(i)

