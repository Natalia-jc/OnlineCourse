from django import template


register = template.Library()


@register.filter(name='get_selected')

def get_selected(question,selected):
    return question.get_selected_answer(selected)
