import win32api as wa
import win32con as wcon
import win32com.client as client

wa.SetCursorPos((5000,1))
wa.mouse_event(wcon.MOUSEEVENTF_LEFTDOWN,5000,1,0,0)
wa.mouse_event(wcon.MOUSEEVENTF_LEFTUP,5000,1,0,0)

wa.Sleep(100)

client.Dispatch("WScript.Shell").SendKeys("{ENTER}")
