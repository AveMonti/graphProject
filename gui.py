import sys
import json
from PyQt4 import QtGui
from getRoouts import getRoots


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Display value', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

        self.textbox = QtGui.QLineEdit(self)
        self.textbox.insert("{0: [1,2,3], 1: [], 2: [1], 3: [4,5],4: [3,5], 5: [3,4,7], 6: [8], 7: [],8: [9], 9: []}")
        layout.addWidget(self.textbox)
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)

    def handleButton(self):

        json_data = self.textbox.text()
        print (json.loads(json_data))
        getRoots(d)

        print (d)
        self.textbox.setText("")

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
