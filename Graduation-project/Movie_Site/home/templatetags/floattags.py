from django.template.defaultfilters import floatformat
from django.template import Library

register = Library()


def formatted_float(value):
    value = floatformat(value, arg=1)
    return str(value).replace(',', '.')


def formatted_float_2(value):
    value = floatformat(value, arg=2)
    return str(value).replace(',', '.')


register.filter('formatted_float', formatted_float)
register.filter('formatted_float_2', formatted_float_2)
