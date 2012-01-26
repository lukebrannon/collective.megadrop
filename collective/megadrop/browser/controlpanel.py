from plone.app.registry.browser import controlpanel

from collective.megadrop.browser.interfaces import IMegaDropSettings

from collective.megadrop import _


class MegaDropSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IMegaDropSettings
    label = _(u"MegaDrop Control")
    description = _(u"""""")

    def updateFields(self):
        super(MegaDropSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(MegaDropSettingsEditForm, self).updateWidgets()

class MegaDropSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MegaDropSettingsEditForm
