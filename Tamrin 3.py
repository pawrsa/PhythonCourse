for i in range(1 , 10001):
    s = 0
    str_i = str(i)
    tool = len(str_i)
    for ch in str_i:
        s += int(ch)**tool
    if(s == i):
        print(i)

