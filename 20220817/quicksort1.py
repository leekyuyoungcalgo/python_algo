# partition과 비슷 sort
def sort(a, left,right):
    pl = left
    pr = right
    x = a[(left+right) // 2]

    while pl <= pr:
        while a[pl] < x : pl += 1 # x보다 큰 값을 찾는과정
        while a[pr] > x: pr -= 1 # x보다 작은 값을 찾는과정
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr : sort(a, left, pr)
    if pl< right : sort(a, pl, right)

def quick_sort(a):
    sort(a, 0, len(a)-1)

if __name__ =="__main__":
    print("배열을 나눕니다.")
    num = int(input("원소의 수를 입력"))
    x = [None]*num
    for i in range(num):
        x[i] = int(input(f"x[{i}] :"))

    quick_sort(x)
