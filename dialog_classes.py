import wx
import math


class MAXISCustom (wx.Frame):
    def __init__(self, parent, title, all_elements, continue_text, cancel_yn):
        wx.Frame.__init__(self, parent, id=wx.ID_OPEN, title=title, pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                  style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.STAY_ON_TOP)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        global gbSizer1
        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # wx.StaticText [type, text, row, col, row_span, col_span]
        # wx.ComboBox   [type, list_of_choices, output_variable, starting_value, mandatory, err_msg, row, col, row_span, col_span]
        # wx.Choice     [type, list_of_choices, output_variable, mandatory, err_msg, row, col, row_span, col_span]
        # wx.TextCtrl   [type, output_variable, starting_value, mandatory, err_msg, row, col, row_span, col_span]
        # wx.CheckBox   [type, text, output_variable, row, col, row_span, col_span]

        deflt_row = 0
        deflt_col = 0

        # self.text1 = ""
        # self.text2 = ""
        # self.text3 = ""
        # self.text4 = ""
        # self.text5 = ""
        # self.combo_box1 = ""
        # self.combo_box2 = ""
        # self.combo_box3 = ""
        # self.combo_box4 = ""
        # self.combo_box5 = ""
        # self.choice1 = ""
        # self.choice2 = ""
        # self.choice3 = ""
        # self.choice4 = ""
        # self.choice5 = ""
        # self.text_ctr1 = ""
        # self.text_ctr2 = ""
        # self.text_ctr3 = ""
        # self.text_ctr4 = ""
        # self.text_ctr5 = ""
        # self.check_box1 = ""
        # self.check_box2 = ""
        # self.check_box3 = ""
        # self.check_box4 = ""
        # self.check_box5 = ""

        # static_text_list = [text1, text2, text3, text4, text5]
        #                     # self.text6, self.text7, self.text8, self.text9, self.text10,
        #                     # self.text11, self.text12, self.text13, self.text14, self.text15,
        #                     # self.text16, self.text17, self.text18, self.text19, self.text20,
        #                     # self.text21, self.text22, self.text23, self.text24, self.text25]
        # stl_count = 0
        # combo_box_list = [combo_box1, combo_box2, combo_box3, combo_box4, combo_box5]
        #                   # self.combo_box6, self.combo_box7, self.combo_box8, self.combo_box9, self.combo_box10,
        #                   # self.combo_box11, self.combo_box12, self.combo_box13, self.combo_box14, self.combo_box15,
        #                   # self.combo_box16, self.combo_box17, self.combo_box18, self.combo_box19, self.combo_box20,
        #                   # self.combo_box21, self.combo_box22, self.combo_box23, self.combo_box24, self.combo_box25]
        # cmbl_count = 0
        # choice_list = [choice1, choice2, choice3, choice4, choice5]
        #                # self.choice6, self.choice7, self.choice8, self.choice9, self.choice10,
        #                # self.choice11, self.choice12, self.choice13, self.choice14, self.choice15,
        #                # self.choice16, self.choice17, self.choice18, self.choice19, self.choice20,
        #                # self.choice21, self.choice22, self.choice23, self.choice24, self.choice25]
        # cl_count = 0
        # text_ctrl_list = [text_ctr1, text_ctr2, text_ctr3, text_ctr4, text_ctr5]
        #                   # self.text_ctrl6, self.text_ctrl7, self.text_ctrl8, self.text_ctrl9, self.text_ctrl10,
        #                   # self.text_ctrl11, self.text_ctrl12, self.text_ctrl13, self.text_ctrl14, self.text_ctrl15,
        #                   # self.text_ctrl16, self.text_ctrl17, self.text_ctrl18, self.text_ctrl19, self.text_ctrl20,
        #                   # self.text_ctrl21, self.text_ctrl22, self.text_ctrl23, self.text_ctrl24, self.text_ctrl25]
        # tcl_count = 0
        # check_box_list = [check_box1, check_box2, check_box3, check_box4, check_box5]
        #                   # self.check_box6, self.check_box7, self.check_box8, self.check_box9, self.check_box10,
        #                   # self.check_box11, self.check_box12, self.check_box13, self.check_box14, self.check_box15,
        #                   # self.check_box16, self.check_box17, self.check_box18, self.check_box19, self.check_box20,
        #                   # self.check_box21, self.check_box22, self.check_box23, self.check_box24, self.check_box25]
        # chbl_count = 0

        for x in range(len(all_elements)):
            setattr(self, str(x), "")
            # self.static_text_list[x] = ""
            # self.combo_box_list[x] = ""
            # self.choice_list[x] = ""
            # self.text_ctrl_list[x] = ""
            # self.check_box_list[x] = ""

        x = 0
        for elements in all_elements:
            # print("Default Row - %s" %(deflt_row))
            # print("Default Col - %s" %(deflt_col))
            x = str(x)
            if elements[0] is "StaticText":
                text = elements[1]

                if len(elements) >= 4:
                    row = elements[2]
                    col = elements[3]
                else:
                    row = deflt_row
                    col = deflt_col

                if len(elements) >= 6:
                    row_span = elements[4]
                    col_span = elements[5]
                else:
                    if len(text) >= 90:
                        if col != 0:
                            row = row + 1
                            col = 0
                        row_span = int(math.ceil(len(text) / 90))
                        col_span = 6
                        running_len = 0
                        word_list = text.split(" ")
                        text = ""
                        for word in word_list:
                            running_len += len(word)
                            if running_len > 90:
                                text = "%s \n %s" % (text, word)
                                running_len = len(word)
                            else:
                                text = "%s %s" % (text, word)
                                running_len += 1
                    else:
                        row_span = 1
                        col_span = int(math.ceil(len(text) / 15))

                deflt_col = col + col_span
                if row_span > 1:
                    deflt_row = row + row_span
                if deflt_col >= 6:
                    deflt_col = 0
                    deflt_row += 1

                # print("text row - " + str(row))
                # print("text col - " + str(col))
                # print("text row span - " + str(row_span))
                # print("text col span - " + str(col_span))
                # self.static_text_list[stl_count] = ""
                self.x = wx.StaticText(self, wx.ID_ANY, text, wx.DefaultPosition, wx.DefaultSize, 0)
                # slf.static_text_list[stl_count].Wrap(-1)
                gbSizer1.Add(self.x, wx.GBPosition(row, col), wx.GBSpan(row_span, col_span), wx.ALL | wx.ALIGN_RIGHT, 5)

                # stl_count += 1
                elements.append(x)

            if elements[0] is "ComboBox":
                combo_choices = elements[1]
                max_len = 0
                for choices in combo_choices:
                    if len(choices) > max_len:
                        max_len = len(choices)

                if len(elements) >= 4:
                    start_value = elements[3]
                else:
                    start_value = wx.EmptyString

                if len(elements) >= 8:
                    row = elements[6]
                    col = elements[7]
                else:
                    row = deflt_row
                    col = deflt_col

                if len(elements) >= 10:
                    row_span = elements[8]
                    col_span = elements[9]
                else:
                    row_span = 1
                    col_span = int(math.ceil(max_len) / 15)

                if col_span < 1:
                    col_span = 1

                deflt_col = col + col_span
                if row_span > 1:
                    deflt_row = row + row_span
                if deflt_col >= 6:
                    deflt_col = 0
                    deflt_row += 1

                # print("combo row - " + str(row))
                # print("combo col - " + str(col))

                self.x = wx.ComboBox(self, wx.ID_ANY, start_value, wx.DefaultPosition, wx.DefaultSize, combo_choices, 0)
                gbSizer1.Add(self.x, wx.GBPosition(row, col), wx.GBSpan(row_span, col_span), wx.ALL | wx.EXPAND, 5)

                # cmbl_count += 1
                elements.append(x)

            if elements[0] is "Choice":
                combo_choices = elements[1]
                max_len = 0
                for choices in combo_choices:
                    if len(choices) > max_len:
                        max_len = len(choices)

                if len(elements) >= 7:
                    row = elements[5]
                    col = elements[6]
                else:
                    row = deflt_row
                    col = deflt_col

                if len(elements) >= 9:
                    row_span = elements[7]
                    col_span = elements[8]
                else:
                    row_span = 1
                    col_span = int(math.ceil(max_len) / 15)
                if col_span < 1:
                    col_span = 1

                deflt_col = col + col_span
                if row_span > 1:
                    deflt_row = row + row_span
                if deflt_col >= 6:
                    deflt_col = 0
                    deflt_row += 1

                # print("choice row - " + str(row))
                # print("choice col - " + str(col))

                self.x = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, combo_choices, 0)
                self.x.SetSelection(0)
                gbSizer1.Add(self.x, wx.GBPosition(row, col), wx.GBSpan(row_span, col_span), wx.ALL | wx.EXPAND, 5)

                # cl_count += 1
                elements.append(x)

            if elements[0] is "TextCtrl":
                if len(elements) >= 3:
                    start_value = elements[2]
                else:
                    start_value = wx.EmptyString

                if len(elements) >= 7:
                    row = elements[5]
                    col = elements[6]
                else:
                    row = deflt_row
                    col = deflt_col

                if len(elements) >= 9:
                    row_span = elements[7]
                    col_span = elements[8]
                else:
                    row_span = 1
                    col_span = 6 - col

                deflt_col = 0

                deflt_row = row + row_span

                if deflt_col >= 6:
                    deflt_col = 0
                    deflt_row += 1

                # print("editbox row - " + str(row))
                # print("editbox col - " + str(col))

                self.x = wx.TextCtrl(self, wx.ID_ANY, start_value, wx.DefaultPosition, wx.DefaultSize, 0)
                gbSizer1.Add(self.x, wx.GBPosition(row, col), wx.GBSpan(row_span, col_span), wx.ALL | wx.EXPAND, 5)

                # tcl_count += 1
                elements.append(x)

            if elements[0] is "CheckBox":
                text = elements[1]

                if len(elements) >= 5:
                    row = elements[3]
                    col = elements[4]
                else:
                    row = deflt_row
                    col = deflt_col

                if len(elements) >= 7:
                    row_span = elements[5]
                    col_span = elements[6]
                else:
                    if len(text) >= 90:
                        if col != 0:
                            row = row + 1
                            col = 0
                        row_span = int(math.ceil(len(text) / 90))
                        col_span = 6
                    else:
                        row_span = 1
                        col_span = int(math.ceil(len(text) / 15))

                deflt_col = col + col_span
                if row_span > 1:
                    deflt_row = row + row_span
                if deflt_col >= 6:
                    deflt_col = 0
                    deflt_row += 1

                # print("check row - " + str(row))
                # print("check col - " + str(col))

                self.x = wx.CheckBox(self, wx.ID_ANY, text, wx.DefaultPosition, wx.DefaultSize, 0)
                gbSizer1.Add(self.x, wx.GBPosition(row, col), wx.GBSpan(row_span, col_span), wx.ALL, 5)

                # chbl_count += 1
                elements.append(x)

            if elements[0] is "Button":
                label = elements[1]

                if len(elements) >= 6:
                    row = elements[4]
                    col = elements[5]
                else:
                    row = deflt_row
                    col = deflt_col

                if len(elements) >= 8:
                    row_span = elements[6]
                    col_span = elements[7]
                else:
                    row_span = 1
                    col_span = int(math.ceil(len(label) / 15))


                deflt_col = col + col_span
                if row_span > 1:
                    deflt_row = row + row_span
                if deflt_col >= 6:
                    deflt_col = 0
                    deflt_row += 1

                self.x = wx.Button(self, wx.ID_ANY, label, wx.DefaultPosition, wx.DefaultSize, 0)

                if elements[3] is True:
                    width = 7 * len(label)
                    self.x.SetMaxSize(wx.Size(width, 17))
                gbSizer1.Add(self.x, wx.GBPosition(row, col), wx.GBSpan(row_span, col_span), wx.ALL, 5)


            x = int(x)
            x += 1

        continue_text = continue_text.upper()
        row = deflt_row + 1

        if  cancel_yn:
            if continue_text is "OK":
                self.continue_button = wx.Button(self, wx.ID_OK)
                gbSizer1.Add(self.continue_button, wx.GBPosition(row, 4), wx.GBSpan(1, 1), wx.ALL, 5)
            else:
                self.continue_button = wx.Button(self, wx.ID_ANY, continue_text)
                gbSizer1.Add(self.continue_button, wx.GBPosition(row, 4), wx.GBSpan(1, 1), wx.ALL, 5)

            self.cancel_button = wx.Button(self, wx.ID_CANCEL)
            gbSizer1.Add(self.cancel_button, wx.GBPosition(row, 5), wx.GBSpan(1, 1), wx.ALL, 5)
        else:
            if continue_text is "OK":
                self.continue_button = wx.Button(self, wx.ID_OK)
                gbSizer1.Add(self.continue_button, wx.GBPosition(row, 5), wx.GBSpan(1, 1), wx.ALL, 5)
            else:
                self.continue_button = wx.Button(self, wx.ID_ANY, continue_text)
                gbSizer1.Add(self.continue_button, wx.GBPosition(row, 5), wx.GBSpan(1, 1), wx.ALL, 5)


        self.SetSizer(gbSizer1)
        self.Layout()
        gbSizer1.Fit(self)

        self.Centre(wx.BOTH)

        for elements in all_elements:
            pass    # here be bindings

    def __del__(self):
        pass


