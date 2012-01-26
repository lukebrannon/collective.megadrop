from plone.theme.interfaces import IDefaultPloneLayer

from z3c.form import interfaces

from zope import schema

from zope.interface import Interface

from collective.megadrop import _

class IMegaDropInstalled(IDefaultPloneLayer):
    """A layer specific for collective.megadrop.
    """
    
class IRichTextMegaDrop(Interface):
    """Marker interface used to trigger RichText 
       MegaDrop menu.
    """

class IMegaDropSettings(Interface):
    """Global Megadrop Settings
    """

    
