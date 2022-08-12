from typing import Any
class FixedStack:
    class Empty(Exception):
        def __init__(self):
            super.__init__("Stack Empty.")
    class Full(Exception):
        def __init__(self):
            super.__init__("Stack Full.")
    def __init__(self,capacity: int = 256)->None:
        self.stk =  [None]*capacity
        self.capacity = capacity
        self.ptr = 0
    def __len__(self)->int:
        return self.ptr
    def isEmpy(self) ->bool:
        return self.ptr <= 0
    def isFull(self)->bool:
        return self.ptr >= self.capacity
    def push(self,value:Any)->None:
        if self.isFull():
            raise FixedStack.Full

        self.stk[self.ptr] = value
        self.ptr += 1
    def pop(self) -> Any:
        if self.isEmpy():
            raise FixedStack.Empty
        self.ptr -= 1;  # self.ptr = self.ptr - 1
        return self.stk[self.ptr]
    def peek(self)->Any:
        if self.isEmpy():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self) ->None:
        self.ptr = 0

    def terminate(self)->None:
        self.ptr = self.capacity = 0

    def search(self, value:Any)->Any:
        for i in range(self.ptr-1,-1,-1):
            if value == self.stk[self.ptr]:
                return i
        return -1

    def count(self,value:Any)->int:
        cnt = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                cnt += 1
        return cnt
    def __contains__(self, item:Any)->bool:
        return self.count(item)
    def showAllStacks(self,type:int = 0):
        # 리스트 .... for X
        # 리스트 슬라이싱 방식으로 표현
        print(self.stk[:self.ptr])