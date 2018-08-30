--python.ExecuteFile @"F:\3dsMax2016\3ds Max 2016\scripts\Python\demoBentCylinder.py"

-- x = box()
-- select x 
-- $.name = "test"

clearListener()

x = nodeTransformMonitor node:selection[1] forwardTransformChangeMsgs:false

print x

print x.node

-- print x.node.name

