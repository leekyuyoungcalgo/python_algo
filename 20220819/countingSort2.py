from typing import MutableSequence
def fsort(a: MutableSequence, max:int)->None:
    # 원소의값은 0이상 max이하
    n = len(a)
    f = [0]*(max+1)
    b = [0]*n
    # 도수 분포표  : 해당 값을 인덱스로 가지는 배열을 만들어서 count하면 해당 값이 몇번? 나왔는지 알수있음
    for i in range(n): f[a[i]] += 1 # 1 step
    # 누적 도수 분포표 : 0 ~ n까지 몇개의 데이터가 있는지 누적된 값을 나타냄
    for i in range(1,max+1) : f[i] += f[i-1]
    # 작업용 배열 : 원래배열의 원소값과 누적도수 분포표를 대조해서 정렬을 완료한 배열
    for i in range(n-1, -1, -1) : f[a[i]] -=1 ; b[f[a[i]]] = a[i]
    for i in range(n) : a[i] = b[i]

def countingSort(a:MutableSequence)->None:
    fsort(a, max(a))

def main()->None:
    from random import sample
    data = sample(range(1000),10)
    print(f"original : {data}")
    countingSort(data)
    print(f"sorted : {data}")

if __name__=="__main__":
    main()
