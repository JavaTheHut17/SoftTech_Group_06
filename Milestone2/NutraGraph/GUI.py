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
from all_functions import search_food, nutrition_breakdown, range_filter, high_med_low_filter, high_low_filter
import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    db = 'DataBase/Food_Nutrition_Dataset.csv'

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition,
                            size = wx.Size( 973,733 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.Search = wx.TextCtrl( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.Size(200,-1), 0 )
        bSizer1.Add( self.Search, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        FunctionChoices = [ _(u"Nutrition Breakdown"), _(u"Range Filter"), _(u"High Med Low Filter"),
                            _(u"High Low Filter"), _(u"Search"), wx.EmptyString, wx.EmptyString, wx.EmptyString ]
        self.Function = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, FunctionChoices, 0 )
        self.Function.SetSelection( 0 )
        bSizer1.Add( self.Function, 0, wx.ALL|wx.EXPAND, 5 )

        wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.High = wx.ToggleButton( self, wx.ID_ANY, _(u"High"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.High, 0, wx.ALL, 5 )

        self.m_button13 = wx.ToggleButton( self, wx.ID_ANY, _(u"Medium"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.m_button13, 0, wx.ALL, 5 )

        self.Low = wx.ToggleButton( self, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.Low, 0, wx.ALL, 5 )

        self.max_value = wx.TextCtrl( self, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.max_value, 0, wx.ALL, 5 )

        self.min_value = wx.TextCtrl( self, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.min_value, 0, wx.ALL, 5 )

        self.Submit = wx.Button( self, wx.ID_ANY, _(u"Submit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer3.Add( self.Submit, 0, wx.ALL, 5 )

        self.label = wx.StaticText(self, wx.ID_ANY, "Please enter food item.", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer3.Add( self.label, 0, wx.ALL, 5 )


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

    def search_input( self):
        search_text = self.Search.GetValue()
        return search_text

    def display_search_results(self, data):
        self.m_grid2.ClearGrid()
        self.m_grid2.Show(True)

        nutrients = ['Fat', 'Carbohydrates', 'Protein', 'Sugars', 'Dietary Fiber', 'Caloric Value']
        num_rows = min(20, len(data))
        num_cols = len(nutrients) + 1

        if self.m_grid2.GetNumberRows() > 0:
            self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())
        if self.m_grid2.GetNumberCols() > 0:
            self.m_grid2.DeleteCols(0, self.m_grid2.GetNumberCols())

        self.m_grid2.AppendRows(num_rows)
        self.m_grid2.AppendCols(num_cols)

        self.m_grid2.SetColLabelValue(0, "Food")
        for col_index, nutrient in enumerate(nutrients, start=1):
            self.m_grid2.SetColLabelValue(col_index, nutrient)

        for row_index, food_item in enumerate(data[:num_rows]):
            food_name = food_item['food']
            self.m_grid2.SetCellValue(row_index, 0, food_name)

            for col_index, nutrient in enumerate(nutrients, start=1):
                nutrient_value = str(food_item[nutrient])  # Convert to string for grid display
                self.m_grid2.SetCellValue(row_index, col_index, nutrient_value)

        self.m_grid2.Refresh()

    def display_nutrition_breakdown(self, result):
        self.m_grid2.ClearGrid()
        self.m_grid2.Show(True)

        nutrients = ['Fat', 'Carbohydrates', 'Protein', 'Sugars', 'Dietary Fiber', 'Caloric Value']

        if isinstance(result, dict):
            self.m_grid2.AppendRows(1)
            self.m_grid2.AppendCols(len(nutrients) + 1)

            self.m_grid2.SetColLabelValue(0, "Food")
            for col_index, nutrient in enumerate(nutrients, start=1):
                self.m_grid2.SetColLabelValue(col_index, nutrient)

            food_name = list(result.keys())[0]
            self.m_grid2.SetCellValue(0, 0, food_name)

            for col_index, nutrient in enumerate(nutrients, start=1):
                nutrient_value = str(result[food_name].get(nutrient, 'N/A'))
                self.m_grid2.SetCellValue(0, col_index, nutrient_value)

        self.m_grid2.Refresh()

    def func_choice(self):
        selected_function = self.Function.GetString(self.Function.GetSelection())

        if selected_function == "Search":
            self.label.SetLabel("Please enter a keyword to search for food items.")
            result = search_food(self.search_input(), self.db)
            self.display_search_results(result)

        elif selected_function == 'Nutrition Breakdown':
            self.label.SetLabel("Please enter a food item for nutrition breakdown.")
            result = nutrition_breakdown(self.search_input(), self.db)
            self.display_nutrition_breakdown(result)

        if selected_function == 'Range Filter':
            self.label.SetLabel("Please enter: Min and Max value")
            res_range_filter = range_filter(self.search_input(), self.max_val_input(),self.min_val_input(), self.db)
            return self.display_data_range_filter(res_range_filter, self.search_input())

        if selected_function == "High Med Low Filter":
            res_high_med_low = high_med_low_filter(self.search_input(), self.high_toggle(), self.medium_toggle(),
                                                   self.low_toggle(), self.db)
            self.label.SetLabel("Please toggle: High, Medium, Or Low.")
            return self.display_data_high_med_low(res_high_med_low, self.search_input())
        if selected_function == "High Low Filter":
            res_high_low_filter = high_low_filter(self.search_input(), self.high_toggle(), self.low_toggle(), self.db)
            self.label.SetLabel("Please toggle: High, Or Low.")
            return self.display_high_low_filter(res_high_low_filter, self.search_input())

    def high_toggle(self):
        if self.High.GetValue():
            return True
        else:
            return False

    def medium_toggle(self):
        if self.m_button13.GetValue():
            return True
        else:
            return False

    def low_toggle( self):
        if self.Low.GetValue():
            return True
        else:
            return False

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
        processed_data = {}

        for item in data:
            for key in item:
                new_data = key.split(', ')
                food = new_data[0]
                nutrient_val = new_data[1].split(': ')[1]
                processed_data[food] = nutrient_val
        num_rows = len(processed_data)
        self.m_grid2.AppendRows(num_rows)
        if processed_data:
            self.m_grid2.SetColLabelValue(1, search_value)
            self.m_grid2.SetColLabelValue(0, 'Food')
            for row_index, (food, nutrient_val) in enumerate(processed_data.items()):
                self.m_grid2.SetCellValue(row_index, 0, food)
                self.m_grid2.SetCellValue(row_index, 1, nutrient_val)
            self.m_grid2.Refresh()

    def display_data_high_med_low(self, data, search_value):
        self.m_grid2.ClearGrid()
        self.m_grid2.Show(True)
        processed_data = {}

        for item in data:
            for key in item:
                new_data = key.split(', ')
                food = new_data[0]
                nutrient_val = new_data[1].split(': ')[1]
                processed_data[food] = nutrient_val
        num_rows = len(processed_data)
        self.m_grid2.AppendRows(num_rows)
        if processed_data:
            self.m_grid2.SetColLabelValue(1, search_value)
            self.m_grid2.SetColLabelValue(0, 'Food')
            for row_index, (food, nutrient_val) in enumerate(processed_data.items()):
                self.m_grid2.SetCellValue(row_index, 0, food)
                self.m_grid2.SetCellValue(row_index, 1, nutrient_val)
            self.m_grid2.Refresh()


    def display_high_low_filter(self, data, search_value):
        self.m_grid2.ClearGrid()
        self.m_grid2.Show(True)
        processed_data = {}

        for item in data:
            for key in item:
                new_data = key.split(', ')
                food = new_data[0]
                nutrient_val = new_data[1].split(': ')[1]
                processed_data[food] = nutrient_val

        num_rows = len(processed_data)
        self.m_grid2.AppendRows(num_rows)

        if processed_data:
            self.m_grid2.SetColLabelValue(1, search_value)
            self.m_grid2.SetColLabelValue(0, 'Food')
            for row_index, (food, nutrient_val) in enumerate(processed_data.items()):
                self.m_grid2.SetCellValue(row_index, 0, food)
                self.m_grid2.SetCellValue(row_index, 1, nutrient_val)
        self.m_grid2.Refresh()


