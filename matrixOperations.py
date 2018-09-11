import MaxPlus

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

MaxPlus.Core.EvalMAXScript("clearListener()")


bip001 = MaxPlus.INode.GetINodeByName("Teapot001")


bip002 = MaxPlus.INode.GetINodeByName("Teapot002")

bip003 = MaxPlus.INode.GetINodeByName("Point001")

bip1_tm = bip001.GetWorldTM()

print dir(bip1_tm)

# bip1_tm.Invert()

bip2_tm = bip002.GetWorldTM()

pos = bip2_tm.GetTranslation()

# tm = MaxPlus.Matrix3(*bip1_tm)
# tm.SetTranslation(pos)  


bip002.SetWorldTM(PreservePosition(pos, bip1_tm))

# bip2_local_tm = getTransformLocal(bip002)
# bip2_local_tm = bip002.GetLocalTM()

print getTransformLocal(bip002)
print bip002.GetLocalTM()


# bip2_tm.Invert()

identity = MaxPlus.Matrix3.GetIdentity()

print dir(MaxPlus.Matrix3.GetIdentity())

# bip002.SetWorldTM(bip2_tm * inverseMatrix(bip2_tm)) # a matrix multiplication by his invert the result is identity matrix

print identity
print inverseMatrix(identity)

# print bip1_tm
# print inverseMatrix(bip1_tm)

# print  (inverseMatrix(bip1_tm) * bip1_tm)

bip003.SetWorldTM(bip2_local_tm * bip1_tm) #local transformation of an object by his parent world transform you get the world transform

# bip003.SetWorldTM(bip2_tm)

print MaxPlus.Core.GetMaxVersion()
