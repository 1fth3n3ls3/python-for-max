import MaxPlus

#Get Selected nodes

selected_nodes = MaxPlus.SelectionManager.Nodes

#move nodes


#delete nodes

for each in selected_nodes:
	# each.Move(MaxPlus.Point3(25,222,22))

	each.Position(MaxPlus.Point3(0,0,0))