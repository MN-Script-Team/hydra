' Determine Engine and architecture (this block re-runs scripts in cscript x86 if not initially started that way)
Engine = replace(replace(lcase(WScript.FullName), lcase(wscript.path), ""), "\", "")
If instr(lcase(wscript.path), "system32") then
    Architecture = "x64"
Elseif instr(lcase(wscript.path), "syswow64") then
    Architecture = "x86"
End if
' Create the complete command line to rerun this script in CSCRIPT32, and exit, if not already running in x86 cscript.exe.
If Engine <> "cscript.exe" or Architecture <> "x86" Then
    Set wshShell = CreateObject( "WScript.Shell" )
    wshShell.run "C:\Windows\SysWOW64\CSCRIPT.EXE //NoLogo """ & WScript.ScriptFullName & """"
    wscript.quit
end if

Set run_another_script_fso = CreateObject("Scripting.FileSystemObject")
Set fso_command = run_another_script_fso.OpenTextFile("bzio-helper-functions.vbs")
text_from_the_other_script = fso_command.ReadAll
fso_command.Close
Execute text_from_the_other_script





parse_and_execute_bzs("client-contact.vbs")
' parse_and_execute_bzs("https://raw.githubusercontent.com/MN-Script-Team/DHS-PRISM-Scripts/master/notes/client-contact.vbs")
' EMConnect ""
' EMWriteScreen ComboBox1, 12, 61
