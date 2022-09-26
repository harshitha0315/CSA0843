def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print('the strings are anagram')
    else:
        print('the strings are not anagram')
s1=str(input("enter a word:"))
s2=str(input("enter another word:"))
check(s1,s2)
