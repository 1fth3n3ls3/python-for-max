import MaxPlus, sys

# MaxPlus.Core.EvalMAXScript("clearlistener()")

the_node = MaxPlus.INode.GetINodeByName("Point001")

tabRef = the_node.BaseObject.GetCustomAttributeContainer()[0].ParameterBlock

print tabRef
node_transform_monitor = tabRef[0]
print node_transform_monitor.Value

print node_transform_monitor.Value[0]



