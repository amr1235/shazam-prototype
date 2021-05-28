from PyQt5 import QtCore, QtGui, QtWidgets

class Slider(QtWidgets.QSlider) :

    def __init__(self,parent) :
        super(Slider,self).__init__()
        self.setParent(parent)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.setMaximum(100)
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.setTickInterval(10)
        self.setObjectName("Mixing_Slider")
        self.mouseReleaseMethod = None
        
    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.mouseReleaseMethod(ev)
        