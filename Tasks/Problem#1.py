def Calc_Standard_Deviation (number1,number2,number3):
	list = [number1,number2,number3]
	mean = (number1 + number2 + number3) / 3 
	summ = 0 ;
	for i in list :
		summ = summ + (i-mean)**2
		result = 1/3 * summ ;
	return result**0.5	


number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))

print("Standard Deviation = ",Calc_Standard_Deviation(number1,number2,number3))
