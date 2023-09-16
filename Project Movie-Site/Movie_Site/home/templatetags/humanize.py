from django.template import Library

import humanize

register = Library()


@register.filter
def intcomma(number):
    num = humanize.intcomma(number)
    return str(num).replace(',', ' ')
