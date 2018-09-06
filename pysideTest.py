import MaxPlus
from PySide import QtGui, QtCore

class _GCProtector(object):
    # protege la ventana de ser cerrada por el garbage collector
    widgets = []

app = QtGui.QApplication.instance()
if not app:
	app = QtGui.QApplication([])

def main():		
	MaxPlus.FileManager.Reset(True)
	w = QtGui.QWidget()
	w.resize(250, 100)
	w.setWindowTitle('Window')
	
	_GCProtector.widgets.append(w)
	w.show()

	main_layout = QtGui.QVBoxLayout()
	label = QtGui.QLabel("Click button to create a cylinder in the scene")
	main_layout.addWidget(label)

	cylinder_btn = QtGui.QPushButton("Cylinder")
	main_layout.addWidget(cylinder_btn)
	w.setLayout(main_layout)

if __name__ == '__main__':
	main()