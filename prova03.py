M = int(input(''))
F1 = int(input(''))
F2 = int(input(''))

F3 = M - (F1 + F2) 

if F1 > F2 and F1 > F3:
    print(F1)
elif F2 > F1 and F2 > F3:
    print(F2)
else:
    print(F3)