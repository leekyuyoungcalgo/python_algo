def heap_sort(a,left,right):
    def down_heap(a, left, right):
        temp = a[left]
        parent = left
        while parent < (right+1) // 2:
            cl = parent*2 +1
            cr = cl+1
            child = cr if cr<= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)
    # heap을 만들어줌
    for i in range((n-1)//2,-1,-1):
        down_heap(a, i, n-1)
    
    #  루트에서 데이터를꺼내서 다시 최소값을 루트로 보내고 자식과 교환하면서 heap구조를 만든
    for i in range(n-1,0,-1):
        a[0], a[i] = a[i], a[0]
        down_heap(a,0,i-1)
    
