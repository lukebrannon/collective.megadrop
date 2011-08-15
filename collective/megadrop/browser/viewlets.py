from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import GlobalSectionsViewlet

#for navigation fix
from Products.CMFCore.utils import getToolByName

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
            results = tabObj.getFolderContents()
            items = []

            #taken from navigation.py
            portal_props = getToolByName(self, 'portal_properties')
            navtree_properties = getattr(portal_props, 'navtree_properties')
            blacklist = navtree_properties.getProperty('metaTypesNotToList', ())

            for result in results:
                #if result.portal_type in view_action_types:
                if result.portal_type not in blacklist:
                    items.append(result)

            #set theNav list
            theNav = []
            #sectionIterator = 1
            if items:
                itemsNum = len(items)
                if itemsNum <= 4:
                    divFill = 1
                else:
                    divFill = itemsNum / 4 + 1

                megadiv1 = []
                megadiv2 = []
                megadiv3 = []
                megadiv4 = []

                if divFill == 1:
                    if itemsNum >= 1:
                        megadiv1.append(items[0])
                    if itemsNum >= 2:
                        megadiv2.append(items[1])
                    if itemsNum >= 3:
                        megadiv3.append(items[2])
                    if itemsNum >= 4:
                        megadiv4.append(items[3])
                else:
                    for item in items [:divFill]:
                        megadiv1.append(item)

                    for item in items [divFill:divFill*2]:
                        megadiv2.append(item)

                    for item in items [divFill*2:divFill*3]:
                        megadiv3.append(item)

                    for item in items [divFill*3:divFill*4]:
                        megadiv4.append(item)

                if megadiv1:
                    theNav.append('<div class="megadiv1">')
                    theNav.append('<ul class="globalNav_lvl1">')
                    for item in megadiv1:
                        if item['is_folderish']:
                            #establish brain of folder contents
                            children = tabObj[item['id']].getFolderContents()
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a>'
                            theNav.append(theLine)
                            theNav.append('<ul class="globalNav_lvl2">')
                            for child in children:
                                theLine = '<li><a href="' + str(child.getURL()) + '">' + child['Title'] + '</a></li>'
                                theNav.append(theLine)
                            theNav.append('</ul>')
                            theNav.append('</li>')

                        else:
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a></li>'
                            theNav.append(theLine)


                        #sectionIterator+=1
                    theNav.append('</ul>')
                    theNav.append('</div>')

                if megadiv2:
                    theNav.append('<div class="megadiv2">')
                    theNav.append('<ul class="globalNav_lvl1">')
                    for item in megadiv2:
                        if item['is_folderish']:
                            #establish brain of folder contents
                            children = tabObj[item['id']].getFolderContents()
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a>'
                            theNav.append(theLine)
                            theNav.append('<ul class="globalNav_lvl2">')
                            for child in children:
                                theLine = '<li><a href="' + str(child.getURL()) + '">' + child['Title'] + '</a></li>'
                                theNav.append(theLine)
                            theNav.append('</ul>')
                            theNav.append('</li>')

                        else:
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a></li>'
                            theNav.append(theLine)


                        #sectionIterator+=1
                    theNav.append('</ul>')
                    theNav.append('</div>')

                if megadiv3:
                    theNav.append('<div class="megadiv3">')
                    theNav.append('<ul class="globalNav_lvl1">')
                    for item in megadiv3:
                        if item['is_folderish']:
                            #establish brain of folder contents
                            children = tabObj[item['id']].getFolderContents()
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a>'
                            theNav.append(theLine)
                            theNav.append('<ul class="globalNav_lvl2">')
                            for child in children:
                                theLine = '<li><a href="' + str(child.getURL()) + '">' + child['Title'] + '</a></li>'
                                theNav.append(theLine)
                            theNav.append('</ul>')
                            theNav.append('</li>')

                        else:
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a></li>'
                            theNav.append(theLine)


                        #sectionIterator+=1
                    theNav.append('</ul>')
                    theNav.append('</div>')

                if megadiv4:
                    theNav.append('<div class="megadiv4">')
                    theNav.append('<ul class="globalNav_lvl1">')
                    for item in megadiv4:
                        if item['is_folderish']:
                            #establish brain of folder contents
                            children = tabObj[item['id']].getFolderContents()
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a>'
                            theNav.append(theLine)
                            theNav.append('<ul class="globalNav_lvl2">')
                            for child in children:
                                theLine = '<li><a href="' + str(child.getURL()) + '">' + child['Title'] + '</a></li>'
                                theNav.append(theLine)
                            theNav.append('</ul>')
                            theNav.append('</li>')

                        else:
                            theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a></li>'
                            theNav.append(theLine)


                        #sectionIterator+=1
                    theNav.append('</ul>')
                    theNav.append('</div>')

            return theNav

        else:
            #item is not container return False
            return False

