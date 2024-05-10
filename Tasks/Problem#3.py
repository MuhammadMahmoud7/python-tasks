def Calculations (a,b,operation) :
	result = 0
	if operation == "+" :
		result = a + b 
		print(a,operation,b,"=",result)
	elif operation == "-" :
		result = a - b 
		print(a,operation,b,"=",result)
	elif operation == "*" :
		result = a * b 
		print(a,operation,b,"=",result)
	elif operation == "/" :
		result = a / b 
		print(a,operation,b,"=",result)
	elif operation == "%" :
		result = a % b 
		print(a,operation,b,"=",result)
	elif operation == "^" :
		result = a ** b 
		print(a,operation,b,"=",result)	
	else :
		print("Character undefined")						




a=float(input("Enter 1st number = "))
b=float(input("Enter 2nd number = "))
operation = input("Enter the char that you want from these operation (+,-,*,/,%,^): ")

Calculations(a,b,operation)
