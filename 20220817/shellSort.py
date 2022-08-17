from typing import  MutableSequence

def shell_sort(a:MutableSequence)->None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h,n):
            j = i-h
            tmp = a[i]
            while j>=0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 2

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
