# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cut
    Parameters
    ----------
    value : TYPE
        DESCRIPTION.
    arg : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return value.replace(arg, '')

# register.filter('cut', cut)