from django.template import Library
from mailing_list.forms import MailingListForm

register = Library()


@register.inclusion_tag("mailing_list/form_mailing.html")
def mailing_form():
    return {"mailing_form": MailingListForm()}

