from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class IMegaDropInstalled(IDefaultPloneLayer):
    """A layer specific for collective.megadrop.
    """
    
class IRichTextMegaDrop(Interface):
    """Marker interface used to trigger RichText 
       MegaDrop menu.
    """