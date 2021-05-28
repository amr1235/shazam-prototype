from PyQt5 import QtCore, QtGui, QtWidgets

class Dialog(QtWidgets.QFileDialog) :
    def __init__(self) :
        super(Dialog,self).__init__()
        self.setFileMode(QtWidgets.QFileDialog.AnyFile)

    def one_file(self) :
        directory = self.getOpenFileName(None,'select file',__file__,'sound files (*.mp3)')
        path = directory[0]
        return path

    def two_files(self) : 
        directory = self.getOpenFileNames(None,'select file',__file__,'sound files (*.mp3)')
        paths = directory[0]
        if len(paths) != 2  :
            self.warnDialog("please choose two files")
            return
        return paths

    def warnDialog(self,message):
        window = QtWidgets.QMessageBox()
        window.setWindowTitle("error")
        window.setText(message)
        window.exec_()

