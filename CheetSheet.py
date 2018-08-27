from pymxs import runtime as rt

#clear listener

rt.clearlistener()

#get selection

mySelection = rt.selection

for each in mySelection:
	
	print each.name
	
#get first selected

firstItem = rt.selection[0]

print firstItem.name

#create simple object

rt.sphere(radius=50, position=rt.point3(25, 25, 25), segments=8)

#select all objects

rt.select(rt.objects)

#clear selection

rt.clearselection()


rt.select(firstItem)

print rt.firstItem.name


rt.selection[0].name = 'PorTuCulpa'



