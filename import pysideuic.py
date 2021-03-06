import pysideuic
import MaxPlus

import xml.etree.ElementTree as exml
from io import BytesIO
from PySide.QtCore import *
from PySide.QtGui import *
import pysideuic

def LoadUiType(uiFile):
	# LoadUiType only accept ascii encoding chars
	uiFile = str(uiFile)
	parsed = exml.parse(uiFile)
	widget_class = parsed.find('widget').get('class')
	ui_class_name = parsed.find('class').text
	with open(uiFile, 'r') as f:
		o = BytesIO()
		frame = {}
		pysideuic.compileUi(f, o)
		pyc = compile(o.getvalue(), '<string>', 'exec')
		exec pyc in frame
		ui_class = frame['Ui_%s' % ui_class_name]
		print str(ui_class)
		base_class = eval(widget_class)
		print str(base_class)

	return ui_class, base_class

ui_file = "F:/3dsMax2016/3ds Max 2016/scripts/anim_library.ui"
formt, btype = LoadUiType(ui_file)

class AnimLibraryWidget(btype, formt):

	def __init__(self, parent=None):
		btype.__init__(self)
		formt.__init__(self)
		self.setupUi(self)

		MaxPlus.AttachQWidgetToMax(self)

		# tree widget construction
		tree = self.treeView

		self.model = QFileSystemModel()
		self.model.setNameFilters(["*.fbx"])
		self.model.setFilter(QDir.AllEntries  | QDir.NoDot | QDir.NoDotDot | QDir.Hidden)
		# explanation of filters (from Qt 4.2 doc for QDirModel):
        # - QDir.AllEntries = list files, dirs, drives, symlinks.
        # - QDir.AllDirs = include dirs regardless of other filters 
        #   [guess: needed to ignore the name filters for dirs]
        # - QDir.NoDotAndDotDot = don't include '.' and '..' dirs
		tree.setModel(self.model)

		# path setup for the tree
		path = "C:/Users/dalvarez/Documents/3dsMax/export" 
		root_path = "C:/Users/dalvarez/Documents/3dsMax/"
		self.model.setRootPath(root_path)
		idx = self.model.index(path) 
		tree.setRootIndex(idx)

		tree.doubleClicked.connect(self.get_item)

		# TODO: go up in the root 
		# TODO: hide not wanted file up in the root 

		# btn = self.pushButton
		# btn.clicked.connect(self.create_cylinder) # call an item already defined in the ui
		# self.__object = None
		# dial = self.dial
		# dial.sliderMoved.connect(self.change_height)
	
	def get_item(self, index):
		index = self.treeView.currentIndex()
		file_path = self.model.filePath(index)
		print file_path

	# TODO: cargar animacion y aplicar a lo seleccionado la información requerida.

	# def create_cylinder(self):
	#     obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
	#     obj.ParameterBlock.Radius.Value = 10.0
	#     obj.ParameterBlock.Height.Value = 30.0
	#     node = MaxPlus.Factory.CreateNode(obj)
	#     time = MaxPlus.Core.GetCurrentTime()
	#     MaxPlus.ViewportManager.RedrawViews(time)
	#     self.__object = obj

	# def change_height(self):
	# 	self.__object.ParameterBlock.Height.Value = self.dial.value() ** 2
	# 	print self.dial.value()
	# 	time = MaxPlus.Core.GetCurrentTime()
	#     MaxPlus.ViewportManager.RedrawViews(time)



form = AnimLibraryWidget()
form.show()