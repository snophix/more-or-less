# Copyright © 2025 Moulay Ali "Snophix" Balouz
import wx
from random import randint

"""
After so much time getting used to C++
python feels strange, espacially with OOP
like why do i need to use the self keyword so much, like why?
"""



# all the consts
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

SUBTEXT_TRIES = " tries left"
SUBTEXT_TRY = " try left"
SUBTEXT_REVEAL = "It was "

BUTTON_SUBMIT = "Submit"
BUTTON_REPLAY = "Replay"

RANDOM_MIN = 1
RANDOM_MAX = 10_000

NUMBER_OF_TRIES = 10

WINDOW_SIZE = wx.Size(300, 250)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        # used to have a parent ot evry widget
        self.mainPanel = wx.Panel(self)
        
        # do more setup
        self.setup_controls()
        self.setup_sizers()
        self.setup_binds()

        # now we setup the frame
        self.SetSize(WINDOW_SIZE)

        # then we setup the variable
        self.reset_game()
        


    def setup_controls(self) -> None:
        # the message text ctrl
        self.messageText = wx.StaticText(self.mainPanel)
        theFont = wx.Font().Bold()
        theFont.SetPointSize(40)
        self.messageText.SetFont(theFont)

        # the subtext text widget
        self.subtextText = wx.StaticText(self.mainPanel)

        # the number picker
        self.numberPickerSpinCtrl = wx.SpinCtrl(self.mainPanel)
        self.numberPickerSpinCtrl.SetMax(10000)
        self.numberPickerSpinCtrl.SetMin(1)

        # the button which can be for choosing/submitting or for replaying
        self.submitButton = wx.Button(self.mainPanel)



    def setup_sizers(self) -> None:
        # the sizer which centers the widgets
        mainBoxSizer = wx.BoxSizer(wx.VERTICAL)
        # the order in which we add each widgets matter
        mainBoxSizer.Add(self.messageText, wx.SizerFlags().Center())
        mainBoxSizer.Add(self.subtextText, wx.SizerFlags().Center().Border(wx.DOWN, 15))
        mainBoxSizer.Add(self.numberPickerSpinCtrl, wx.SizerFlags().Center().Border(wx.DOWN, 15))
        mainBoxSizer.Add(self.submitButton, wx.SizerFlags().Center())

        # the sizer which centers the whole ui
        mainGridSizer = wx.GridSizer(1)# 1 cell only
        mainGridSizer.Add(mainBoxSizer, wx.SizerFlags().Expand().Border(wx.ALL, 5).CentreVertical())

        # now we set the panel's sizer to mainGridSizer
        self.mainPanel.SetSizer(mainGridSizer)
        mainGridSizer.SetSizeHints(self)
        #mainBoxSizer.SetSizeHints(self)



    def setup_binds(self) -> None:
        self.submitButton.Bind(wx.EVT_BUTTON, self.on_submitButton_pressed)
    


    def reset_game(self) -> None:
        # setting the key vars
        self.isGaming = True
        self.randomNumberToGuess = randint(RANDOM_MIN, RANDOM_MAX)
        #self.randomNumberToGuess = 4097
        self.triesLeft = NUMBER_OF_TRIES

        # resetting the widgets
        self.SetTitle(TITLE_BASE + TITLE_ADD_BEGIN)
        self.messageText.SetLabel(MESSAGE_BEGIN)
        self.subtextText.SetLabel(str(self.triesLeft) + SUBTEXT_TRIES)
        self.numberPickerSpinCtrl.Show()
        self.numberPickerSpinCtrl.SetValue(1)
        self.submitButton.SetLabel(BUTTON_SUBMIT)
        self.mainPanel.Layout()



    # event handler for wx.EVT_BUTTON from submitButton
    def on_submitButton_pressed(self, event: wx.Event) -> None:
        #print("pressed")
        #if not gaming then start gaming
        if not self.isGaming:
            self.reset_game()
            return
        
        # so we ARE gaming
        guessedNumber = self.numberPickerSpinCtrl.GetValue()
        # now we verify if the player guessed correctly, as we don't need to know if he is out of guess' now
        if guessedNumber == self.randomNumberToGuess:
            self.finish_game(TITLE_ADD_WIN, MESSAGE_WIN)
            return
        
        # now we verify if he doesn't have any tries left, we don't need to now that it is more or less
        self.triesLeft -= 1
        if self.triesLeft <= 0:
            self.finish_game(TITLE_ADD_LOSE, MESSAGE_LOSE)
            return
        
        # we tell the uiser how much tries/try left
        if self.triesLeft > 1:
            self.subtextText.SetLabel(str(self.triesLeft) + SUBTEXT_TRIES)
        else:
            self.subtextText.SetLabel("1" + SUBTEXT_TRY)
        
        # and now we just tell the player if the number to guess is higher or lower
        if self.randomNumberToGuess < guessedNumber:
            self.messageText.SetLabel(MESSAGE_LESS)
            self.SetTitle(TITLE_LESS)
        else:
            self.messageText.SetLabel(MESSAGE_MORE)
            self.SetLabel(TITLE_MORE)
        self.mainPanel.Layout()
    


    # it handles all the finishing game logic
    def finish_game(self, titleAdd:str, message: str) -> None:
        self.isGaming = False
        self.SetTitle(TITLE_BASE + titleAdd)
        self.messageText.SetLabel(message)
        self.subtextText.SetLabel(SUBTEXT_REVEAL + str(self.randomNumberToGuess))
        self.numberPickerSpinCtrl.Hide()
        self.submitButton.SetLabel(BUTTON_REPLAY)
        self.mainPanel.Layout()