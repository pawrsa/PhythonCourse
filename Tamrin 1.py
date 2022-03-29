n = 20
s = 0
x = float(input('Enter the Daraje : '))
pi = 3.1415
x = x * pi/180
for i in range(n):
    f = 1
    for j in range(1 , 2*i + 2):
        f*=j
    s += ((-1) ** i) * ((x ** (2*i + 1)) / f)

print('sinus barabar ast ba : ' , s)