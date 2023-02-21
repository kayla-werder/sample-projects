def anagrams(str1, str2):
    lower_str1 = str1.lower()
    lower_str2 = str2.lower()
    no_spaces_str1 = lower_str1.replace(" ", "")
    no_spaces_str2 = lower_str2.replace(" ", "")
    
    if(sorted(no_spaces_str1) == sorted(no_spaces_str2)):
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")

    
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

anagrams(string1, string2)