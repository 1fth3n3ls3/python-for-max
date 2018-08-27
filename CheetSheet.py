from pymxs import runtime as rt

#get selection

mySelection = rt.selection

for each in mySelection:
	
	print each.name
	
#get first selected

firstItem = rt.selection[0]

print firstItem.name

#create simple object

rt.sphere(radius=5, position=rt.point3(25, 25, 25))

#select all objects

rt.select(rt.objects)

#clear selection

rt.clearselection()

