import MaxPlus
from itertools import islice
from itertools import takewhile
from itertools import dropwhile

MaxPlus.Core.EvalMAXScript("clearlistener()")

def GetHierarchy(node):
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

bip001 = MaxPlus.INode.GetINodeByName("Bip001")
hierarchy_bip1 = GetHierarchy(bip001)


# Modo de recopilar cosas en listados
x =  list(each for each in hierarchy_bip1 if each.GetName().find("Foot") != -1 and each.GetName().find("steps") == -1)

for each in x:
	# print each.GetName()
	pass

# print hierarchy_bip1

# print any( each for each in hierarchy_bip1 if each.GetName().find("Foot"))

# print list(islice(hierarchy_bip1, 2))

# print list(takewhile(lambda each: "Foot" in each.GetName().find("Foot"), hierarchy_bip1))

# print list(dropwhile(lambda each: "Foot" in each.GetName(), hierarchy_bip1))

# print "test{}".format("ddd")

def CreateIdList(nodes):
	list_nodes = list(nodes)
	# print list_nodes
	list_names = list(each.GetName() for each in list_nodes)
	# print list_names
	tuple_list = []
	i = 0
	for each in  list_nodes:
		parent = each.GetParent()
		parent_name = parent.GetName()

		if  parent_name in list_names:
			tuple_list.append((i, list_names.index(parent_name)))

		else :
			tuple_list.append((i, i))
		
		i += 1


	return tuple_list


def GetHierarchyTree(ids_list, node_list):
	# pass 1: create nodes dictionary
	nodes = {}
	for i in ids_list:
		id, parent_id = i
		nodes[id] = { 'id': id }

	# pass 2: create trees and parent-child relations
	forest = []
	for i in ids_list:
		id, parent_id = i
		node = nodes[id]

		# either make the node a new tree or link it to its parent
		if id == parent_id:
			# start a new tree in the forest
			forest.append(node)
		else:
			# add new_node as child to parent
			parent = nodes[parent_id]
			if not 'children' in parent:
				# ensure parent has a 'children' field
				parent['children'] = []
			children = parent['children']
			children.append(node)

	return forest




MaxPlus.Core.EvalMAXScript("clearlistener()")

selected_nodes = MaxPlus.SelectionManager.Nodes

ids_list =  CreateIdList(selected_nodes)
		

trees =  GetHierarchyTree(ids_list, selected_nodes)


for tree in trees:
	children = False
	# print each['id']
	if 'children' in  tree.keys():
		children = True
		# while children:
		for branch in tree['children']:
			print branch
			if 'children' in  branch.keys():
				branch = branch['children']

				print 'llego ' + str(branch)
			else:
				children = False
				print 'llego1'



