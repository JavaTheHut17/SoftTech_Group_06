# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(854, 616), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        # Search Bar
        self.Search = wx.TextCtrl(self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.Search, 0, wx.ALL | wx.EXPAND, 5)

        # Dropdown for Function Choices
        FunctionChoices = [_(u"Nutrition Breakdown"), _(u"Range Filter"), _(u"High Med Low Filter"), _(u"High Low Filter")]
        self.Function = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, FunctionChoices, 0)
        self.Function.SetSelection(0)
        bSizer1.Add(self.Function, 0, wx.ALL | wx.EXPAND, 5)

        # Grid for buttons
        gridSizer = wx.GridSizer(1, 6, 5, 5)

        self.High = wx.Button(self, wx.ID_ANY, _(u"High"), wx.DefaultPosition, wx.DefaultSize, 0)
        gridSizer.Add(self.High, 0, wx.ALL | wx.EXPAND)

        self.Medium = wx.Button(self, wx.ID_ANY, _(u"Medium"), wx.DefaultPosition, wx.DefaultSize, 0)
        gridSizer.Add(self.Medium, 0, wx.ALL | wx.EXPAND)

        self.Low = wx.Button(self, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.DefaultSize, 0)
        gridSizer.Add(self.Low, 0, wx.ALL | wx.EXPAND)

        self.MinValue = wx.TextCtrl(self, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0)
        gridSizer.Add(self.MinValue, 0, wx.ALL | wx.EXPAND)

        self.MaxValue = wx.TextCtrl(self, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0)
        gridSizer.Add(self.MaxValue, 0, wx.ALL | wx.EXPAND)

        # Add "Run Action" Button
        self.Action = wx.Button(self, wx.ID_ANY, _(u"Run Action"), wx.DefaultPosition, wx.DefaultSize, 0)
        gridSizer.Add(self.Action, 0, wx.ALL | wx.EXPAND)

        bSizer1.Add(gridSizer, 0, wx.ALL | wx.EXPAND, 5)

        # Data Grid Panel
        bSizer8 = wx.BoxSizer(wx.VERTICAL)
        sbSizer8 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"Data Grid")), wx.VERTICAL)

        self.m_grid1 = wx.grid.Grid(sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(600, 300), 0)

        # Grid
        self.m_grid1.CreateGrid(10, 5)  # Increased number of rows for more data display
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

        sbSizer8.Add(self.m_grid1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer8.Add(sbSizer8, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass



