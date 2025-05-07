import wx

"""
After so much time getting used to C++
python feels strange, espacially with OOP
"""


TITLE_BASE = "More Or Less"
TITLE_LESS = "Less!!"
TITLE_MORE = "More!!"
TITLE_ADD_BEGIN = "!!"
TITLE_ADD_LOSE = " :("
TITLE_ADD_WIN = " :)"

MESSAGE_BEGIN = "Let's play!"
MESSAGE_LESS = "It's less"
MESSAGE_MORE = "It's more"
MESSAGE_LOSE = "You lost!"
MESSAGE_WIN = "You won!"

BUTTON_SUBMIT = "Submit"
BUTTON_REPLAY = "Replay"


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.SetTitle(TITLE_BASE)

        self.mainPanel = wx.Panel(self)

        self.setup_controls()
        self.setup_sizers()

        self.SetSize(wx.Size(300, 250))



    def setup_controls(self) -> None:
        # the message text ctrl
        self.messageTextCtrl = wx.StaticText(self.mainPanel, label="Let's play!")
        theFont = wx.Font().Bold()
        theFont.SetPointSize(40)
        self.messageTextCtrl.SetFont(theFont)

        # the number picker
        self.numberPickerSpinCtrl = wx.SpinCtrl(self.mainPanel)
        self.numberPickerSpinCtrl.SetMax(10000)
        self.numberPickerSpinCtrl.SetMin(1)

        # the button which can be for choosing/submitting or for replaying
        self.chooseButton = wx.Button(self.mainPanel, label="Submit")


    def setup_sizers(self) -> None:
        # the sizer which 
        mainBoxSizer = wx.BoxSizer(wx.VERTICAL)
        mainBoxSizer.Add(self.messageTextCtrl, wx.SizerFlags().CenterHorizontal().Border(wx.DOWN, 15))
        mainBoxSizer.Add(self.numberPickerSpinCtrl, wx.SizerFlags().CenterHorizontal().Border(wx.DOWN, 15))
        mainBoxSizer.Add(self.chooseButton, wx.SizerFlags().CenterHorizontal())

        mainGridSizer = wx.GridSizer(1)
        mainGridSizer.Add(mainBoxSizer, wx.SizerFlags().Expand().Border(wx.ALL, 5).CentreVertical())

        self.mainPanel.SetSizer(mainGridSizer)
        mainGridSizer.SetSizeHints(self)
        #mainBoxSizer.SetSizeHints(self)
