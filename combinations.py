from itertools import permutations
n=(input("enter the numbers="))
p=permutations(n)
for i in list(p):
    print(i)