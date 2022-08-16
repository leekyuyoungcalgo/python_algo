list_a = [9, 1, 3, 4, 6, 7, 8]
# 홀수 일때는 뒤에서 앞으로 가장 작은값을 앞으로
# 짝수일 때는 앞에서 뒤로 가장큰값을 뒤로

# 1 path or 1cycle
size = len(list_a)
# for i in range(size-1,0,-1):
#     if list_a[i-1] > list_a[i]:
#         list_a[i - 1], list_a[i] = list_a[i], list_a[i-1]
#
#
# for i in range(1,size-1):
#     if list_a[i] > list_a[i+1]:
#         list_a[i + 1], list_a[i] = list_a[i], list_a[i + 1]


from typing import  MutableSequence
def shake_sort(a:MutableSequence)->None:
    left = 0
    right = len(a) - 1
    last = right

    while left < right:
        for i in range(right,left,-1):
            if list_a[i-1] > list_a[i]:
                list_a[i - 1], list_a[i] = list_a[i], list_a[i - 1]
                last = i
        left = last

        for i in range(left, right):
            if list_a[i] > list_a[i+1]:
                list_a[i + 1], list_a[i] = list_a[i], list_a[i + 1]
                last = i
        right = last

print(f"original {list_a}")
shake_sort(list_a)
print(f"sorted... {list_a}")
