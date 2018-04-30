#task6
line= input("enter sentence	")
list=[]

for i in line.split(' '):
	if list.count(i) == 0:
		list.append(i)
	
	list.sort()
print("duplicates are  removed and sorted list is",list)
