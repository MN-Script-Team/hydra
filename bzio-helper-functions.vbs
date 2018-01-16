' ----------------------------------- NEW FUNCTIONS FOR FUNCLIB FOR WIN10 ONLY

' Replaces BeginDialog, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function BeginDialog(dlgID_var, dlgPosX_num, dlgPosY_num, dlgWidth_num, dlgHeight_num, dlgTitle_text)
    ' Assigns a numeric value to the dlgID_var
    last_dlgID = "dlg_" & global_dlgcontrolIDs
    dlgID_var = last_dlgID

    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    dlgWidth_num = round(dlgWidth_num * resize_factor)
    dlgHeight_num = round(dlgHeight_num * resize_factor)

    ' Creating a new string which contains dialog details, erasing any previous contents for the variable
    DlgLast = "BeginDialog|" & _
              dlgWidth_num & "|" & _
              dlgHeight_num & "|" & _
              dlgTitle_text


    global_dlgcontrolIDs = global_dlgcontrolIDs + 1
end function

' This is just a dummy script function to allow the script files themselves to exist as-is without issue.
function ButtonGroup(ButtonPressed)
    ' This is just a dummy script function to allow the script files themselves to exist as-is without issue.
end function

' Replaces CancelButton, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function CancelButton(posX_num, posY_num, width_num, height_num)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, erasing any previous contents for the variable (BeginDialog does this)
    DlgLast = DlgLast + "|~|" & _
              "Button|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              "Cancel" & "|" & _
              0
end function

' Replaces CheckBox, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function CheckBox(posX_num, posY_num, width_num, height_num, list_text, variable)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, adding contents to the variable
    DlgLast = DlgLast + "|~|" & _
              "CheckBox|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              replace(list_text, chr(9), "+chr(9)+") & "|" & _
              variable_array(global_dlgcontrolIDs)


    global_dlgcontrolIDs = global_dlgcontrolIDs + 1
end function

' Replaces ComboBox, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function ComboBox(posX_num, posY_num, width_num, height_num, list_text, variable)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, adding contents to the variable
    DlgLast = DlgLast + "|~|" & _
              "ComboBox|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              replace(list_text, chr(9), "+chr(9)+") & "|" & _
              variable_array(global_dlgcontrolIDs)


    global_dlgcontrolIDs = global_dlgcontrolIDs + 1
end function

