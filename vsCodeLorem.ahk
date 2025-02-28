TypeLorem(){
    SetKeyDelay 0, 150 ; Sets delay between keystrokes
    SendEvent "{Blind}Lorem ipsum dolor sit amet, consectetur adipiscing" ; Type, {Blind} disables extra functions.
    Sleep 200
    SendEvent "^a {BS}"
    Send "^w" ; Close the tab, otherwise it will be restored when reopened, potentially influencing other runs
}

Run "C:\Users\sotir\AppData\Local\Programs\Microsoft VS Code\Code.exe" ; Run text editor.
Sleep 3600
WinWait "Visual Studio Code" ;
if WinExist("Visual Studio Code")
    WinActivate ;
Sleep 800 ; Short delay to ensure VS Code is ready
Send "^w" ; Close the start tab
Sleep 300 ;
Send "^n" ; Create a new file (Ctrl+N)
Sleep 300 ;
TypeLorem ; Type after a delay of 3000ms.
if WinExist("Visual Studio Code")
    WinKill ; Use the window found by WinExist.
Exit ; Terminate script
