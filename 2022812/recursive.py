# 5! 5*4*3*2*1

def nonRecursive(n:int)->int:
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(f"non recursive result = {nonRecursive(10)}")

def recursive(n:int)->int:
    if n > 0:
        return n * recursive(n-1)
    else:
        return 1
print(f"recursive result = {recursive(10)}")