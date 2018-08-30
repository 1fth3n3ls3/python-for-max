import MaxPlus

#Get Selected nodes

selected_nodes = MaxPlus.SelectionManager.Nodes

#move nodes


#add modifier

for each in selected_nodes:


	mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.Class_ID(0x9c92c88, 0x13d466dc))
	MaxPlus.ModifierPanel.AddToSelection(mod)