"""Test buttons."""
import wx
import sys

global dlg_argument_to_parse


# If there's no dialog passed to this utility, use a standard dialog for debugging/testing.
if len(sys.argv) == 1:
    dlg_argument_to_parse = ("BeginDialog|320|110|HydraVB Dialog Generator|~|"
                             "Button|120|80|80|24|OK|-1|~|"
                             "Text|10|10|300|70|HydraVB.exe is a dialog generator written by Veronica Cary for DHS' BlueZone Scripts Program"
                             " to overcome limitations in VBScript's dialog rendering. It is written in Python, source code is available at"
                             " https://github.com/MN-Script-Team/hydra. |")
else:
    dlg_argument_to_parse = sys.argv[1]
    print(dlg_argument_to_parse)


# A blank array we'll use for button controls
buttons = []

# A blank array for text controls
textcontrols = []
returncontrols = []
checkboxcontrols = []

dialog_declaration_details = dlg_argument_to_parse.split("|~|")[0]

global dialog_width
dialog_width = int(dialog_declaration_details.split("|")[1]) + 16   # For some reason it's off by this with the 331x160 box

global dialog_height
dialog_height = int(dialog_declaration_details.split("|")[2]) + 39  # For some reason it's off by this with the 331x160 box

global dialog_title
dialog_title = str(dialog_declaration_details.split("|")[3])


class HydraVBDialog(wx.Frame):
    """A form class for VBScript-invoked dialogs."""

    def __init__(self):
        """Init function."""
        wx.Frame.__init__(self, None, wx.ID_ANY, title=dialog_title, size=(dialog_width, dialog_height))
        panel = wx.Panel(self, wx.ID_ANY)

        font = panel.GetFont()
        font.SetPointSize(8)
        font.SetFamily(wx.FONTFAMILY_SWISS)
        # font.SetFaceName("Tahoma")
        panel.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)

        for control_to_parse in dlg_argument_to_parse.split("|~|"):
            control_parsed = control_to_parse.split("|")
            if control_parsed[0].lower() == "button":
                (buttons.append(wx.Button(panel,
                                          id=wx.ID_ANY,
                                          label=control_parsed[5],
                                          name=control_parsed[6],
                                          pos=(int(control_parsed[1]), int(control_parsed[2])),
                                          size=(int(control_parsed[3]), int(control_parsed[4])))))
            elif control_parsed[0].lower() == "text":
                (textcontrols.append(wx.StaticText(panel,
                                                   id=wx.ID_ANY,
                                                   label=control_parsed[5],
                                                   name=control_parsed[6],
                                                   pos=(int(control_parsed[1]), int(control_parsed[2])),
                                                   size=(int(control_parsed[3]), int(control_parsed[4])))))
            elif control_parsed[0].lower() == "groupbox":
                (textcontrols.append(wx.StaticBox(panel,
                                                  id=wx.ID_ANY,
                                                  label=control_parsed[5],
                                                  name=control_parsed[6],
                                                  pos=(int(control_parsed[1]), int(control_parsed[2])),
                                                  size=(int(control_parsed[3]), int(control_parsed[4])))))
            elif control_parsed[0].lower() == "editbox":
                (returncontrols.append(wx.TextCtrl(panel,
                                                   id=wx.ID_ANY,
                                                   value=control_parsed[5],
                                                   name=control_parsed[6],
                                                   pos=(int(control_parsed[1]), int(control_parsed[2])),
                                                   size=(int(control_parsed[3]), int(control_parsed[4])))))
            elif control_parsed[0].lower() == "combobox":
                (returncontrols.append(wx.ComboBox(panel,
                                                   id=wx.ID_ANY,
                                                   choices=control_parsed[5].split("+chr(9)+"),
                                                   name=control_parsed[6],
                                                   pos=(int(control_parsed[1]), int(control_parsed[2])),
                                                   size=(int(control_parsed[3]), int(control_parsed[4])))))
            elif control_parsed[0].lower() == "droplistbox":
                (returncontrols.append(wx.ComboBox(panel,
                                                   id=wx.ID_ANY,
                                                   choices=control_parsed[5].split("+chr(9)+"),
                                                   name=control_parsed[6],
                                                   style=wx.CB_READONLY,
                                                   pos=(int(control_parsed[1]), int(control_parsed[2])),
                                                   size=(int(control_parsed[3]), int(control_parsed[4])))))
            elif control_parsed[0].lower() == "checkbox":
                (checkboxcontrols.append(wx.CheckBox(panel,
                                                     id=wx.ID_ANY,
                                                     label=control_parsed[5],
                                                     name=control_parsed[6],
                                                     pos=(int(control_parsed[1]), int(control_parsed[2])),
                                                     size=(int(control_parsed[3]), int(control_parsed[4])))))
                # print(str(["A", "B"]))
                # print(control_parsed[5].split("+chr(9)+"))

        for button in buttons:
            self.buildButtons(button, sizer)

        # panel.SetSizer(sizer)

    def buildButtons(self, btn, sizer):
        """Build buttons."""
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, wx.ALL, 5)

    def onButton(self, event):
        """Fire when its corresponding button is pressed."""
        button = event.GetEventObject()

        print('RETURN-->ButtonPressed = ' + button.GetName())

        # Goes through each editbox-style control and prints a return string to be iterated through VBScript (via stdout)
        for control in returncontrols:
            print("RETURN-->" + control.GetName() + ' = "' + control.GetValue() + '"')

        # Checkboxes use different logic in BZSH, requiring 1s and 0s instead of true and false
        for control in checkboxcontrols:
            # True (checked) is 1, false is 0
            if control.GetValue() == True:
                print("RETURN-->" + control.GetName() + ' = 1')
            else:
                print("RETURN-->" + control.GetName() + ' = 0')

        self.Close()

        # button_id = event.GetId()
        # button_by_id = self.FindWindowById(button_id)
        # print("By ID: " + button_by_id.GetLabel())
        # print("Name by ID: " + button_by_id.GetName())


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = HydraVBDialog()
    frame.Show()
    app.MainLoop()
