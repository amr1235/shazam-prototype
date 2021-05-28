from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from Task4_GUI.UI import Ui_MainWindow
from lib.dialog import Dialog
from lib.compare import Compare
from lib.mixer import Mix

class mainWindow(Ui_MainWindow) :
    def __init__(self,starterWindow: QtWidgets.QMainWindow) :
        super(mainWindow, self).setupUi(starterWindow)

        # connect listen button
        self.Listen_Button.clicked.connect(self.listen)
        # connect mix button
        self.Mix_Button.clicked.connect(self.mix)
        # slider defult
        self.Mixing_Slider.setValue(50)
        self.Mixing_Slider.mouseReleaseMethod = self.update_mixing_ratio
        self.results = []
        self.mixer = None

    def update_mixing_ratio(self,ev) :
        if(self.mixer == None) : 
            return
        # get slider value
        weight = self.Mixing_Slider.value() / 100
        filename = self.mixer.mix(weight)
        c = Compare(filename)
        self.results = c.get_similarty_indices()
        self.write_results()

    def listen(self) :
        song_path = Dialog().one_file()
        c = Compare(song_path)
        self.results = c.get_similarty_indices()
        self.write_results()
    
    def write_results(self) :
        for i in range(0,10) :
            song_name = QtWidgets.QTableWidgetItem(str(self.results[i][0]))
            sim = QtWidgets.QTableWidgetItem(str(self.results[i][1]))
            #row col
            self.tableWidget.setItem(i, 0, song_name)
            self.tableWidget.setItem(i, 1, sim)

    def mix(self) :
        paths = Dialog().two_files()
        if paths == None : 
            return 
        self.mixer = Mix(paths[0],paths[1])
        # get slider value
        weight = self.Mixing_Slider.value() / 100
        filename = self.mixer.mix(weight)
        c = Compare(filename)
        self.results = c.get_similarty_indices()
        self.write_results()




        




if __name__ == '__main__':
    import sys

app = QtWidgets.QApplication(sys.argv)
Window = QtWidgets.QMainWindow()
ui = mainWindow(Window)
Window.show()
sys.exit(app.exec_())

