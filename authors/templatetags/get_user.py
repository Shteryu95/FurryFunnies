from django import template

from authors.models import Author

register = template.Library()


@register.simple_tag
def get_user():
    return Author.objects.first()