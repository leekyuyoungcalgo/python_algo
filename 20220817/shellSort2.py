# h값이 서로 배수가 되면 교환작업을 할때 간섭현상때문에 결국 다시 돌아가는 현상
# 1부터 시작해서 3배한 값에 1을 더하는 수열을 적용
from typing import  MutableSequence

def shell_sort(a:MutableSequence)->None:
    n = len(a)
    h = 1
    while h < n // 9:
        h = h*3+1

    while h > 0:
        for i in range(h,n):
            j = i-h
            tmp = a[i]
            while j>=0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 3

def main():
    print("쉘정렬")
    num = int(input("원소의 수를 입력하세요 : "))
    x = [None]*num
    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))

    shell_sort(x)

    for i in x:
        print(i,end=" ")
    print()




if __name__=='__main__':
    main()
