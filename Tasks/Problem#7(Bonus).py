def Vowels_and_Consonants(String) :
	Temp = ""
	for i in String :
		if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" :
			Temp +=("."+i)
	String = Temp
	return String		
			
String = str(input("Enter your string : "))
print("The String is :" ,Vowels_and_Consonants(String))


