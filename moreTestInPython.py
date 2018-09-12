import MaxPlus
import copy # module to make copys and deep copies
import math

# triObjectID = MaxPlus.Class_ID(0x0009, 0)

# def getMeshFromNode(node, time):
#        obj = node.EvalWorldState(time).Getobj()
#        if (obj.CanConvertToType(triObjectID)):
#               return MaxPlus.TriObject._CastFrom(obj.ConvertToType(triObjectID, time)).GetMesh()
#        else:
#               return None

# def getNodeVerts(node, time):
#        tm = node.GetObjTMAfterWSM(time)
#        mesh = getMeshFromNode(node, time)
#        return [tm.PointTransform(mesh.GetVertex(v)) for v in xrange(0, mesh.GetNumVertices())]

# getNodeVerts(MaxPlus.SelectionManager.Nodes.next()  , MaxPlus.Animation.GetTime())

def PrintInterval(interval):
	'''This function prints an Interval instance nicely with identifiable values. i.e. 'Interval [0,100]'
	It prints the values in terms of frames, instead of ticks.
	Each frame contains 160 ticks. In the SDK, when Intervals are passed around, they
	are not passed as the number of frames, but instead the frames multiplied by ticks (i.e. 160)'''
	start = interval.Start() / 160
	end = interval.End() / 160
	# print "Current Animation Range: [%d,%d]" % (start, end)

def SetAnimationRanges():
	'''Changes the animation range from the default of 100 frames to 200 frames'''
	anim = MaxPlus.Animation
	PrintInterval(anim.GetAnimRange())
	# Intervals come in units of ticks. Each frame is 160 ticks.
	newFrames = 200 * 160
	newRange = MaxPlus.Interval(0, newFrames)
	anim.SetRange(newRange)
	# The animation slider now shows 200 frames
	PrintInterval(anim.GetAnimRange())

def GetAnimationRanges():
	'''Changes the animation range from the default of 100 frames to 200 frames'''
	anim = MaxPlus.Animation
	anim_range = anim.GetAnimRange()
	ticks_per_frame = 160
	PrintInterval(anim_range)
	# # Intervals come in units of ticks. Each frame is 160 ticks.
	# newFrames = 200 * 160
	# newRange = MaxPlus.Interval(0, newFrames)
	# anim.SetRange(newRange)
	# # The animation slider now shows 200 frames
	# PrintInterval(anim.GetAnimRange())
	return anim_range.Start() / ticks_per_frame, anim_range.End() / ticks_per_frame

# def AnimateTransform(node, tm_list, offset = 0):
# 	'''Moves the node around to demonstrate animation'''
# 	# select the node so we will see the keyframes in the timeslider
# 	ticks_per_frame = 160
# 	# node.Select()
# 	anim = MaxPlus.Animation
# 	# Turn on the AutoKey button
# 	anim.SetAnimateButtonState(True)

	

# 	for frame in xrange(offset, len(tm_list) + offset):
# 		anim.SetTime((frame * ticks_per_frame) + offset, False) 
# 		# print frame 
# 		node.SetWorldTM(tm_list[frame - offset])

# 	# Turn off the AutoKey button
# 	anim.SetAnimateButtonState(False)

# def GetTransformAnim(node):
# 	'''Moves the node around to demonstrate animation'''
# 	# select the node so we will see the keyframes in the timeslider
# 	ticks_per_frame = 160
# 	# node.Select()
# 	anim = MaxPlus.Animation

# 	start, end = GetAnimationRanges()

# 	tm_info = []

# 	for frame in xrange(start, end):
# 		anim.SetTime(frame * ticks_per_frame, False)
# 		# print frame 
# 		tm_info.append(node.GetWorldTM()) 

# 	return tm_info

def AnimateTransformDecompose(nodes, tm_list, offset = 0):
	'''Moves the node around to demonstrate animation'''
	# select the node so we will see the keyframes in the timeslider
	ticks_per_frame = 160
	anim = MaxPlus.Animation
	# Turn on the AutoKey button
	anim.SetAnimateButtonState(True)

	for frame in xrange(offset, len(tm_list) + offset):
		# print frame
		anim.SetTime((frame * ticks_per_frame) + offset, False) 
 		for i in xrange(0, len(nodes)):
 			# TODO Chequear si esto realmente funciona
 			t = (tm_list[frame - offset][i]).GetTranslation()
 			r = (tm_list[frame - offset][i]).GetRotation()


			nodes[i].SetWorldPosition(t)
			nodes[i].SetWorldRotation(r)



	# Turn off the AutoKey button
	anim.SetAnimateButtonState(False)

