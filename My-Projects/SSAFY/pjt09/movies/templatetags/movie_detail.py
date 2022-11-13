from django import template

register = template.Library()

@register.filter
def make_genre_list(genres):
    return ', '.join([genre.name for genre in genres])
