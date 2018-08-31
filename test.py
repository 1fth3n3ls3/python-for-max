import MaxPlus

#Get Selected nodes

selected_nodes = MaxPlus.SelectionManager.GetNodes()

n = len(selected_nodes)

newSelection = MaxPlus.INodeTab()

for each in range(0, n):
	print selected_nodes[each].GetName()
	if each == 1:
		newSelection.Append(selected_nodes[each])

MaxPlus.SelectionManager.ClearNodeSelection()
MaxPlus.SelectionManager.SelectNodes(newSelection)

#move nodes


#add modifier

# for each in selected_nodes:


# 	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
# 	MaxPlus.ModifierPanel.AddToSelection(mod)