def AnimateTransform(nodes, tm_list, offset = 0):
	'''Moves the node around to demonstrate animation'''
	# select the node so we will see the keyframes in the timeslider
	ticks_per_frame = 160
	anim = MaxPlus.Animation
	# Turn on the AutoKey button
	anim.SetAnimateButtonState(True)
	for frame in xrange(offset, len(tm_list) + offset):
		# print frame
		# anim.SetTime((frame * ticks_per_frame) + offset, False) 
		t = ((frame + offset)* ticks_per_frame) 
 		for i in xrange(0, len(nodes)):
 			# print i
			nodes[i].SetWorldTM(tm_list[frame - offset][i], int(t))


	# Turn off the AutoKey button
	anim.SetAnimateButtonState(False)

def AnimateTransformCompensation(nodes, tm_list, offset=0, stride=1.0): # la tm_list ahora mismo se compone de una lista que representa cada frame, que a su vez contiene la informacion de todos los nodos
	'''Moves the node around to demonstrate animation

	'''
	ticks_per_frame = 160
	anim = MaxPlus.Animation
	initial_tm = tm_list[0][0] #posicion inicial para el padre de toda la jerarquia del biped
	invert_initial_tm = inverseMatrix(initial_tm)
	initial_pos = tm_list[0][0].GetTranslation()

	original_pos = nodes[0].GetWorldPosition(offset * ticks_per_frame ) # toma la posicion original en el primer frame 


	# Turn on the AutoKey button
	anim.SetAnimateButtonState(True)
	for frame in xrange(offset, len(tm_list) + offset):
		t = ((frame)* ticks_per_frame) 
 		for i in xrange(0, len(nodes)):
 			if i > 0:
 				name = (nodes[i].GetName())
				p = nodes[i].GetWorldPosition(t)
				tm_from_file = tm_list[frame - offset][i]
				new_tm = PreservePosition(p, tm_from_file)
				nodes[i].SetWorldTM(new_tm, t)
				
			else:
				# new_tm = applyOffset(-original_pos, applyOffset(initial_pos, tm_list[frame - offset][i]))
				new_tm = tm_list[frame - offset][i]


				# extraigo la translacion para compensarla por las dimensiones del personaje y volver a reintroducirla
				p = new_tm.GetTranslation() 
				# p.X = p.X * stride
				# p.Y = p.Y * stride
				# p.Z = p.Z * stride

				new_tm.SetTranslation(p)

				nodes[i].SetWorldTM(new_tm, t)

	# Turn off the AutoKey button
	anim.SetAnimateButtonState(False)	


def GetTransformAnim(nodes, start=None, end=None):
	'''Moves the node around to demonstrate animation'''
	# select the node so we will see the keyframes in the timeslider
	ticks_per_frame = 160
	# node.Select()
	anim = MaxPlus.Animation

	if start == None or end == None:
		start, end = GetAnimationRanges()

	range_list = []

	for frame in xrange(start, end): # para cada frame
		# anim.SetTime(frame * ticks_per_frame, False)
		t = frame * ticks_per_frame
		node_list = []
		# print frame
		for each in nodes: # para cada uno de los nodos
			node_list.append(each.GetWorldTM(t)) 
		range_list.append(node_list) 


	return range_list	


def getTransformLocal(node, ref=None):
	tm = node.GetWorldTM()
	if not ref:
		parent = node.GetParent()
		if parent:
			parent_tm = parent.GetWorldTM()
			inversed_tm = inverseMatrix(parent_tm)# MaxPlus.Matrix3(*parent_tm)
			local_tm = tm * inversed_tm
			return local_tm			
		else:
			return tm
	else:
		parent_tm = ref.GetWorldTM()
		inversed_tm = inverseMatrix(parent_tm)# MaxPlus.Matrix3(*parent_tm)
		local_tm = tm * inversed_tm
		return local_tm


def inverseMatrix(matrix):
	# return the inverse matrix
	tm = MaxPlus.Matrix3(*matrix)
	tm.Invert()
	return tm


def PreservePosition(pos, matrix):
	tm = MaxPlus.Matrix3(*matrix)
	tm.SetTranslation(pos)
	return tm  

def applyOffset(new_pos, matrix):
	tm = MaxPlus.Matrix3(*matrix)
	pos = tm.GetTranslation()
	tm.SetTranslation(pos-new_pos)
	return tm 	

def getHierarchy(node):
	hierarchy = []
	hierarchy.append(node)
	# print dir(node)
	childs = list(node.Children)
	while len(childs) > 0:
		for each in childs:
			hierarchy.append(each)
			childs.remove(each)
			childs.extend(each.Children)
	return hierarchy


def module(vector):
	return math.sqrt(vector.GetX() ** 2 + vector.GetY() ** 2 + vector.GetZ() ** 2)

def GetDistance(point_a, point_b):	
	x = point_b.GetX() - point_a.GetX()
	y = point_b.GetY() - point_a.GetY()
	z = point_b.GetZ() - point_a.GetZ()

	c = MaxPlus.Point3()
	c.Set(x, y, z)

	return module(c)


