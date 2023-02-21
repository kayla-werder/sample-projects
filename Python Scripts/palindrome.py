def isPalindrome(w):
    sentence = w.lower()
    no_spaces = sentence.replace(" ", "")
   
    if not no_spaces:
        print("Not a palindrome")
        return 0
    
    if(no_spaces == no_spaces[::-1]):
        return True
    else:
        return False
            

word = input("Please enter your phrase: ")

answer = isPalindrome(word)

if answer : print("It is a palindrome")
else: print("Not a palindrome")
