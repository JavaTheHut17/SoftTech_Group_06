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
from f1_search_food import search_food
from f2_nutritionBreakdown import nutrition_breakdown
from f3_rangeFilter import range_filter
from f4_high_med_low_filter import high_med_low_filter
from f5_high_low_filter import high_low_filter
import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    db = 'DataBase/Food_Nutrition_Dataset.csv'

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 973,733 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.Search = wx.TextCtrl( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.Search, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        FunctionChoices = [ _(u"Nutrition Breakdown"), _(u"Range Filter"), _(u"High Med Low Filter"), _(u"High Low Filter"), wx.EmptyString, wx.EmptyString, wx.EmptyString ]
        self.Function = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, FunctionChoices, 0 )
        self.Function.SetSelection( 0 )
        bSizer1.Add( self.Function, 0, wx.ALL|wx.EXPAND, 5 )

        wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.High = wx.Button( self, wx.ID_ANY, _(u"High"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.High, 0, wx.ALL, 5 )

        self.m_button13 = wx.Button( self, wx.ID_ANY, _(u"Medium"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.m_button13, 0, wx.ALL, 5 )

        self.Low = wx.Button( self, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.Low, 0, wx.ALL, 5 )

        self.max_value = wx.TextCtrl( self, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.max_value, 0, wx.ALL, 5 )

        self.min_value = wx.TextCtrl( self, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.min_value, 0, wx.ALL, 5 )

        self.Submit = wx.Button( self, wx.ID_ANY, _(u"Submit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.Submit, 0, wx.ALL, 5 )

        self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid2.CreateGrid( 25, 10 )
        self.m_grid2.EnableEditing( True )
        self.m_grid2.EnableGridLines( True )
        self.m_grid2.EnableDragGridSize( False )
        self.m_grid2.SetMargins( 0, 0 )

        # Columns
        self.m_grid2.EnableDragColMove( False )
        self.m_grid2.EnableDragColSize( True )
        self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid2.AutoSizeRows()
        self.m_grid2.EnableDragRowSize( True )
        self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        wSizer3.Add( self.m_grid2, 0, wx.ALL, 5 )


        bSizer1.Add( wSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8.Add( self.m_panel2, 1, wx.EXPAND, 5 )


        bSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Search.Bind( wx.EVT_TEXT, self.search_input )
        self.Function.Bind( wx.EVT_CHOICE, self.func_choice )
        self.High.Bind( wx.EVT_BUTTON, self.high_toggle )
        self.m_button13.Bind( wx.EVT_BUTTON, self.medium_toggle )
        self.Low.Bind( wx.EVT_BUTTON, self.low_toggle )
        self.Submit.Bind( wx.EVT_BUTTON, self.submit_button )
        self.max_value.Bind( wx.EVT_TEXT, self.max_val_input )
        self.min_value.Bind( wx.EVT_TEXT, self.min_val_input )

    def __del__( self ):
        pass

    # Virtual event handlers, override them in your derived class
    def search_input( self):
        search_text = self.Search.GetValue()
        return search_text

    def func_choice(self):
        selected_function = self.Function.GetString(self.Function.GetSelection())
        if selected_function == 'Range Filter':
            res_range_filter = range_filter(self.search_input(), self.max_val_input(),self.min_val_input(), self.db)
            return self.display_data_range_filter(res_range_filter, self.search_input())


    def high_toggle( self, event,):
        event.Skip()

    def medium_toggle( self, event ):
        event.Skip()

    def low_toggle( self, event ):
        event.Skip()

    def min_val_input( self):
        min_input = self.min_value.GetValue()
        return float(min_input)

    def max_val_input(self):
        max_input = self.max_value.GetValue()
        return float(max_input)

    def submit_button( self, event ):
        self.func_choice()
        self.search_input()
        event.Skip()

    def display_data_range_filter(self, data, search_value):

        self.m_grid2.ClearGrid()
        self.m_grid2.Show(True)
        processed_data = {}  # Use a dictionary to collect the processed data

        for item in data:
            for key in item:  # Access the key from the dictionary
                new_data = key.split(', ')  # Split by comma and space
                food = new_data[0]
                nutrient_val = new_data[1].split(': ')[1]
                processed_data[food] = nutrient_val  # Assign food item as key and nutrient info as value

        if processed_data:
            self.m_grid2.SetColLabelValue(1, search_value)
            self.m_grid2.SetColLabelValue(0, 'Food')
            for row_index, (food, nutrient_val) in enumerate(processed_data.items()):
                self.m_grid2.SetCellValue(row_index, 0, food)  # Set the food item in column 0
                self.m_grid2.SetCellValue(row_index, 1, nutrient_val)  # Set the nutrient value in column 1
            self.m_grid2.Refresh()


