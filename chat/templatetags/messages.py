from django import template

register = template.Library()


@register.filter
def format_messages(messages):
    if not messages:
        return []

    formatted_messages = []
    current_author = None
    current_group = []

    for message in messages:
        if message.author != current_author:
            if current_group:
                formatted_messages.append({'author': current_author, 'messages': current_group})
            current_author = message.author
            current_group = [message]
        else:
            current_group.append(message)

    if current_group:
        formatted_messages.append({'author': current_author, 'messages': current_group})

    return formatted_messages
