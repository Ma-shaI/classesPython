from django import template

register = template.Library()


@register.filter
def unique(lst):
    return list(set(lst))
