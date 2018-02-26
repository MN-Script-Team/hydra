import wx


script_vars = {
    "PRISMCaseNum": "0000000016-01",
    "StartDate": "01/01/2018",
    "EndDate": "02/01/2018"
}


class testDialog(wx.Frame):

    def __init__(self, parent, title, contents):
        super(testDialog, self).__init__(parent, title=contents[0])     # Sets title to be the first item in the contents array

        global script_vars

        # for key, value in script_vars.items():
        #   print(key, "=", value)

        # content type taken from PALC calculator: https://github.com/MN-Script-Team/DHS-PRISM-Scripts/blob/master/calculators/palc.vbs

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(0, 0)
        # sizer = wx.GridBagSizer()

        # TODO: CAN I MAKE THIS A FUNCTION WHICH GETS PASSED PARAMETERS AND RESPONDS WITH BINDING SIMILAR TO HYDRAVB BUT PURE PYTHON?????

        # labelPRISMCaseNum = wx.StaticText(panel, label="PRISM case number:")
        # sizer.Add(labelPRISMCaseNum, pos=(0, 0), flag=wx.ALL, border=5)
        # textPRISMCaseNum = wx.TextCtrl(panel, value=script_vars["PRISMCaseNum"], name="PRISMCaseNum")
        # sizer.Add(textPRISMCaseNum, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=5)
        # textPRISMCaseNum.Bind(wx.EVT_TEXT, self.OnEdited)


        # BUG: Needs to iterate smarter... I think the DialogItem object is only accepting the last item... perhaps dynamnically in an array?

        for key in contents:
            if key > 0:
                print(str(key), contents[key].Label)
                label_to_add = wx.StaticText(panel, label=contents[key].Label)
                sizer.Add(label_to_add, pos=(0, 0), flag=wx.ALL, border=5)
                textctrl_to_add = wx.TextCtrl(panel, value=script_vars[contents[key].Variable], name=contents[key].Variable)
                sizer.Add(textctrl_to_add, pos=(0, 1), span=contents[key].Span, flag=wx.EXPAND | wx.ALL, border=5)
                textctrl_to_add.Bind(wx.EVT_TEXT, self.OnEdited)

        # labelStartDate = wx.StaticText(panel, label="Start date:")
        # sizer.Add(labelStartDate, pos=(1, 0), flag=wx.ALL, border=5)
        # textStartDate = wx.TextCtrl(panel, value=script_vars["StartDate"], name="StartDate")
        # sizer.Add(textStartDate, pos=(1, 1), flag=wx.EXPAND | wx.ALL, border=5)
        # textStartDate.Bind(wx.EVT_TEXT, self.OnEdited)
        #
        # labelEndDate = wx.StaticText(panel, label="End date:")
        # sizer.Add(labelEndDate, pos=(2, 0), flag=wx.ALL, border=5)
        # textEndDate = wx.TextCtrl(panel, value=script_vars["EndDate"], name="EndDate")
        # sizer.Add(textEndDate, pos=(2, 1), flag=wx.EXPAND | wx.ALL, border=5)
        # textEndDate.Bind(wx.EVT_TEXT, self.OnEdited)

        # buttonOK = wx.Button(panel, label="OK")
        # sizer.Add(buttonOK, pos=(1, 2), flag=wx.ALL, border=5)
        # buttonOK.Bind(wx.EVT_BUTTON, self.OnClicked)
        #
        # buttonCancel = wx.Button(panel, label="Cancel")
        # sizer.Add(buttonCancel, pos=(2, 2), flag=wx.ALL, border=5)
        # buttonCancel.Bind(wx.EVT_BUTTON, self.OnClicked)

        panel.SetSizerAndFit(sizer)

        self.Center()
        self.Show()

    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", btn)

    def OnEdited(self, event):
        text_value = event.GetEventObject().GetValue()
        text_name = event.GetEventObject().GetName()
        print(text_name, "=", text_value)
        script_vars[text_name] = text_value


def dialog_statictext(label, **kwargs):
    # print(label, "kwargs>>>")
    for key in kwargs:
        print(key, "->", kwargs[key])
    # return title
    x = DialogItem
    x.Label = label
    x.Type = "statictext"
    return x


def dialog_textctrl(label, variable, **kwargs):
    x = DialogItem
    x.Label = label
    x.Variable = variable
    x.Type = "textctrl"
    for key in kwargs:
        # print(key, "->", kwargs[key])
        if key == "span":
            x.Span = kwargs[key]
    return x


class DialogItem:
    Label = ""
    Type = "statictext"  # default
    Variable = ""
    Span = (1, 1)        # default


dialog_display_dict = {
    0: "PALC dlg",
    1: dialog_textctrl(label="PRISM Case Number", variable="PRISMCaseNum", span=(1, 2)),
    # 2: dialog_textctrl(label="Start Date", variable="StartDate"),
    # 3: dialog_textctrl(label="End Date", variable="EndDate")
    # 1: dialog_statictext(label="PRISM Case Number:")
}



app = wx.App()
testDialog(None, title='PALC Calculator Demo', contents=dialog_display_dict)
app.MainLoop()

print(script_vars["PRISMCaseNum"])
print(dialog_display_dict[1].Span)
