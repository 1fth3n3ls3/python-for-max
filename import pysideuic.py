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
        base_class = eval(widget_class)
    return ui_class, base_class

fname = "F:/3dsMax2016/3ds Max 2016/scripts/test.ui"
formt, btype = LoadUiType(fname)

class TestWidget(btype, formt):
    def __init__(self, parent=None):
        btype.__init__(self)
        formt.__init__(self)
        self.setupUi(self)
        MaxPlus.AttachQWidgetToMax(self)
        btn = self.pushButton
        btn.clicked.connect(self.create_cylinder) # call an item already defined in the ui
        self.__object = None
        dial = self.dial
        dial.sliderMoved.connect(self.change_height)

    def create_cylinder(self):
        obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
        obj.ParameterBlock.Radius.Value = 10.0
        obj.ParameterBlock.Height.Value = 30.0
        node = MaxPlus.Factory.CreateNode(obj)
        time = MaxPlus.Core.GetCurrentTime()
        MaxPlus.ViewportManager.RedrawViews(time)
        self.__object = obj

    def change_height(self):
    	self.__object.ParameterBlock.Height.Value = self.dial.value() ** 2
    	print self.dial.value()
    	time = MaxPlus.Core.GetCurrentTime()
        MaxPlus.ViewportManager.RedrawViews(time)



form = TestWidget()
form.show()