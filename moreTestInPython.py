import MaxPlus

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
	print "Current Animation Range: [%d,%d]" % (start, end)

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

def AnimateTransform(node, tm_list, offset = 0):
	'''Moves the node around to demonstrate animation'''
	# select the node so we will see the keyframes in the timeslider
	ticks_per_frame = 160
	node.Select()
	anim = MaxPlus.Animation
	# Turn on the AutoKey button
	anim.SetAnimateButtonState(True)

	start = offset

	for frame in xrange(start, len(tm_list) + 1):
		anim.SetTime(frame * ticks_per_frame)
		# print frame 
		node.SetWorldTM(tm_list[frame])

	# Turn off the AutoKey button
	anim.SetAnimateButtonState(False)

def GetTransformAnim(node):
	'''Moves the node around to demonstrate animation'''
	# select the node so we will see the keyframes in the timeslider
	ticks_per_frame = 160
	node.Select()
	anim = MaxPlus.Animation

	start, end = GetAnimationRanges()

	tm_info = []

	for frame in xrange(start, end + 1 ):
		anim.SetTime(frame * ticks_per_frame)
		# print frame 
		tm_info.append(node.GetWorldTM()) 

	return tm_info


def getTransforms(node):
	return [node.GetWorldTM() for node in nodes]

def getTransformLocal(node, parent=None):
	if (not parent):
		parent = node.GetParent()
	print str(parent)
	tm = node.GetWorldTM()
	parent_tm = parent.GetWorldTM()


	print tm 
	print parent_tm
	inversed_tm = MaxPlus.Matrix3(*parent_tm)
	inversed_tm.Invert()

	local_tm = tm * inversed_tm

	print parent_tm
	print local_tm

	return local_tm



# getTransforms(MaxPlus.Core.GetRootNode().Children)

selected_nodes = MaxPlus.SelectionManager.Nodes

# tm_list = GetTransformAnim(*selected_nodes)

the_node = MaxPlus.INode.GetINodeByName("Point001")

# AnimateTransform(the_node, tm_list)

# TODO: Get Hierarchy of selected, get hierarchy of  biped
# TODO: Get Matrix with parent

local_transform = getTransformLocal(the_node)

the_node.SetWorldTM(local_transform)



# tm = the_node.GetWorldTM()
# inverse_tm = MaxPlus.Matrix3(*tm)

# print tm
# print inverse_tm
# inverse_tm.Invert()
# print inverse_tm



	