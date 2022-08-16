list_a = [5,4,2,1,8,9]
size = len(list_a)

# print(f"orginal {list_a}")
# for i in range(size-1,0,-1):
#     if list_a[i] < list_a[i-1]:
#         list_a[i], list_a[i - 1] = list_a[i-1], list_a[i]
#
#
# print(f"1 cicle {list_a}")
# for i in range(size-1,1,-1):
#     if list_a[i] < list_a[i-1]:
#         list_a[i], list_a[i - 1] = list_a[i-1], list_a[i]
#
# print(f"2 cicle {list_a}")

from typing import MutableSequence  # 변경가능한 집합
def bubble_sort(a : MutableSequence, asc=True)->int:
    size = len(a)
    cnt = 0
    for j in range(size):
        exchange = 0
        cnt += 1
        for i in range(size - 1, j, -1):
            if asc:   # 오름차순
                if a[i] < a[i - 1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
                    exchange += 1
            else:   # 내림차순
                if a[i] > a[i - 1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
                    exchange += 1
        if exchange == 0:
            return cnt
    return cnt



if __name__ == '__main__':
    list_a = [2,1,3,4,5,6,7,8,9,10]
    cnt = bubble_sort(list_a)
    print(cnt)
    # from random import sample
    # list_a = sample(range(60,100),10)
    # print(f"before bubble sort : {list_a}")
    # bubble_sort(list_a)
    # print(f"after bubble sort : {list_a}")
    # bubble_sort(list_a,False)
    # print(f"after bubble sort : {list_a}")
    # top3 = list_a[:3]
    # print(f"top3 = {top3}")

