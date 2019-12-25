def func(index):
    f = [0,1]
    for i in range(1,index):
        f.append(f[i]+f[i-1])
    f = tuple(f)
    print(f)
