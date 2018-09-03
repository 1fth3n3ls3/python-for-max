import MaxPlus, sys

#Get Selected nodes

# selected_nodes = MaxPlus.SelectionManager.Nodes

#move nodes


#add modifier

# for each in selected_nodes:


# 	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
# 	MaxPlus.ModifierPanel.AddToSelection(mod)

# Ejemplo de seleccion de tabnodes propios

# selected_nodes = (MaxPlus.SelectionManager.GetNodes())



# myList = MaxPlus.INodeTab()

# for i in range( 0, len(selected_nodes)):

# 	myList.Append(selected_nodes[1])

# 	# print str(selected_nodes[i].GetName())
# MaxPlus.SelectionManager.ClearNodeSelection()
# MaxPlus.SelectionManager.SelectNodes(myList)

# for each in selected_nodes:
# 	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
# 	MaxPlus.ModifierPanel.AddToSelection(mod)

# 	i = 0
# 	for p in mod.ParameterBlock:

# 		type_name = MaxPlus.FPTypeGetName(p.Type)
# 		try:
# 			print '  parameter', i, p.Name, p.Type, type_name, p.Value
# 			i += 1
# 		except:
# 			etype, evalue = sys.exc_info()[:2]
# 			print 'error '. etype, evalue


selected_nodes = (MaxPlus.SelectionManager.GetNodes())

for each in selected_nodes:
	n = each.GetNumModifiers()
	mod = each.GetModifier(n - 1) #accedo al último de la lista
	print str(mod)
