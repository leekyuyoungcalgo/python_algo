# 배열을 나누기 퀵정렬용...
from typing import MutableSequence

def partition(a: MutableSequence) ->None:
    n = len(a)
    pl = 0 # 왼쪽
    pr = n-1 # 오른쪽
    x = a[n//2] # 피벗(가운데)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    print(f"피벗은 {x}")
    print(f"피벗이하 그룹")
    print(a[:pl])
    if pl > pr+1:
        print("피벗하고 일치하는 그룹")
        print(a[pr+1:pl])
    print("피벗이상 그룹")
    print(a[pr+1:n])

#  __name__ 해당파일이 독립적으로 실행되면 값은 __main__
# 해당파일이 다른파이썬파일에서 import 가 되어 사용되면 __name__  파이썬 파일명을 반환
if __name__ =="__main__":
    print("배열을 나눕니다.")
    num = int(input("원소의 수를 입력"))
    x = [None]*num
    for i in range(num):
        x[i] = int(input(f"x[{i}] :"))

    partition(x)



