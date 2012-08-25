from five import grok

from Products.CMFCore.interfaces import IFolderish
from collective.megadrop.browser.interfaces import IRichTextMegaDrop 
from zope.interface import providedBy, alsoProvides, noLongerProvides
from Products.Five.utilities.marker import mark

class AddCustomTab(grok.View):
    """Render a document as a message
    """
    grok.name('md_custom_tab')
    grok.require('zope2.View')
    grok.context(IFolderish)
    
    def render(self):
        """No-op to keep grok.View happy
        """
        self.markMDCustom()
        
        return ''
    
    def markMDCustom(self):
        if IRichTextMegaDrop.providedBy(self.context):
            noLongerProvides(self.context, IRichTextMegaDrop)
        else:
            alsoProvides(self.context, IRichTextMegaDrop)
        
        self.context.reindexObject(idxs=['object_provides'])
        
        return True
        #alsoProvides(self.context, IRichTextMegaDrop)
        #return True

    #def unmarkMDCustom(self):
    #    noLongerProvides(self, IRichTextMegaDrop)
    #    return True