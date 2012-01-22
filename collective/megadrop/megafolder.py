from five import grok
from zope import schema

from plone.directives import form, dexterity
from plone.app.textfield import RichText

from collective.megadrop import _

class IDropFolder(form.Schema):
    """A folder to include richtext content for megadrop navigation.
    """
    
    use_body_text = schema.Bool(
            title=_(u"Custom View"),
            description=_(u"Check this box display the custom content below."),
            required=False,
        )
    
    body = RichText(
            title=_(u"Drop Down Custom Content"),
            description=_(u"Custom content to be displayed in your drop down menu"),
            required=False,
        )

class View(grok.View):
    grok.context(IDropFolder)
    grok.require('zope2.View')
