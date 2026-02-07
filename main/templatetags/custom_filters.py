from django import template

register = template.Library()

@register.filter
def get_range(value):
    """Returns a range for iteration in templates"""
    return range(value)