' Replaces Dialog, which is normally provided by BlueZone Script Host. Uses execute_cmd_with_stdout to execute Hydra's dialog engine, then executes the stdout
'   from Hydra, which assigns variables, similar to how BlueZone Script Host did it. But this time, it works on Windows 10.
function Dialog(dialog_to_display)

    stdout_return = execute_cmd_with_stdout("D:\hydra\dist\hydravbdlg\hydravbdlg.exe """ & DlgDictionary.item(dialog_to_display)) & """"
    MsgBox stdout_return
    wscript.echo stdout_return  ' TODO: comment this out when not in use for testing

    ' stdout_return contains some lines of executable VBScript, returned from hydravbdlg.py. Those lines are prefixed "RETURN-->" and contain our variables.
    output_array = split(stdout_return, vbNewLine)

    for each line in output_array
        if left(trim(line), 9) = "RETURN-->" then
            executeglobal replace(trim(line), "RETURN-->", "")
        end if
    next

end function

' Replaces DropListBox, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function DropListBox(posX_num, posY_num, width_num, height_num, list_text, variable)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, adding contents to the variable
    DlgLast = DlgLast + "|~|" & _
              "DropListBox|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              replace(list_text, chr(9), "+chr(9)+") & "|" & _
              variable_array(global_dlgcontrolIDs)


    global_dlgcontrolIDs = global_dlgcontrolIDs + 1
end function

' Replaces EditBox, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function EditBox(posX_num, posY_num, width_num, height_num, variable)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, adding contents to the variable
    DlgLast = DlgLast + "|~|" & _
              "EditBox|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              variable & "|" & _
              variable_array(global_dlgcontrolIDs)


    global_dlgcontrolIDs = global_dlgcontrolIDs + 1
end function

' Opens a conversation with the BlueZone Display session. The Connect command must be called before any other BlueZone Host Automation object methods that
'   access data in the host screen. Connect auto-connects to the BlueZone session that launched the BlueZone Object or it searches for the first available
'   session if launched from BlueZone desktop when no short name session identifier is specified.
function EMConnect(SessionShortName)
	bz.Connect SessionShortName
end function

' Brings the BlueZone Display session window into the foreground.
function EMFocus()
	bz.Focus
end function

' Retrieves the host screen cursor position.
function EMGetCursor(RowVal, ColumnVal)
	bz.GetCursor RowVal, ColumnVal
end function

' Retrieves data from the host screen.
function EMReadScreen(BufferStr, LengthVal, RowVal, ColumnVal)
	bz.ReadScreen BufferStr, LengthVal, RowVal, ColumnVal
end function

' Searches the host screen for some specified text.
function EMSearch(SearchStr, RowVal, ColumnVal)
	bz.Search SearchStr, RowVal, ColumnVal
end function

' Sends a sequence of keys to the display session.
function EMSendKey(KeyStr)
	bz.SendKey KeyStr
end function

' Sets the host screen cursor position.
function EMSetCursor(RowVal, ColumnVal)
	bz.SetCursor RowVal, ColumnVal
end function

' Suspends script execution until the host screen is ready for keyboard input.
function EMWaitReady(TimeoutVal, ExtraWaitVal)
	bz.WaitReady TimeoutVal, ExtraWaitVal
end function


' Pastes the specified text into the host screen.
function EMWriteScreen(WriteStr, RowVal, ColumnVal)
	bz.WriteScreen WriteStr, RowVal, ColumnVal
end function

' Replaces EndDialog, which is normally provided by BlueZone Script Host. Adds DlgLast to the DlgDictionary
function EndDialog
    DlgDictionary.add last_dlgID, DlgLast
end function

' Executes a commandline command, and captures the stdout details, which can then be used to retrieve data for VBScript. It's a workaround for Python and Hydra,
' which allows communication (dialogs) without creating COM objects.
Function execute_cmd_with_stdout(command)
   Set objWSH = CreateObject("WScript.Shell")               ' Needs an object!
   Set executed_cmd = objWSH.exec(command)                  ' .exec gets the output stream
   execute_cmd_with_stdout = executed_cmd.StdOut.ReadAll()  ' Return the standard output
End Function

' Replaces GroupBox, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function GroupBox(posX_num, posY_num, width_num, height_num, title_text)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, erasing any previous contents for the variable (BeginDialog does this)
    DlgLast = DlgLast + "|~|" & _
              "GroupBox|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              title_text & "|" & _
              ""
end function

' Replaces OKButton, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function OKButton(posX_num, posY_num, width_num, height_num)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, erasing any previous contents for the variable (BeginDialog does this)
    DlgLast = DlgLast + "|~|" & _
              "Button|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              "OK" & "|" & _
              -1
end function

' Parses a script file to collect information about it's dialogs
function parse_and_execute_bzs(filename)
	' Getting script file including dialogs
    ' If it's a URL, it needs to act differently than if it's a local file
    if left(lcase(filename), 4) <> "http" then
    	Set run_another_script_fso = CreateObject("Scripting.FileSystemObject")
    	Set fso_command = run_another_script_fso.OpenTextFile(filename)
    	text_from_the_other_script = fso_command.ReadAll
    	fso_command.Close
    else
        SET req = CreateObject("Msxml2.XMLHttp.6.0")				'Creates an object to get a url
        req.open "GET", filename, FALSE							    'Attempts to open the url
        req.send													'Sends request
        IF req.Status = 200 THEN									'200 means great success
            Set fso = CreateObject("Scripting.FileSystemObject")	'Creates an FSO
            text_from_the_other_script = req.responseText   		'Gets the script code
        ELSE														'Error message
            critical_error_msgbox = MsgBox ("Something has gone wrong getting script info from online repository.")
            StopScript
        END IF

    end if

    ' Splitting the text into an array for easier manipulation
	file_array = split(text_from_the_other_script, vbLf)

	' Simple incrementer to be used in the following loop
	i__ = 0


	' Create an array of variable IDs for controls, which can be compared against the controls as displayed in dialogs
	For each line_of_script in file_array

		set Line = new Script_Line
		Line.AddOriginal(line_of_script)

		if left(trim(Line.Original), 1) <> "'" then   ' It shouldn't load from comments
			If Line.LCheck("begindialog") then
				line_iteration = split(Line.Original, ",")
				variable_name = trim(replace(lcase(line_iteration(0)), "begindialog", ""))
				ReDim Preserve variable_array(i__)
				variable_array(i__) = variable_name
				wscript.echo i__ & ": " & variable_name
				i__ = i__ + 1
			ElseIf Line.LCheck("editbox") then
				line_iteration = split(Line.Original, ",")
				variable_name = trim(lcase(line_iteration(4)))
				ReDim Preserve variable_array(i__)
				variable_array(i__) = variable_name
				wscript.echo i__ & ": " & variable_name
				i__ = i__ + 1
			ElseIf Line.LCheck("checkbox") then
				line_iteration = split(Line.Original, ",")
				variable_name = trim(lcase(line_iteration(5)))
				ReDim Preserve variable_array(i__)
				variable_array(i__) = variable_name
				wscript.echo i__ & ": " & variable_name
				i__ = i__ + 1
			ElseIf Line.LCheck("droplistbox") then
				line_iteration = split(Line.Original, ",")
				variable_name = trim(lcase(line_iteration(5)))
				ReDim Preserve variable_array(i__)
				variable_array(i__) = variable_name
				wscript.echo i__ & ": " & variable_name
				i__ = i__ + 1
			ElseIf Line.LCheck("combobox") then
				line_iteration = split(Line.Original, ",")
				variable_name = trim(lcase(line_iteration(5)))
				ReDim Preserve variable_array(i__)
				variable_array(i__) = variable_name
				wscript.echo i__ & ": " & variable_name
				i__ = i__ + 1
            ElseIf Line.LCheck("pushbutton") then
				line_iteration = split(Line.Original, ",")
				variable_name = trim(lcase(line_iteration(5)))
				ReDim Preserve variable_array(i__)
				variable_array(i__) = variable_name
				wscript.echo i__ & ": " & variable_name
				i__ = i__ + 1
			End if
		end if

        ' Clear the line
		set Line = nothing

	Next

    '...execute the code, now that details have been loaded
	Execute text_from_the_other_script
end function

' Replaces PushButton, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function PushButton(posX_num, posY_num, width_num, height_num, title_text, variable)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, adding contents to the variable
    DlgLast = DlgLast + "|~|" & _
              "Button|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              title_text & "|" & _
              global_dlgcontrolIDs


    global_dlgcontrolIDs = global_dlgcontrolIDs + 1
end function

' Stops a script from continuing.
function StopScript()
	wscript.quit
end function

' Replaces Text, which is normally provided by BlueZone Script Host. Simply adds appropriate text to the DlgLast variable.
function Text(posX_num, posY_num, width_num, height_num, title_text)
    ' Resizing (because BZSH renders dialogs larger than the straight pixel amount)
    width_num = round(width_num * resize_factor)
    height_num = round(height_num * resize_factor)
    posX_num = round(posX_num * resize_factor)
    posY_num = round(posY_num * resize_factor)

    ' Creating a new string which contains dialog details, erasing any previous contents for the variable (BeginDialog does this)
    DlgLast = DlgLast + "|~|" & _
              "Text|" & _
              posX_num & "|" & _
              posY_num & "|" & _
              width_num & "|" & _
              height_num & "|" & _
              title_text & "|" & _
              ""
end function

' ----------------------------------------------------------------------------------------------------- CLASSES WE NEED

' Useful for rendering the line in different ways and determining the contents of each line, for iterating through dialogs
class Script_Line

    ' Adds the original line to the script, after trimming the contents (we use this for determining contents)
	public sub AddOriginal(line)
		original = trim(line) ' has to trim the line, otherwise debug functions display too many newlines and an overflow error can occur
	end sub

    ' A public method to store the original line, for use later when we have to execute the line
	public original

    ' Searches inside the left of a string for another string, helpful for determining if a line contains a specific command
	public function LCheck(string_to_check)
        stringLenth = len(string_to_check)
        if left(trim(lower), stringLenth) = lcase(string_to_check) then
            lcheck = true
        else
            lcheck = false
        end if
	end function

    ' Lower-cases the line
	public function lower
		lower = lcase(original)
	end function

    ' Upper-cases the line
	public function upper
		upper = ucase(original)
	end function
end class


' ----------------------------------------------------------------------------------------------------- VARIABLES WE NEED


DlgLast = "no dialog declared"                              ' A string which will contain the last known dialog contents
Set DlgDictionary = CreateObject("Scripting.Dictionary")    ' A dialog dictionary
resize_factor = 1.6                                         ' The default sizes are about 1.55 times the declared sizes in BZSH.exe... this compensates.
variable_array = array()	                                ' A blank array which various functions will use to contain a list of variables
global_dlgcontrolIDs = 0                                    ' Creates a variable for dlgIDs... this can be used by the dictionary to load the correct dialog
last_dlgID = 0                                              ' Each dialog gets it's own ID, the first one should be 0
Set bz = CreateObject( "BZWhll.WhllObj" )                   ' An object for BZWhll.WhllObj, provided by Rocket in BZWhll.dll
