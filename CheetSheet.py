from pymxs import runtime as rt

import MaxPlus, sys

#clear listener

rt.clearlistener()

#get selection

mySelection = rt.selection

for each in mySelection:
	
	print each.name
	
#get first selected

firstItem = rt.selection[0]

print firstItem.name

#create simple object

rt.sphere(radius=50, position=rt.point3(25, 25, 25), segments=8)

#select all objects

rt.select(rt.objects)

# with MaxPlus

MaxPlus.Core.GetRootNode().Children

#clear selection

rt.clearselection()


rt.select(firstItem)

print rt.firstItem.name


rt.selection[0].name = 'PorTuCulpa'

#layer.nodes &thenodes

rt.layer.nodes(pymxs.mxsreference(theNodes))

#autosave preferences

autosave = rt.autosave
print "Autosave enabled? {}".format(autosave.enable)
print "Autosave filename: {}".format(autosave.filename)

#coordsys setting

rt.toolMode.coordsys(pymxs.runtime.Name("world"))

#get coordsys value

x = rt.getRefCoordSys()

print x


#execute maxscript code

MaxPlus.Core.EvalMAXScript("coordsys parent $'%s'.pos = Point3 0 0 0" % node_name)


#nesting sublayer

parent = rt.LayerManager.NewLayerFromName("C")
child = rt.LayerManager.NewLayerFromName("D")
child.setParent(parent)


#get key info


bone = MaxPlus.INode.GetINodeByName("Bone001")
ctrl = bone.GetTMController().GetPositionController()
print ctrl.GetNumKeys()


#set attributtes in nested attr

teapot = rt.teapot()
object = teapot
attribute = "controller.position.x" #it works with 'controller.pos.x' as well
attribute_parts = attribute.split(".")
#~ for a in attribute_parts[:-1]:
	#~ object = getattr(object, a)
	
#~ print "posX: {0}".format(getattr(object, attribute_parts[-1]))
# prints: posX: 0.0
setattr(object, '.'.join(attribute_parts[1:]), 20)
#~ print "posX: {0}".format(getattr(object, attribute_parts[-1]))
# prints: posX: 20.0


# add a shortcut to python script
"""
See the MaxPlus.ActionFactory method. The file demoActionFactory.py shows how to create ActionItems 
(same as what macroscripts do) in python, it creates a 'Python demo' entry in 'Do something' 
category which you can then bind a shortcut to in the customize UI dialog. There's also demoMenu.py 
that shows how to add the ActionItem to a menu.

"""

#MaxPlus

#Get Selected nodes

selected_nodes = MaxPlus.SelectionManager.Nodes

#delete nodes

for each in selected_nodes:
	each.Delete()


#move nodes


for each in selected_nodes:
	# each.Move(MaxPlus.Point3(25,222,22))
	each.Position(MaxPlus.Point3(0,0,0))

#add modifier

for each in selected_nodes:
	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
	MaxPlus.ModifierPanel.AddToSelection(mod)


# Ejemplo de seleccion de tabnodes propios

selected_nodes = (MaxPlus.SelectionManager.GetNodes()) # creo el tabnode



myList = MaxPlus.INodeTab()

for i in range( 0, len(selected_nodes)):
	myList.Append(selected_nodes[1])

	# print str(selected_nodes[i].GetName())
MaxPlus.SelectionManager.ClearNodeSelection()
MaxPlus.SelectionManager.SelectNodes(myList)


# Example accesing param blocks in a modifier

for each in selected_nodes:
	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
	MaxPlus.ModifierPanel.AddToSelection(mod)
	i = 0
	for p in mod.ParameterBlock:

		type_name = MaxPlus.FPTypeGetName(p.Type)
		try:
			print '  parameter', i, p.Name, p.Type, type_name, p.Value
			i += 1
		except:
			etype, evalue = sys.exc_info()[:2]
			print 'error '. etype, evalue

# Get access to a modifier

selected_nodes = (MaxPlus.SelectionManager.GetNodes())

for each in selected_nodes:
	n = each.GetNumModifiers()
	mod = each.GetModifier(n - 1) #accedo al último de la lista
	print str(mod)

#How to pass a custom selection to max

selected_nodes = MaxPlus.SelectionManager.GetNodes()

n = len(selected_nodes)

#create tab for selection and then append chossen reference nodes to it
newSelection = MaxPlus.INodeTab()

for each in range(0, n):
	print selected_nodes[each].GetName()
	if each == 1:
		newSelection.Append(selected_nodes[each])

