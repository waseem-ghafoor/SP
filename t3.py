#task3
list=[]
userData = input("enter values with comma separated		")
for i in userData.split(','):
	list.append(i)
tple=tuple(list)
print(list  ,'|',  tple)
