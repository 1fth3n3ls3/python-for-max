from pymxs import runtime as rt

import MaxPlus

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

rt.getRefCoordSys()


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