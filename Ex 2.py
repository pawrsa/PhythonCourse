x = int(input('Enter the (x) : '))
y = int(input('Enter the (y) : '))

if(x > y):
    x , y = y , x
for i in range(1 , x + 1):
    if(x % i == 0 and y % i == 0):
        bmm = i


print('bmm =',bmm)