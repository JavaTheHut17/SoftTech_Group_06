import wx
import wx.grid
import matplotlib
matplotlib.use('WXAgg')  # Allows Matplotlib to render plots within wxPython
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.pyplot as plt
from GUI import MyFrame1 as MyFrame

# Subclassing MyFrame to add Matplotlib support
class MyMainFrame(MyFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_grid2.Show(False)

        self.Layout()
        self.Show(True)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyMainFrame()
    app.MainLoop()
