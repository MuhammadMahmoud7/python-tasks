def Check_Positive_and_Even_Numbers(Size) :
	list=[]
	counter1 = 0 
	counter2 = 0
	print("Enter elements : ")
	for i in range(Size) :
		Elements = int(input())
		list.append(Elements)
		if list[i] > 0 :
			counter1 +=1 
		if list[i]%2 == 0 :
			counter2 +=1
	print("Number of Positive numbers = " , counter1)
	
	print("Number of even numbers = " , counter2)		





Size = int(input("Enter Size of List : "));

Check_Positive_and_Even_Numbers(Size)
