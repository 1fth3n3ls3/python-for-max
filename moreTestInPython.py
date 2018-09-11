import MaxPlus
import copy # module to make copys and deep copies

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

def AnimateTransformCompensation(nodes, tm_list, offset = 0):
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
 			if i > 0:
 				name = (nodes[i].GetName())

 				# if name.find("Hand") == -1:
				p = nodes[i].GetWorldPosition(t)

				tm_from_file = tm_list[frame - offset][i]

				new_tm = PreservePosition(p, tm_from_file)

				nodes[i].SetWorldTM(new_tm, t)

			else:
				nodes[i].SetWorldTM(tm_list[frame - offset][i], int(t))

	# Turn off the AutoKey button
	anim.SetAnimateButtonState(False)	


def GetTransformAnim(nodes):
	'''Moves the node around to demonstrate animation'''
	# select the node so we will see the keyframes in the timeslider
	ticks_per_frame = 160
	# node.Select()
	anim = MaxPlus.Animation

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

MaxPlus.Core.EvalMAXScript("clearListener()")

# getTransforms(MaxPlus.Core.GetRootNode().Children)

# selected_nodes = MaxPlus.SelectionManager.Nodes

# tm_list = GetTransformAnim(*selected_nodes)

# the_node = MaxPlus.INode.GetINodeByName("Point001")

# AnimateTransform(the_node, tm_list)

# TODO: get hierarchy of  biped without nubs


# local_transform = getTransformLocal(the_node)

# the_node.SetWorldTM(local_transform)


##################
# get hierarchy
##################

# hierarchy_nodes = getHierarchy(*selected_nodes)
# print len(hierarchy_nodes)

# for each in hierarchy_nodes:
# 	print each.GetName()



# tm = the_node.GetWorldTM()
# inverse_tm = MaxPlus.Matrix3(*tm)

# print tm
# print inverse_tm
# inverse_tm.Invert()
# print inverse_tm

# the_node2 = MaxPlus.INode.GetINodeByName("Bip001")
# world_tm = the_node2.GetWorldTM()
# local_tm = getTransformLocal(the_node2)

# world_translation = world_tm.GetTranslation()
# world_rotation = world_tm.GetRotation()

# translation = local_tm.GetTranslation()
# quat = local_tm.GetRotation()

# print local_tm
# print quat

# the_node3 = MaxPlus.INode.GetINodeByName("Bip002 R Forearm")


# the_node3.SetLocalRotation(quat)
# the_node3.SetLocalPosition(translation)
# the_node3.SetLocalTM(local_tm)

# the_node3.SetWorldTM(world_tm)


# TODO check undos 

# MaxPlus.Core.EvalMAXScript("biped.getTransform $'%s' #pos" % the_node3.GetName())
# MaxPlus.Core.EvalMAXScript("biped.setTransform $'%s' #pos " % the_node3.GetName())


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

the_tm = GetTransformAnim(hierarchy_bip1)


newFrames = 125 * 160
newRange = MaxPlus.Interval(0, newFrames)
MaxPlus.Animation.SetRange(newRange)

bip1_tm = bip001.GetWorldTM()

bip1_tm.Invert()

bip2_tm = bip002.GetWorldTM()

bip2_tm.Invert()

AnimateTransformCompensation(hierarchy_bip2, the_tm, offset=10)
# AnimateTransform(hierarchy_bip2, the_tm, offset=10)


# MaxPlus.Core.EvalMAXScript("timeSlider.setVisible true")
# MaxPlus.Core.EvalMAXScript("trackbar.visible = true")
# MaxPlus.Core.EvalMAXScript("enableSceneRedraw()")

# TODO: ver si se puede ser consistente descomponiendo el pegado en posicion y rotacion





