x = 1
h = (x * x * x - x * x + 2) / (3 * x * x - 2 * x)
while (-0.0001 >= h or h >= 0.0001):
    h = (x * x * x - x * x + 2) / (3 * x * x - 2 * x)
    
    x = x - h

print('rishe = ',x)
