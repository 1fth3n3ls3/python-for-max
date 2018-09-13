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

def GetHierarchyTrees(nodes):
	list_nodes = list(nodes)
	print list_nodes
	list_names = list(each.GetName() for each in list_nodes)
	print list_names

	i = 0
  	for each in  list_nodes:
  		parent = each.GetParent()
  		parent_name = parent.GetName()
  		if  parent_name in list_names:
  			print parent_name  
  		

		# parent = each.GetParent()
		# parent_name = parent.GetName()
		# print each
		# print parent
		# if parent in list(nodes):
		# 	print parent

MaxPlus.Core.EvalMAXScript("clearlistener()")

selected_nodes = MaxPlus.SelectionManager.Nodes

GetHierarchyTrees(selected_nodes)


a = [(1, 1), (2, 1), (3, 1), (4, 3), (5, 3), (6, 3), (7, 7), (8, 7), (9, 7)] # first number is id, second parent id, if id is eaqual to idparent the object is root.

# pass 1: create nodes dictionary
nodes = {}
for i in a:
    id, parent_id = i
    nodes[id] = { 'id': id }

# pass 2: create trees and parent-child relations
forest = []
for i in a:
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

print forest
			

