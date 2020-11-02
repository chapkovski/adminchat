from django import template

register = template.Library()


@register.inclusion_tag('adminchat/tags/chat.html', name='admin_chat', takes_context=True)
def render_chat(context, *args, **kwargs):
    return dict()
