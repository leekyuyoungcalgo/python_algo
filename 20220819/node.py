from __future__ import  annotations
class Node:
    def __init__(self, data = None, next : Node = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.no = 0   # 노드의 개수
        self.head = None  # 헤더
        self.current = None # 현재 노드(탐색중...)
    def __len__(self)->int:
        return self.no

    def search(self,data)->int:
        cnt = 0 # 노드의 위치
        ptr = self.head # 검색위치의 노드 head로 초기화
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    def __contains__(self, item)->bool:
        return self.search(item) >=0

    def add_first(self,data)->None:  # 새로운 노드를 head로 만든다
        ptr = self.head
        self.head = self.current = Node(data,ptr)
        self.no += 1

    def add_last(self,data)->None:
        if self.head is None: # 비어있는 링크드 리스트
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current =  Node(data,None)
            self.no += 1
    def remove_first(self)->None:
        if self.head is not None:  # 비어있지 않으면
            self.current = self.head = self.head.next
            self.no -= 1
    def remove_last(self)->None:
        if self.head is not None: # 비어있지 않으면
            if self.head.next is None: # 노드가 하나 있을때
                self.remove_first()
            else:
                ptr = pre= self.head # head 실제 존재하지 않고 첫번째 노드를 나타내는 상징적인 표식
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1
    def remove(self,p:Node)->None:
        if self.head is not None:  # 비어있지 않으면
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_nod(self)->None:
        self.remove(self.current)

    def clear(self)->None:
        self.head = self.current = None
        self.no = 0
    def next(self)->bool:
        if self.head is not None or self.current.next is not None:
            self.current = self.current.next
            return True
        else:
            return False
    def print_current_noe(self)->None:
        if self.current is None:
            print("탐색중인 노드가 없습니다.")
            return
        print(self.current.data)
    def print(self)->None:
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, head : Node)->None:
        self.current = head
    def __iter__(self)->LinkedListIterator:
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

if __name__ == '__main__':
    # 1 머리에 노드 삽입
    list = LinkedList()
    list.add_first(10)
    list.add_last(20)
    list.add_last(30)
    list.add_last(40)
    list.add_first(50)
    list.print()  # 50 10 20 30 40
    list.remove_first()  # 10 20 30 40
    list.remove_last() # 10 20 30
    print("------------------------------")
    list.print()
    print("------------------------------")
    list.print_current_noe()
    searchdata = 20
    print(f"{list.search(searchdata)+1} 번재 위치함")
    print("------------------------------")

    for i in list:
        print(i)

# 배열의 단점을 보완   삽입과 삭제를 하면 실제로 데이터를 이동.... 성능저하
# 리스트는 삽입 삭제가 빠르다.. 단점....링크드 리스트를 구현... 특정위치의 데이터를 접근하려면 .. 처음 searh..
