TypeLorem(){
    SetKeyDelay 0, 150  ; Sets delay between keystrokes
    SendEvent "{Blind}Lorem ipsum dolor sit amet, consectetur adipiscing"  ; Type, {Blind} disables extra functions.
    Sleep 200
    SendEvent "^a {BS}"  ; Simulates select all and backspace
}

Run "winword.exe"  ; Run Microsoft Word
Sleep 5000

if WinExist("Word")
    WinActivate ; Use the window found by WinExist
TypeLorem ; Type after a delay of 3000ms.
if WinExist("Word")
    WinKill ; Use the window found by WinExist.

Exit ; Terminate script