app = wx.App()

edit_case_number = ""
MAXIS_case_number = ""
the_choice = ""
cool_checkbox = ""
best_choice = ""
# list1 = ["This one", "Another One", "Last One"]
frame = MAXISCustom(None, "NEW THING", [["StaticText", "ENTER A CASE NUMBER:"],
                                        ["TextCtrl", edit_case_number, "", MAXIS_case_number, True, "Please enter a case number"],
                                        ["StaticText", "Choose"],
                                        ["ComboBox", ["This one", "Another One", "Last One"], the_choice],
                                        ["StaticText", "This is a very long line of text, I have a lot to say. There is a lot of information to convey with a dialog and scripts are great. LOTS more here. Going to keep writing. I can get used to my new keyboard."],
                                        ["CheckBox", "Check me for a reall awesome, fantastic cool thing", cool_checkbox],
                                        ["StaticText", "Did it work           "],
                                        ["StaticText", "Pickone of these - no other choices:"],
                                        ["Choice", ["Small", "Medium", "Large"], best_choice],
                                        ["Button", "Cool Button", "Nav", True, 8, 5],
                                        ["Button", "This button will send the case through background", "bkrnd", True]],
                    "Continue...", False)


# wx.StaticText [type, text, row, col, row_span, col_span]
# wx.ComboBox   [type, list_of_choices, output_variable, starting_value, mandatory, err_msg, row, col, row_span, col_span]
# wx.Choice     [type, list_of_choices, output_variable, mandatory, err_msg, row, col, row_span, col_span]
# wx.TextCtrl   [type, output_variable, starting_value, mandatory, err_msg, row, col, row_span, col_span]
# wx.CheckBox   [type, text, output_variable, row, col, row_span, col_span]
# wx.Button     [type, label, action, constrict_size, row, col, row_span, col_span]
frame.Show()
app.MainLoop()
