string=str(input("enter the string:"))
char=0
word=1
for i in string:
    char=char+1
    if(i==' '):
        word=word+1
print('the number of words in the string is:',word,)
print('the number of characters in the string is:',char,)
