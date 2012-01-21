from five import grok
from zope import schema

from plone.directives import form, dexterity

from collective.megadrop import _

class IDropFolder():
    """A folder to include richtext content for megadrop navigation.
    """