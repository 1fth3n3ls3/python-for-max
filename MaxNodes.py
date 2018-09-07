import MaxPlus

class MaxNodes():
	"""docstring for MaxNodes"""
	def __init__(self, nodes=MaxPlus.INodeTab()):
		self.__nodes = nodes

	def __str__(self):
		name_list = []
		for each in self.__nodes:
			name_list.append(each.GetName())

		return str(name_list)

	def append_selection(self):	
		"""add the selected nodes to the specified tab"""
		new_nodes = MaxPlus.SelectionManager.GetNodes()
		for each in new_nodes:
			if not (each in self.__nodes):
				self.__nodes.Append(each)

theNode = MaxPlus.INode.GetINodeByName("Sphere001")

theList = MaxPlus.INodeTab()

theList.Append(theNode)

m = MaxNodes(theList)

print m

m.append_selection()

print m

print dir(MaxPlus.INodeTab())