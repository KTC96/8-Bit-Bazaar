from django import template

register = template.Library()

@register.simple_tag
def clear_session_var(request, variable_name):
    del request.session[variable_name]
    return ''