import MaxPlus, sys

MaxPlus.Core.EvalMAXScript("clearlistener()")

the_node = MaxPlus.INode.GetINodeByName("Point001")

tabRef = the_node.BaseObject.GetCustomAttributeContainer()[0].ParameterBlock

print tabRef

print tabRef.Count()


node_transform_monitor = tabRef[0]

print node_transform_monitor.GetValue()
print node_transform_monitor.Value

print node_transform_monitor.Value[0].Refs


print dir(node_transform_monitor.Value[0].Refs)

# How to get node transform monitor target from a maxscript

x = MaxPlus.Core.EvalMAXScript("$'%s'.nodeRefs[1].node" % the_node.GetName()) 

y = x.Get()

print y.GetName()