MaxPlus.SelectionManager.ClearNodeSelection()
MaxPlus.SelectionManager.SelectNodes(newSelection)

# Create maxscript variables
  MaxPlus.Core.EvalMAXScript("o_layer = undefined")
  MaxPlus.Core.EvalMAXScript("l_oNodes = #()")
  l_oNodes = []

  for i in range(len(rt.LayerManager)):
    o_layer = rt.LayerManager.getLayer(i)
    if o_layer.name.lower().find(sLayerName) > -1:
      rt.o_layer = rt.LayerManager.getLayer(i)
      # Get maxscript nodes 
      MaxPlus.Core.EvalMAXScript("o_layer.nodes &l_oNodes")
      # Generate python list from nodes
      for n in rt.l_oNodes:
        l_oNodes.append(n)

# Importar librerias de python externas

import sys
sys.path.append("F:/FBX/2016.1/lib/Python27_x64/")

import FbxCommon


# Get Node by Name

the_node = MaxPlus.INode.GetINodeByName("Point001")


# Invert matrix method for Matrix3 class

the_node = MaxPlus.INode.GetINodeByName("Point001")

tm = the_node.GetWorldTM()
inverse_tm = MaxPlus.Matrix3(*tm)

print tm
print inverse_tm
inverse_tm.Invert()
print inverse_tm

# Change max modes hack though maxscript

MaxPlus.Core.EvalMAXScript("max create mode")


# Disable / Enable some redraws and viewports stuff

MaxPlus.Core.EvalMAXScript("timeSlider.setVisible true")
MaxPlus.Core.EvalMAXScript("trackbar.visible = true")
MaxPlus.Core.EvalMAXScript("enableSceneRedraw()")

MaxPlus.Core.EvalMAXScript("disableSceneRedraw()")
MaxPlus.Core.EvalMAXScript("timeSlider.setVisible false")
MaxPlus.Core.EvalMAXScript("trackbar.visible = false")

# Get access to data returned by maxcript, applied to rootscene

test = MaxPlus.Core.EvalMAXScript("rootscene.expArtistProps.objsNames")
x = test.Get()
print x

#########################
# Back and for with pymxs
#########################


import pymxs
import MaxPlus
MaxPlus.Core.EvalMAXScript("clearlistener()")
#Create a global using MaxScript
x = MaxPlus.Core.EvalMAXScript('test1 = sphere()')

test1 = x.Get()
print test1
#Print and modify using Python
rt = pymxs.runtime
print rt.test
rt.test1.radius = 100

print test1.GetName()

#Print using MaxScript
MaxPlus.Core.EvalMAXScript(" print test1.name")

# Create Bones  with MaxPlus
def createBone (start, end, width = 2.0, height = 2.0):
	if not (type(start) == type(end) == mp.Point3):
		return None
	dirVec = end - start
	if not (dirVec.Normalize()%mp.Point3(0,0,1) == 1.0) or (dirVec.Normalize()%mp.Point3(0,0,1) == -1.0):
		upVec = mp.Point3(0,0,1)
	else:
		upVec = mp.Point3(0,1,0)
	
	frontVec = dirVec.Normalize()
	sideVec = (upVec^frontVec).Normalize()
	upVec = (frontVec^sideVec).Normalize()
	tm = mp.Matrix3(frontVec , sideVec , upVec , start)
	obj = mp.Factory.CreateGeomObject(MaxPlus.ClassIds.BoneGeometry)
	obj.ParameterBlock.Length.Value = dirVec.GetLength()
       	obj.ParameterBlock.Width.Value = width
	obj.ParameterBlock.Height.Value = height
	node = mp.Factory.CreateNode(obj)
	node.SetWorldTM(tm)
	return node
def createBoneChain (posList, width = 4.0, height = 4.0, index = 0, parent=mp.Core.GetRootNode()):
	'''
	posList is a list of Point3 positions of the bones you want to create,
	!!! INCLUDING !!! the end position of the end bone.
	'''
	bn = createBone(posList[index], posList[index+1], width, height)
	bn.SetParent(parent)
	if index < len(posList) - 2:
		createBoneChain(posList, width, height, index + 1, bn)


# How to get node transform monitor target from a maxscript

x = MaxPlus.Core.EvalMAXScript("$'%s'.nodeRefs[1].node" % the_node.GetName()) 
# new sintaxis
name =  the_node.GetName()
x = MaxPlus.Core.EvalMAXScript("$'{}'.nodeRefs[1].node".format(name)) 


y = x.Get()

print y.GetName()		