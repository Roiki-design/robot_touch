#!/usr/bin/python3

import sys
import os
import PyQt5.QtWidgets

class Ui(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui',self)  # Load the .ui file

       
        self.load_file.clicked.connect(self.openFile)
        self.save_file.clicked.connect(self.saveFile)
        #self.run_program.clicked.connect()
        #self.stop_program.clicked.connect()

        self.show()  # Show the GUI

    def openFile(self):
         filename = qt.QFileDialog.getOpenFileName(self, "Open File")

         #file = open(filename, 'r')
         #with file as f:
             #line=f.read().splitlines()
             #self.programView.addItem(line)


    
    def saveFile(self):
        name = qt.QFileDialog.getSaveFileName()
        file = open(name,'w')
        #text = 
        file.write(text)
        file.close()


def main():

    app = qt.QApplication(sys.argv)

    window = Ui()
    app.exec_()

if __name__ == '__main__':
   main()
