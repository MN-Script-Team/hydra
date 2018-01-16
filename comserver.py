"""Testing the creation of COM servers for dialogs."""
# TODO: this needs to be packaged so it provides wx and win32com


class HydraDialog:
    """This generates a dialog class to be used by VBScript files."""

    _reg_clsid_ = "{fe6203dc-f738-11e7-b7c0-88d7f67dcf01}"
    _reg_desc_ = "Hydra Dialog COM Server"
    _reg_progid_ = "Hydra.Dialog"
    _public_methods_ = ['Hello', 'Dialog', 'setWidth', 'setHeight', 'setTitle', 'getOutput']
    _public_attrs_ = ['softspace', 'noCalls']
    _readonly_attrs_ = ['noCalls']

    def __init__(self):
        """Define softspace and nocalls."""
        self.softspace = 1
        self.noCalls = 0

    # def setOutput(self, width):
    #     """Set the output of the dialog to a variable."""
    #     global dlgWidth_num
    #     dlgWidth_num = width

    def setWidth(self, width):
        """Set the width of the dialog."""
        global dlgWidth_num
        dlgWidth_num = width

    def setHeight(self, height):
        """Set the height of the dialog."""
        global dlgHeight_num
        dlgHeight_num = height

    def setTitle(self, title):
        """Set the title of the dialog."""
        global dlgTitle_text
        dlgTitle_text = title

    global output_for_VB

    def getOutput(self):
        """Return output to be executed by VBS."""
        return self.output_for_VB

    def Dialog(self):
        """Display the dialog."""
        import wx

        self.output_for_VB = "pass_success = false"

        class MyFrame(wx.Frame):
            """We simply derive a new class of Frame."""

            def __init__(self, parent, title):
                wx.Frame.__init__(self, parent, title=dlgTitle_text, size=(dlgWidth_num, dlgHeight_num))
                panel = wx.Panel(self, wx.ID_ANY)

                sizer = wx.BoxSizer(wx.VERTICAL)

                # Blank array which we use later
                buttons = []

                # TODO: replace str(i) with the variable
                for i in range(0, 2):
                    buttons.append(wx.Button(panel, id=wx.ID_ANY, label="Button " + str(i), name=str(i)))

                for button in buttons:
                    self.buildButtons(button, sizer)

                panel.SetSizer(sizer)

                self.Show(True)

            def buildButtons(self, btn, sizer):
                """Build buttons with IDs and such."""
                btn.Bind(wx.EVT_BUTTON, self.onButton)
                sizer.Add(btn, 0, wx.ALL, 5)

            def onButton(self, event):
                """Fire when its corresponding button is pressed."""
                button = event.GetEventObject()
                self.output_for_VB = "ButtonPressed = " + button.GetName()
                print(self.output_for_VB)

                # button_id = event.GetId()
                # button_by_id = self.FindWindowById(button_id)
                # print("By ID: " + button_by_id.GetLabel())
                # print("Name by ID: " + button_by_id.GetName())

        app = wx.App(True)
        frame = MyFrame(None, "Hydra test")
        frame.Show()
        app.MainLoop()
        # print(return_to_VBS)


if __name__ == '__main__':
    import win32com.server.register
    win32com.server.register.UseCommandLine(HydraDialog)
