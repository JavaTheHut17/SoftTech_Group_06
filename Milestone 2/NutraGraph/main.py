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

        # # Create a Matplotlib figure and add it to a wxPanel
        # self.figure = plt.Figure()
        # self.axes = self.figure.add_subplot(111)
        # self.canvas = FigureCanvas(self, -1, self.figure)
        #
        # # Sample plot
        # self.axes.plot([0, 1, 2], [1, 4, 9])

        # Layout update
        self.Layout()
        self.Show(True)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyMainFrame()
    app.MainLoop()
