def Palindrome(Word) :
	reverse=Word[::-1]
	if Word==reverse:
		print("This string is palindrome")
	else :
		print("This sting is not palindrome")
Word=str(input("Enter your Word : "));
Palindrome(Word)
