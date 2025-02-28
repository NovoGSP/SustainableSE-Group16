TypeLorem(){
    SetKeyDelay 0, 150 ; Sets delay between keystrokes
    SendEvent "{Blind}Lorem ipsum dolor sit amet, consectetur adipiscing" ; Type, {Blind} disables extra functions.
    Sleep 200
    SendEvent "^a {BS}"
}
Run "C:\Windows\notepad.exe" ; Run text editor.
Sleep 5000
WinWait "Untitled - Notepad" ;

if WinExist("Untitled - Notepad")
    WinActivate ; Use the window found by WinExist
TypeLorem ; Type after a delay of 3000ms.
if WinExist("Untitled - Notepad")
    WinKill ; Use the window found by WinExist.
Exit ; Terminate script
