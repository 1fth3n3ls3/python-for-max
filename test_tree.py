import unittest
import matrixOperations

class TestCalc(unittest.TestCase): # inherits from this  class

	
	def test_getTransformLocal(self): # this naming convention is requiered
		obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
		obj.ParameterBlock.Radius.Value = 10.0
		obj.ParameterBlock.Height.Value = 30.0
		node = MaxPlus.Factory.CreateNode(obj)
		result = matrixOperation.getTransformLocal(node)
		self.assertEqual(result, MaxPlus.Matrix3(MaxPlus.Point3(1, 0, 0), 
												MaxPlus.Point3(0, 1, 0), 
												MaxPlus.Point3(0, 0, 1), 
												MaxPlus.Point3(1, 0, 0)))

if __name__ == '__main__':
	unittest.main()