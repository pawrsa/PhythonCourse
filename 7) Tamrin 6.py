
a = float(input('enter a number: '))
s = 0
count = 0
while(a >= 0):
    if(count == 0):
        minimum = a
        maximum = a
    else:
        if(maximum < a):
            maximum = a
        if(minimum > a):
            minimum = a
    s += a
    count += 1
    a = float(input('enter a number: '))

print('avg = ' , s / count)
print('min = ' , minimum)
print('max = ' , maximum)
    