def GetLegDistance(hierarchy):
	foot_node = None
	calf_node = None
	thigh_node = None
	for each in hierarchy:
		name = each.GetName()
		if name.find("L Foot") != -1:
			foot_node = each
			print "llego1"
		if name.find("L Calf") != -1:
			calf_node = each
			print "llego2"
		if name.find("L Thigh") != -1:
			thigh_node = each
			print "llego3"

	leg_distance = GetDistance(thigh_node.GetWorldPosition(), calf_node.GetWorldPosition()) + GetDistance(foot_node.GetWorldPosition(), calf_node.GetWorldPosition())

	return leg_distance

def StrideProportion(long_leg2, long_leg1):
	proportion = long_leg2 / long_leg1
	return proportion	

MaxPlus.Core.EvalMAXScript("clearListener()")

# getTransforms(MaxPlus.Core.GetRootNode().Children)

# selected_nodes = MaxPlus.SelectionManager.Nodes

# tm_list = GetTransformAnim(*selected_nodes)

# the_node = MaxPlus.INode.GetINodeByName("Point001")

# AnimateTransform(the_node, tm_list)

# TODO: get hierarchy of  biped without nubs
# TODO: keep initial pose of target biped
# TODO: work idea about different namespace for mapping
# TODO: biped class


# local_transform = getTransformLocal(the_node)

# the_node.SetWorldTM(local_transform)





##################
# get hierarchy
##################

# TODO check undos 

###################################
# test copy animation with offset
###################################

# MaxPlus.Core.EvalMAXScript("disableSceneRedraw()")
# MaxPlus.Core.EvalMAXScript("timeSlider.setVisible false")
# MaxPlus.Core.EvalMAXScript("trackbar.visible = false")

# bip001 = MaxPlus.INode.GetINodeByName("Bip001")

# hierarchy_bip1 = getHierarchy(bip001)

# bip002 = MaxPlus.INode.GetINodeByName("Bip002")

# hierarchy_bip2 = getHierarchy(bip002)

# the_tms = []
# for each in hierarchy_bip1:
# 	the_tm = GetTransformAnim(each) # esto da de resultado toda la animacion de ese nodo en el rango
# 	the_tms.append(the_tm) # lo anyado a una lista donde cada indice sera el listado de matrices de transformacion



# for i in xrange(0, len(hierarchy_bip2)): # para cada nodo de la jerarquia de destino
# 	AnimateTransform(hierarchy_bip2[i], the_tms[i], offset=5)


# TODO transform the matrixes with the matrix or offset of target parent.

# MaxPlus.Core.EvalMAXScript("timeSlider.setVisible true")
# MaxPlus.Core.EvalMAXScript("trackbar.visible = true")
# MaxPlus.Core.EvalMAXScript("enableSceneRedraw()")
MaxPlus.Core.EvalMAXScript("max create mode")

# MaxPlus.Core.EvalMAXScript("disableSceneRedraw()")
# MaxPlus.Core.EvalMAXScript("timeSlider.setVisible false")
# MaxPlus.Core.EvalMAXScript("trackbar.visible = false")


bip001 = MaxPlus.INode.GetINodeByName("Bip001")
hierarchy_bip1 = getHierarchy(bip001)

bip002 = MaxPlus.INode.GetINodeByName("Bip002")
hierarchy_bip2 = getHierarchy(bip002)

# the_tm = GetTransformAnim(hierarchy_bip1, start=1137, end=1497)
the_tm = GetTransformAnim(hierarchy_bip1)



ld1 = GetLegDistance(hierarchy_bip1)
ld2 = GetLegDistance(hierarchy_bip2)

sp = StrideProportion(ld2, ld1)

print sp



# newFrames = 125 * 160
# newRange = MaxPlus.Interval(0, newFrames)
# MaxPlus.Animation.SetRange(newRange)

bip1_tm = bip001.GetWorldTM()

bip1_tm.Invert()

bip2_tm = bip002.GetWorldTM()

bip2_tm.Invert()

AnimateTransformCompensation(hierarchy_bip2, the_tm, offset=0, stride=sp)
# AnimateTransformCompensation(hierarchy_bip2, the_tm, offset=0)

# AnimateTransform(hierarchy_bip2, the_tm, offset=0)


# MaxPlus.Core.EvalMAXScript("timeSlider.setVisible true")
# MaxPlus.Core.EvalMAXScript("trackbar.visible = true")
# MaxPlus.Core.EvalMAXScript("enableSceneRedraw()")

# TODO: ver si se puede ser consistente descomponiendo el pegado en posicion y rotacion
# FIX: que pasa con los dedos
# TODO: pillar valor del maxscript ejecutado
# TODO: contemplar la posibilidad de que el bip este linkado a un master
# TODO: mirror


