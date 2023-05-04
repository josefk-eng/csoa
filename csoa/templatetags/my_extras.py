from django import template

register = template.Library()


@register.filter
def slide_text(words, text):
    filtered = words.filter(movingText=text)
    return list(filtered)


@register.filter
def headers(heads, section):
    filtered = heads.get(section=section)
    return filtered.head


@register.filter
def sub_headers(heads, section):
    filtered = heads.get(section=section)
    return filtered.description
