from django import template


register = template.Library()


bad_words = ['редиска','дурак']

@register.filter()
def censor(value):
    for word in bad_words:
        value = value.replace(word,"*****")
    return value



