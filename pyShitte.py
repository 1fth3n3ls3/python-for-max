import MaxPlus
from PySide import QtGui, QtCore


# MaxPlus.Core.MaxEval("clearlisterner()")

# app = QtGui.QApplication.instance()
# if not app:
#     app = QtGui.QApplication([])

# w = QtGui.QWidget(MaxPlus.GetQMaxWindow())
# _GCProtector.widgets.append(w)
# w.resize(250, 100)
# w.setWindowTitle('PySide Qt Window')
# def main():
# 	window = QtGui.QWidget(MaxPlus.GetQMaxWindow())
# 	window.setGeometry(15, 35, 500, 300)
# 	window.setWindowTitle("PyQT Tuts!")

# 	window.show()\

# if __name__ == '__main__':
#     main()

class _GCProtector(object):
    # protege la ventana de ser cerrada por el garbage collector
    widgets = []

class Window(QtGui.QWidget):
    """docstring for Window"""

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(15, 35, 500, 300)
        self.setWindowTitle("My Window")

        # self.setWindowIcon(QtGui.QIcon(''))

        # extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        # extractAction.setShortcut("Ctrl+Q")
        # extractAction.setStatusTip('Leave The App')

        # # self.statusBar()

        # mainMenu = self.menuBar()
        # fileMenu = mainMenu.addMenu('&File')
        # fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("cylinder", self)
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close_application)
        # btn.resize(100,100)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 0)

        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)
        # depending on what you want the default to be.
        # checkBox.toggle()

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton('Download', self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)


        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.move(50, 250)
        

        # comboBox.activated[str].connect(self.style_choice)

        self.show()




    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.00001
            self.progress.setValue(self.completed)    

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def make_cylinder(self):
        obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
        obj.ParameterBlock.Radius.Value = 10.0
        obj.ParameterBlock.Height.Value = 30.0
        node = MaxPlus.Factory.CreateNode(obj)
        time = MaxPlus.Core.GetCurrentTime()
        MaxPlus.ViewportManager.RedrawViews(time)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
        # sys.exit()
        else:
            pass


def main():
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])

    window = Window()
    # MaxPlus.AttachQWidgetToMax(window) # 2016
    window.setParent(MaxPlus.GetQMaxWindow()) # by default the QWidget is modeless #2017
    # _GCProtector.widgets.append(window)


if __name__ == '__main__':
    main()