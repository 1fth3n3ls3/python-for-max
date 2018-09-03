import MaxPlus, sys

#Get Selected nodes

<<<<<<< HEAD
# selected_nodes = MaxPlus.SelectionManager.Nodes
=======
selected_nodes = MaxPlus.SelectionManager.GetNodes()

n = len(selected_nodes)

newSelection = MaxPlus.INodeTab()

for each in range(0, n):
	print selected_nodes[each].GetName()
	if each == 1:
		newSelection.Append(selected_nodes[each])

MaxPlus.SelectionManager.ClearNodeSelection()
MaxPlus.SelectionManager.SelectNodes(newSelection)
>>>>>>> 499872690918df8b119a983d6d22a935096cf796

#move nodes


#add modifier

# for each in selected_nodes:
<<<<<<< HEAD


# 	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
# 	MaxPlus.ModifierPanel.AddToSelection(mod)

# Ejemplo de seleccion de tabnodes propios

# selected_nodes = (MaxPlus.SelectionManager.GetNodes())



# myList = MaxPlus.INodeTab()
=======
>>>>>>> 499872690918df8b119a983d6d22a935096cf796

# for i in range( 0, len(selected_nodes)):

<<<<<<< HEAD
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
=======
# 	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
# 	MaxPlus.ModifierPanel.AddToSelection(mod)
>>>>>>> 499872690918df8b119a983d6d22a935096cf796
