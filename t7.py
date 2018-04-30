#task7
digitsCounts=0
lettersCounts=0

line= input("enter sentence	")
for i in line:
	if i.isalpha():
		lettersCounts += 1
	if i.isdigit():
		digitsCounts += 1
		
	
print("letter are", lettersCounts,"| letter are",digitsCounts)