from zope.interface import Interface

from plone import tiles
from zope.schema import Text
from plone.app.textfield import RichText
from plone.app.textfield.interfaces import ITransformer


class IRichTextTileData(Interface):

    text = RichText(title=u'Text')


class RichTextTile(tiles.PersistentTile):

    def __call__(self):
        text = ''
        if self.data['text']:
            transformer = ITransformer(self.context, None)
            if transformer is not None:
                text = transformer(self.data['text'], 'text/x-html-safe')
        return '<html><body>%s</body></html>' % text