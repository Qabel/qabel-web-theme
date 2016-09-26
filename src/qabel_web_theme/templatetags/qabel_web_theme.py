
from django.template import Library, Node, TemplateSyntaxError
from django.utils import translation

register = Library()


class GetCurrentLanguageShortCodeNode(Node):
    def __init__(self, variable):
        self.variable = variable

    def render(self, context):
        # de-DE -> de
        context[self.variable] = translation.get_language().split('-', 1)[0]
        return ''


@register.tag('get_current_language_short')
def do_get_current_language_short(parser, token):
    """
    This will store the current languages short code in the context.

    Usage::

        {% get_current_language as language %}

    This will fetch the currently active language and
    put it's value into the ``language`` context
    variable.
    """
    # token.split_contents() isn't useful here because this tag doesn't accept variable as arguments
    args = token.contents.split()
    if len(args) != 3 or args[1] != 'as':
        raise TemplateSyntaxError("'get_current_language_short' requires 'as variable' (got %r)" % args)
    return GetCurrentLanguageShortCodeNode(args[2])


@register.simple_tag
def qabel_de():
    # XXX via settings
    return 'https://www.qabel.de'
