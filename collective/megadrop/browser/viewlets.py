from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import GlobalSectionsViewlet

#for navigation fix
from Products.CMFCore.utils import getToolByName

from Products.CMFCore.interfaces import IFolderish
from zope.app.component.hooks import getSite

class MegaDropGlobalSectionsViewlet(GlobalSectionsViewlet):
    """A custom version of the global navigation viewlet that reveals two levels of structure
       in a single drop down drawer.
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
            
            
            #print utils.getUserFriendlyTypes(results)
                
            items = []

            #borrowed from navigation.py
            portal_props = getToolByName(self, 'portal_properties')
            navtree_properties = getattr(portal_props, 'navtree_properties')
            blacklist = navtree_properties.getProperty('metaTypesNotToList', ())
            
            catalog = getToolByName(self, 'portal_catalog')
            
            for result in results:
                result_rid = result.getRID()
                indexed_default_result_page = catalog._catalog.getIndex("is_default_page").getEntryForObject(result_rid, default=[])
                #if result.portal_type in view_action_types:
                if result.portal_type not in blacklist and not indexed_default_result_page and not result['exclude_from_nav']:
                    items.append(result)

            #set theNav list
            theNav = []
            #sectionIterator = 1
            if items:
                itemsNum = len(items)
                divFill = 0
                if itemsNum <= 3:
                    divFill = 1
                else:
                    itemsRdr = itemsNum%3
                    if itemsRdr:
                        if itemsRdr == 1:
                            divFill0 = itemsNum / 3 + 1
                            divFill1 = divFill2 = itemsNum / 3
                        elif itemsRdr == 2:
                            divFill0= divFill1 = itemsNum / 3 + 1
                            divFill2 = itemsNum / 3

                    else:
                        divFill0 = divFill1 = divFill2 = itemsNum / 3
                    
                    #set column slices
                    colA = divFill0
                    colB = divFill0+divFill1
                        
                #set brain lists for each column        
                megadiv1 = []
                megadiv2 = []
                megadiv3 = []
                megadivList = [megadiv1, megadiv2, megadiv3,]
                
                
                if divFill:
                    divIter = 0
                    for item in items:
                        megadivList[divIter].append(item)
                        divIter += 1
                else:
                    for item in items [:colA]:
                        megadiv1.append(item)

                    for item in items [colA:colB]:
                        megadiv2.append(item)

                    for item in items [colB:]:
                        megadiv3.append(item)
                
                #create html to return
                divListIter = 1
                
                #ptool = getToolByName(self, 'plone_utils')
                
                for divSection in megadivList:
                    if divSection:
                        theNav.append('<div class="megadiv' + str(divListIter) + '">')
                        theNav.append('<ul class="globalNav_lvl1">')
                        for item in divSection:
                            if item['is_folderish']:
                                
                                #establish brain of folder contents
                                children = tabObj[item['id']].getFolderContents()
                                
                                #start template
                                theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a>'
                                theNav.append(theLine)
                                theNav.append('<ul class="globalNav_lvl2">')
                                for child in children:
                                    #try with RID
                                    child_rid = child.getRID()
                                    indexed_default_page = catalog._catalog.getIndex("is_default_page").getEntryForObject(child_rid, default=[])
                                    if child.portal_type not in blacklist and not indexed_default_page and not child['exclude_from_nav']:
                                        theLine = '<li><a href="' + str(child.getURL()) + '">' + child['Title'] + '</a></li>'
                                        theNav.append(theLine)
                                
                                
                                
                                theNav.append('</ul>')
                                theNav.append('</li>')

                            else:
                                theLine = '<li><a href="' + str(item.getURL()) + '">' + item['Title'] + '</a></li>'
                                theNav.append(theLine)

                        theNav.append('</ul>')
                        theNav.append('</div>')

                    divListIter += 1

            return theNav

        else:
            #item is not container return False
            return False
