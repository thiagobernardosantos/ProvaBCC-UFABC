L = int(input(''))
C = int(input(''))

if L % 2 == 0 and C % 2 == 0:
    print('1')
elif L % 2 == 0 and C % 2 == 1:
    print('0')
elif L % 2 == 1 and C % 2 == 0:
    print('0')
else: 
    print('1')