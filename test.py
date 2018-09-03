import MaxPlus, sys




selected_nodes = (MaxPlus.SelectionManager.GetNodes())

for each in selected_nodes:
	n = each.GetNumModifiers()
	mod = each.GetModifier(n - 1) #accedo al último de la lista
	for p in mod.ParameterBlock:
		type_name = MaxPlus.FPTypeGetName(p.Type)
		if p.Name == 'aExpBn':
			print p.Value
			print p.Value.GetItem(2)
			print p.Name
			print type_name
			print p.Value.GetCount()
			i = 0
			for i in range(0,p.Value.GetCount()):
				x =  p.Value[i].this

				print x
				# shit = MaxPlus.Core.EvalMAXScript("'%s'" % p.Value)

				# print (str(shit) + " dddd")
				# print p.Value[i].FindDependentNode()

			# for v in p.Value:
			# 	print str(v)
			# 	print str(v.GetNumRefs())

