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
Description=我的脚本1
Enable=1
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
MyString = Split("VBScriptXisXfun!", "x", -1, 1)
Text = Plugin.File.ReadFileEx("C:\Users\yun\Desktop\描述.txt")
Msgbox "向目标文件读出文本内容为："& Text
MyArray = Split(Text, "|")
If UBound(MyArray)>=0 Then
    i=0
    For UBound(MyArray)
        //下面这句是得到文本内容
        Msgbox "第 " & i+1 &" 行文本内容为："& Cstr(MyArray(i))
        i=i+1
    Next
End If 

