"""
Copyright © 2025 Moulay Ali "Snophix" Balouz

This game is simple :
- 

This program requires wxPython to be installed.

Also I am remaking it in C++ with wxWidgets so look out for that :)
"""
import wx
import MainFrame

if __name__ == "__main__":
    app = wx.App()
    mainFrameStyle = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
    mainFrame = MainFrame.MainFrame(None, style=mainFrameStyle)
    mainFrame.Show()
    app.MainLoop()