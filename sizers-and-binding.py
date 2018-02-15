import wx

# class HydraWindow(wx.Frame):
#     """A form class for VBScript-invoked dialogs."""
#
#     def __init__(self):
#         """Init function."""
#         wx.Frame.__init__(self, None, wx.ID_ANY, title="BZS/Python", size=(800, 600))
#         panel = wx.Panel(self, wx.ID_ANY)
#
# # Run the program
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = HydraWindow()
#     frame.Show()
#     app.MainLoop()


# class dialog(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, None, wx.ID_ANY, title="BZS/Python", size=(800, 600))
#         self.widget_output = []
#
#     def add_element(self, new_element):
#         pass
#
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = dialog()
#     frame.Show()
#     app.MainLoop()


class ScriptVars:
    user_name_to_print = "Enter name here"


class Form(wx.Panel):
    ''' The Form class is a wx.Panel that creates a bunch of controls
        and handlers for callbacks. Doing the layout of the controls is
        the responsibility of subclasses (by means of the doLayout()
        method). '''

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.referrers = ['friends', 'advertising', 'websearch', 'yellowpages']
        self.colors = ['blue', 'red', 'yellow', 'orange', 'green', 'purple',
                       'navy blue', 'black', 'gray']
        self.createControls()
        self.bindEvents()
        self.doLayout()

        # control_array = [wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY),
        #                  wx.Button(self, label="Save")]

    def createControls(self):
        self.logger = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.saveButton = wx.Button(self, label="Save")
        self.nameLabel = wx.StaticText(self, label="Your name:")
        self.nameTextCtrl = wx.TextCtrl(self, value="user_name_to_print")
        self.referrerLabel = wx.StaticText(self, label="How did you hear from us?")
        self.referrerComboBox = wx.ComboBox(self, choices=self.referrers, style=wx.CB_DROPDOWN)
        self.insuranceCheckBox = wx.CheckBox(self, label="Do you want Insured Shipment?")
        self.colorRadioBox = wx.RadioBox(self, label="What color would you like?", choices=self.colors, majorDimension=3, style=wx.RA_SPECIFY_COLS)

    def bindEvents(self):
        for control, event, handler in \
            [(self.saveButton, wx.EVT_BUTTON, self.onSave),
             (self.nameTextCtrl, wx.EVT_TEXT, self.onNameEntered),
             (self.nameTextCtrl, wx.EVT_CHAR, self.onNameChanged),
             (self.referrerComboBox, wx.EVT_COMBOBOX, self.onReferrerEntered),
             (self.referrerComboBox, wx.EVT_TEXT, self.onReferrerEntered),
             (self.insuranceCheckBox, wx.EVT_CHECKBOX, self.onInsuranceChanged),
             (self.colorRadioBox, wx.EVT_RADIOBOX, self.onColorchanged)]:
            control.Bind(event, handler)

    # def doLayout(self):
    #     ''' Layout the controls that were created by createControls().
    #         Form.doLayout() will raise a NotImplementedError because it
    #         is the responsibility of subclasses to layout the controls. '''
    #     raise NotImplementedError

    # Callback methods:

    def onColorchanged(self, event):
        self.__log('User wants color: %s' % self.colors[event.GetInt()])

    def onReferrerEntered(self, event):
        self.__log('User entered referrer: %s' % event.GetString())

    def onSave(self, event):
        self.__log('User clicked on button with id %d' % event.GetId())

    def onNameEntered(self, event):
        self.__log('User entered name: %s' % event.GetString())
        ScriptVars.user_name_to_print = event.GetString()

    def onNameChanged(self, event):
        self.__log('User typed character: %d' % event.GetKeyCode())
        event.Skip()

    def onInsuranceChanged(self, event):
        self.__log('User wants insurance: %s' % bool(event.Checked()))

    # Helper method(s):

    def __log(self, message):
        ''' Private method to append a string to the logger text
            control. '''
        self.logger.AppendText('%s\n' % message)


class FormWithSizer(Form):
    def doLayout(self):
        ''' Layout the controls by means of sizers. '''

        # A horizontal BoxSizer will contain the GridSizer (on the left)
        # and the logger text control (on the right):
        boxSizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        # A GridSizer will contain the other controls:
        gridSizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)

        # Prepare some reusable arguments for calling sizer.Add():
        expandOption = dict(flag=wx.EXPAND)
        noOptions = dict()
        emptySpace = ((0, 0), noOptions)

        test_array = [(self.nameLabel, noOptions),
                      (self.nameTextCtrl, expandOption),
                      (self.referrerLabel, noOptions),
                      (self.referrerComboBox, expandOption),
                      emptySpace,
                      (self.insuranceCheckBox, noOptions),
                      emptySpace,
                      (self.colorRadioBox, noOptions),
                      emptySpace,
                      (self.saveButton, dict(flag=wx.ALIGN_CENTER))
                      ]

        # Add the controls to the sizers:
        for control, options in test_array:
            gridSizer.Add(control, **options)

        for control, options in \
                [(gridSizer, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND, proportion=1))]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)


class FrameWithForms(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(FrameWithForms, self).__init__(*args, **kwargs)
        notebook = wx.Notebook(self)
        form1 = FormWithSizer(notebook)
        notebook.AddPage(form1, 'Sizers')
        # We just set the frame to the right size manually. This is feasible
        # for the frame since the frame contains just one component. If the
        # frame had contained more than one component, we would use sizers
        # of course, as demonstrated in the FormWithSizer class above.
        self.SetClientSize(notebook.GetBestSize())

        # print(form1.nameTextCtrl.Value)


if __name__ == '__main__':
    app = wx.App(0)
    frame = FrameWithForms(None, title='Demo with Notebook')
    frame.Show()
    app.MainLoop()

    # print(frame.nameTextCtrl)

print(ScriptVars.user_name_to_print)
