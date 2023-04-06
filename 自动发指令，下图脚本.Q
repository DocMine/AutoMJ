[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=0
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=27e860fa-352a-4400-899b-5cb0f449ef0c
Description=ÎÒµÄ½Å±¾1
Enable=0
AutoRun=0
[Repeat]
Type=0
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]
Dim MyString, MyArray
Text = Plugin.File.ReadFileEx("C:\Users\yun\Desktop\ÃèÊö.txt")
MyArray = Split(Text, "|")
If UBound(MyArray)>=0 Then
    i=0
    For UBound(MyArray)
        MyString = "/imagine prompt " + Cstr(MyArray(i))
        SayString MyString
        KeyPress "Enter", 1
        Delay 10000
        i=i+1
        FindPic 0,0,1024,768,"position.jpg",0.9,intX,intY
			If intX > 0 And intY > 0 Then 
			MoveTo intX, intY - 300
			LeftClick 1
			Delay 1000
			RightClick 1
			Delay 1000
			FindPic 0,0,1024,768,"save.jpg",0.9,saveX,saveY
				If intX > 0 And intY > 0 Then 
				MoveTo saveX, saveY
				LeftClick 1
				KeyPress "Enter", 1
				End If
			End If
    Next
End If 

