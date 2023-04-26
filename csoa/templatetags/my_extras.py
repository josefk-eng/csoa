from django import template

register = template.Library()


@register.filter
def slide_text(words, text):
    filtered = words.filter(movingText=text)
    return list(filtered)
