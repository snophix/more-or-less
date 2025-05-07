"""
This game is simple :
- 

This program requires wxPython to be installed.
"""
import wx
import MainFrame

if __name__ == "__main__":
    app = wx.App()
    mainFrameStyle = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
    mainFrame = MainFrame.MainFrame(None, style=mainFrameStyle)
    mainFrame.Show()
    app.MainLoop()