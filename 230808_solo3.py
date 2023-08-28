
a=[]
for i in range(28):
    b = int(input())
    a.append(b)
    
for j in range(28):
    j += 1
    if j in a:
        continue    
    else:
        print(j)
        