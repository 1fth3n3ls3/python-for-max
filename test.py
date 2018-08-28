import MaxPlus

# MaxPlus.Core.GetRootNode()
x = MaxPlus.SelectionManager.Nodes

for each in x:
	# each.position = MaxPlus.Point3(243,222,222)
	test = each.SetName("ddd")
	print test