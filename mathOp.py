import math
import MaxPlus

# def module(vector):
# 	return math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)

# print module([1, 1, 1])	

# x = 1.0
# y = 1.0
# z = 1.0


# c = MaxPlus.Point3()
# c.Set(x, y, z)
# print c
MaxPlus.Core.EvalMAXScript("clearlistener()")

o = MaxPlus.INode.GetINodeByName("Sphere001")

test = MaxPlus.Core.EvalMAXScript("print %s" % o[1])

# x = test.Get()
# print dir(x)
# print x.GetNumRefs()
# print x.GetName()

# print x

