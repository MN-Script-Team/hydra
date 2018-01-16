import wx
import win32com.client


class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame."""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,300)) # overriding __init__ to modify the frame behavior
#        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE) # Multiline text box control
        self.CreateStatusBar() # A status bar is a good thing

        # Let's make a menu
        filemenu = wx.Menu()

        # -------------- THIS PART CREATES THE "File" MENU OPTION
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        # menuSendMsgBox = filemenu.Append(wx.ID_NEW, "MsgBox test", " Send test MsgBox to open BZ")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") # Adding "File" to the MenuBar
        self.SetMenuBar(menuBar) # Adding the MenuBar to the Frame content.

        # Event handling -------------------------------------- <<<<< IS THIS WHERE WE COULD BIND EVENTS TO BZ???
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout) # clicking "About" runs self.OnAbout, wx.EVT_MENU = "select menu item" event
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Adding buttons?
        panel = wx.Panel(self, wx.ID_ANY, size=(500, 200))
        button_array = []
        for i in range(0, 3):
            print(i)
            button = wx.Button(panel, id=wx.ID_ANY, label=str(i), pos=(i*100, 30), size=(100, 100) )
            button.Bind(wx.EVT_BUTTON, self.onButton)
            button_array.append(button)
            # button = None

        # Shows frame... prevents us from having to explicitly do frame.Show()
        self.Show(True)

    def onButton(self, event):
        """Fire when its corresponding button is pressed."""
        # TODO: could this write to a variable containing strings to be executed?
        print("Button pressed!")

    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self, "Veronica made this", "About Hydra", wx.OK)

        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

#    def OnNew(self, e):
#        bz.connect("A")
#        bz.MsgBox("What up?")
#        bz.disconnect()
#        setHydra()
#        import win32com.server.register


    def OnExit(self, e):
        self.Close(True)  # Close the frame.




app = wx.App(False)
frame = MyFrame(None, "Hydra test")
app.MainLoop()
