from django import template
from django.contrib.messages import get_messages
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('components/messages.html', takes_context=True)
def show_messages(context):
    return {
        'messages': get_messages(context['request']),
    }


@register.inclusion_tag('components/nav_menu.html', takes_context=True)
def nav_menu(context, items):
    request = context['request']
    current_url = request.path

    menu_items = []
    for item_str in items.split(','):
        parts = item_str.split('=')
        url_name = parts[1].strip()
        menu_items.append({
            'name': parts[0].strip(),
            'url_name': url_name,
            'icon': parts[2].strip() if len(parts) > 2 else None,
            'is_active': current_url == reverse(url_name)
        })

    return {
        'menu_items': menu_items
    }
