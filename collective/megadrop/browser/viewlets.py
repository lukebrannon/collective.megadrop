from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import GlobalSectionsViewlet

from Products.CMFCore.interfaces import IFolderish
from zope.app.component.hooks import getSite

class MegaDropGlobalSectionsViewlet(GlobalSectionsViewlet):
    """A custom version of the global navigation viewlet
    """

    def render(self):
        # defer to index method, because that's what gets overridden by the template ZCML attribute
        return self.index()

    index = ViewPageTemplateFile('sections.pt')

    def getPortalRoot(self):
        site = getSite()

        return site


    def sectionQuery(self, tabObj):
        #check to make sure tabObj is a container
        if IFolderish.providedBy(tabObj):
            #return brain of tabObj contents
            items = tabObj.getFolderContents()

            #set theNav list
            theNav = []
            sectionIterator = 1
            if items:
                theNav.append('<ul class="globalNav_ul">')
                for item in items:
                    if item['is_folderish']:
                        #establish brain of folder contents
                        children = tabObj[item['id']].getFolderContents()
                        theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a>'
                        theNav.append(theLine)
                        theNav.append('<ul>')
                        for child in children:
                            theLine = '<li><a href="' + str(child.getURL()) + '">' + child['Title'] + '</a></li>'
                            theNav.append(theLine)
                        theNav.append('</ul>')
                        theNav.append('</li>')

                    else:
                        theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a></li>'
                        theNav.append(theLine)


                    sectionIterator+=1
                theNav.append('</ul>')

            return theNav

        else:
            #item is not container return False
            return False

