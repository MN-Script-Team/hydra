import wx


class dialog(wx.Frame):
    def __init__(self, parent, title, all_elements):
        self.widget_output = []

        wx.Frame.__init__(self, parent, id=wx.ID_OPEN, title=title, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                  style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.STAY_ON_TOP)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        global gbSizer1
        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # wx.StaticText [type, name, text, row, col, row_span, col_span]
        # wx.ComboBox   [type, name, list_of_choices, starting_value, output_variable, mandatory, err_msg, row, col, row_span, col_span]
        # wx.Choice     [type, name, list_of_choices, starting_value, output_variable, mandatory, err_msg, row, col, row_span, col_span]
        # wx.TextCtrl   [type, name, starting_value, output_variable, mandatory, err_msg, row, col, row_span, col_span]
        # wx.CheckBox   [type, name, text, output_variable, row, col, row_span, col_span]

        for elements in all_elements:
            if elements[0] is "StaticText":
                name = elements[1]
                text = elements[2]
                row = elements[3]
                self.elements[1] = wx.StaticText(self, wx.ID_ANY, elements[1], wx.DefaultPosition, wx.DefaultSize, 0)
                self.elements[1].Wrap(-1)
                gbSizer1.Add(self.elements[0], wx.GBPosition(elements[2], elements[3]), wx.GBSpan(elements[4], elements[5]), wx.ALL | wx.ALIGN_RIGHT, 5)

            if elements[0] is "ComboBox":
                combo_choices = elements[1]
                self.elements[0] = wx.ComboBox(self, wx.ID_OPEN, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, combo_choices, 0)
                gbSizer1.Add(self.elements[0], wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

            if elements[0] is "Choice":
                pass
            if elements[0] is "TextCtrl":
                pass
            if elements[0] is "CheckBox":
                pass


app = wx.App()

text1 = ""
edit_case_number = ""
MAXIS_case_number = ""
DIALOG = dialog(None, "NEW THING", [["StaticText", text1, "ENTER A CASE NUMBER:"],
                             ["TextCtrl", edit_case_number, "", MAXIS_case_number, True, "Please enter a case number"]])
