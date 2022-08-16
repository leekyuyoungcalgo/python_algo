a = [3, 4, 2, 3, 1]
# 1 cycle

n = len(a)
for i in range(n-1):
    min = i
    for t in range(i+1,n):   # 1 2 3 4 ....
        if a[t] < a[min]:
            min = t
    a[i], a[min] = a[min], a[i]   # a[0] a[1] a[2]

print(a)

