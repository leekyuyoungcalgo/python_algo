from typing import MutableSequence
def merge_sort(a: MutableSequence)->None:
    def _merge_sort(a,left:int, right:int)->None:
        if left < right:
            center = (left + right) // 2
            _merge_sort(a, left,center)  # 앞부분을 정렬
            _merge_sort(a, center+1, right) # 뒷부분을 정렬
# 병합
            p = j = 0
            i = k = left
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a,0,n-1)
    del buff

from random import sample
if __name__=="__main__":
    x = sample(range(100),10)
    print(x)
    merge_sort(x)
    print(x)
