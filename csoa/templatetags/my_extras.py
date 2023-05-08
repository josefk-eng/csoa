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


@register.filter
def coordinators(portfolios, group):
    filtered = portfolios.filter(group__icontains=group)
    return list(filtered)


@register.filter
def mainStory(story):
    filtered = story.get(isMain=True)
    return filtered.title


@register.filter
def mainDescription(story):
    filtered = story.get(isMain=True)
    return filtered.description


@register.filter
def mainLink(story):
    filtered = story.get(isMain=True)
    return filtered.url


@register.filter
def image(story):
    filtered = story.get(isMain=True)
    return filtered.image.url
