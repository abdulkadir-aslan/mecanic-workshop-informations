from django import template
from django.utils.safestring import mark_safe
import json
register = template.Library()

@register.filter()
def job_done(value):
    item = value.split(",")
    return item

