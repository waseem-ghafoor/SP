#task2
initial=1
upperLimit = int(input('Enter Upper Range: '))

dict={}

for i in range(initial,upperLimit+1):
	temp={i:i*i}
	dict.update(temp)
print(dict)