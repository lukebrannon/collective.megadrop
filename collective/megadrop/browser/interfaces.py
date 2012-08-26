from plone.theme.interfaces import IDefaultPloneLayer

from z3c.form import interfaces

from zope import schema

from zope.interface import Interface

from plone.app.textfield import RichText

from collective.megadrop import _

class IMegaDropInstalled(IDefaultPloneLayer):
    """A layer specific for collective.megadrop.
    """
    
class IRichTextMegaDrop(Interface):
    """Marker interface used to trigger RichText 
       MegaDrop menu.
    """
    mdTabContent = RichText(
        title=_(u"Tab Content"),
        description=_(u"Enter content to display in your megadrop tab"),
        required=False,
        default=u'',)

class IMegaDropSettings(Interface):
    """Global Megadrop Settings
    """
    
