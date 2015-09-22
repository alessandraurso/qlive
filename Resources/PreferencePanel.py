# encoding: utf-8

import wx
import QLiveLib
from constants import *

class GeneralPrefsTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.tooltipsCheckBox = wx.CheckBox(self, -1, "Use tooltips", style=wx.ALIGN_RIGHT)
        self.tooltipsCheckBox.SetValue(QLiveLib.getVar("useTooltips"))
        self.Bind(wx.EVT_CHECKBOX, self.enableTooltips, self.tooltipsCheckBox)

        box = wx.StaticBox(self, -1, "General settings")
        bsizer = wx.StaticBoxSizer(box, wx.VERTICAL, )
        bsizer.Add(self.tooltipsCheckBox, 0, wx.TOP|wx.LEFT, 10)

        border = wx.BoxSizer()
        border.Add(bsizer, 1, wx.EXPAND|wx.ALL, 10)
        self.SetSizer(border)

    def enableTooltips(self, state):
        QLiveLib.setVar("useTooltips", state.GetEventObject().GetValue())

#TODO: needs better GUI design
class AudioPrefsTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Setting audio driver
        audioDriverDefault = QLiveLib.getVar("audio")
        audioDriverLabel = wx.StaticText(self, -1, "Audio driver:")
        self.audioDriverCB = wx.ComboBox(self, -1, audioDriverDefault, wx.DefaultPosition,
                         wx.DefaultSize, AUDIO_DRIVERS, wx.CB_READONLY|wx.TE_PROCESS_ENTER)
        self.audioDriverCB.Bind(wx.EVT_COMBOBOX, self.setAudioDriver, self.audioDriverCB)

        # Portaudio: Audio Input devices
        self.inputDeviceLabel = wx.StaticText(self, -1, "Audio Input (portaudio):")

        availableAudioIns = []
        for d in QLiveLib.getVar("availableAudioInputs"):
            availableAudioIns.append(QLiveLib.ensureNFD(d))
        initInput = QLiveLib.ensureNFD(QLiveLib.getVar("audioInput"))
        self.inputDeviceCB = wx.ComboBox(self, -1, initInput, wx.DefaultPosition,
                         wx.DefaultSize, availableAudioIns, wx.CB_READONLY|wx.TE_PROCESS_ENTER)
        self.inputDeviceCB.Bind(wx.EVT_COMBOBOX, self.setInputDevice, self.inputDeviceCB)

        # Portaudio: Audio Output devices
        self.outputDeviceLabel = wx.StaticText(self, -1, "Audio Output (portaudio):")
        availableAudioOuts = []
        for d in QLiveLib.getVar("availableAudioOutputs"):
            availableAudioOuts.append(QLiveLib.ensureNFD(d))
        initOutput = QLiveLib.ensureNFD(QLiveLib.getVar("audioOutput"))
        self.outputDeviceCB = wx.ComboBox(self, -1, initOutput, wx.DefaultPosition,
                         wx.DefaultSize, availableAudioOuts, wx.CB_READONLY|wx.TE_PROCESS_ENTER)
        self.outputDeviceCB.Bind(wx.EVT_COMBOBOX, self.setOutputDevice, self.outputDeviceCB)

        # Setting buffer size
        bufferSizeDefault = QLiveLib.getVar("bufferSize")
        bufferSizeLabel = wx.StaticText(self, -1, "Buffer size:")
        self.bufferSizeCB = wx.ComboBox(self, -1, bufferSizeDefault, wx.DefaultPosition,
                         wx.DefaultSize, BUFFER_SIZES, wx.CB_READONLY|wx.TE_PROCESS_ENTER)
        self.bufferSizeCB.Bind(wx.EVT_COMBOBOX, self.setBufferSize, self.bufferSizeCB)

        # Setting sampling rate
        samplingRateDefault = QLiveLib.getVar("sr")
        samplingRateLabel = wx.StaticText(self, -1, "Sampling rate:")
        self.samplingRateCB = wx.ComboBox(self, -1, samplingRateDefault, wx.DefaultPosition,
                         wx.DefaultSize, SAMPLE_RATES, wx.CB_READONLY|wx.TE_PROCESS_ENTER)
        self.samplingRateCB.Bind(wx.EVT_COMBOBOX, self.setSamplingRate, self.samplingRateCB)

        # Setting duplex True/False
        duplexDefault = QLiveLib.getVar("duplex")
        duplexLabel = wx.StaticText(self, -1, "Duplex:")
        self.duplexCB = wx.CheckBox(self, -1, "", style=wx.ALIGN_LEFT)
        self.duplexCB.SetValue(bool(int(QLiveLib.getVar("duplex"))))
        self.duplexCB.Bind(wx.EVT_CHECKBOX, self.setDuplex, self.duplexCB)

        # Main box
        box = wx.StaticBox(self, -1, "Audio settings")

        # Sizers
        vsizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        hsizerAudioDriver = wx.BoxSizer(wx.HORIZONTAL)
        hsizerInputDevice = wx.BoxSizer(wx.HORIZONTAL)
        hsizerOutputDevice = wx.BoxSizer(wx.HORIZONTAL)
        hsizerBufferSize  = wx.BoxSizer(wx.HORIZONTAL)
        hsizerSamplingRate  = wx.BoxSizer(wx.HORIZONTAL)
        hsizerDuplex  = wx.BoxSizer(wx.HORIZONTAL)

        hsizerAudioDriver.Add(audioDriverLabel, -1, wx.ALL|wx.ALIGN_CENTER, 3)
        hsizerAudioDriver.Add(self.audioDriverCB, -1, wx.ALL, 3)

        hsizerInputDevice.Add(self.inputDeviceLabel, -1, wx.ALL|wx.ALIGN_CENTER, 3)
        hsizerInputDevice.Add(self.inputDeviceCB, -1, wx.ALL, 3)

        hsizerOutputDevice.Add(self.outputDeviceLabel, -1, wx.ALL|wx.ALIGN_CENTER, 3)
        hsizerOutputDevice.Add(self.outputDeviceCB, -1, wx.ALL, 3)

        hsizerBufferSize.Add(bufferSizeLabel, -1, wx.ALL|wx.ALIGN_CENTER , 3)
        hsizerBufferSize.Add(self.bufferSizeCB, -1, wx.ALL, 3)

        hsizerSamplingRate.Add(samplingRateLabel, -1, wx.ALL|wx.ALIGN_CENTER , 3)
        hsizerSamplingRate.Add(self.samplingRateCB, -1, wx.ALL, 3)

        hsizerDuplex.Add(duplexLabel, -1, wx.ALL|wx.ALIGN_CENTER , 3)
        hsizerDuplex.Add(self.duplexCB, -1, wx.ALL, 3)

        vsizer.AddSpacer(5)
        vsizer.Add(hsizerAudioDriver, 0, wx.ALL|wx.EXPAND, 0)
        vsizer.Add(hsizerInputDevice, 0, wx.ALL|wx.EXPAND, 0)
        vsizer.Add(hsizerOutputDevice, 0, wx.ALL|wx.EXPAND, 0)
        vsizer.Add(hsizerBufferSize, 0, wx.ALL|wx.EXPAND, 0)
        vsizer.Add(hsizerSamplingRate, 0, wx.ALL|wx.EXPAND, 0)
        vsizer.Add(hsizerDuplex, 0, wx.ALL|wx.EXPAND, 0)

        border = wx.BoxSizer()
        border.Add(vsizer, -1, wx.EXPAND|wx.ALL, 5)
        self.SetSizerAndFit(border)

        self.EnableDisablePortaudioOpts()

    def EnableDisablePortaudioOpts(self):
        if QLiveLib.getVar("audio") in ["portaudio", "coreaudio"]:
            enablePortaudioOpts = True
        else:
            enablePortaudioOpts = False
        self.inputDeviceCB.Enable(enablePortaudioOpts)
        self.inputDeviceLabel.Enable(enablePortaudioOpts)
        self.outputDeviceCB.Enable(enablePortaudioOpts)
        self.outputDeviceLabel.Enable(enablePortaudioOpts)

    def setAudioDriver(self, evt):
        QLiveLib.setVar("audio", evt.GetString())
        self.EnableDisablePortaudioOpts()

    def setInputDevice(self, evt):
        #inputIndexes = QLiveLib.getVar("availableAudioInputIndexes")
        #QLiveLib.setVar("audioInput", inputIndexes[QLiveLib.getVar("availableAudioInputs").index(evt.GetString())])
        QLiveLib.setVar("audioInput", evt.GetString())

    def setOutputDevice(self, evt):
        #outputIndexes = QLiveLib.getVar("availableAudioOutputIndexes")
        #QLiveLib.setVar("audioOutput", outputIndexes[QLiveLib.getVar("availableAudioOutputs").index(evt.GetString())])
        QLiveLib.setVar("audioOutput", evt.GetString())

    def setBufferSize(self, evt):
        QLiveLib.setVar("bufferSize", evt.GetString())

    def setSamplingRate(self, evt):
        QLiveLib.setVar("sr", evt.GetString())

    def setDuplex(self, state):
        if state.GetEventObject().GetValue() == True:
            QLiveLib.setVar("duplex", "1")
        else:
            QLiveLib.setVar("duplex", "0")

#TODO: needs better var names
class PreferenceFrame(wx.Dialog):
    def __init__(self, parent):
        style = wx.DEFAULT_FRAME_STYLE | wx.FRAME_FLOAT_ON_PARENT
        wx.Dialog.__init__(self, parent, title="QLive Preferences", style=style, size=(500, 350))
        self.parent = parent

        # Create a panel and notebook (tabs holder)
        panel = wx.Panel(self)
        nb = wx.Notebook(panel)
        closeButton = wx.Button(panel, -1, label="Close")
        closeButton.Bind(wx.EVT_BUTTON, self.onClose)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        # Create the tab windows
        tab1 = AudioPrefsTab(nb)
        tab2 = GeneralPrefsTab(nb)

        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Audio")
        nb.AddPage(tab2, "General")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nb, 0, wx.EXPAND)
        sizer.Add(closeButton, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizerAndFit(sizer)
        Y = panel.GetSize()[1]
        self.SetSize((500, Y+35))

    def onClose(self, evt):
        self.Destroy()

