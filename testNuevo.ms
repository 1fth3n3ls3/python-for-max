clearlistener()
code = 
"
import MaxPlus
the_node = MaxPlus.INode.GetINodeByName('Point001')
MaxPlus.Core.EvalMAXScript( 'global s = the_node')
"
python.Execute code
print s