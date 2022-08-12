# 마지막 재귀함수를 비 재귀적 표현으로 변경  스택
from stack import FixedStack
def recur(n:int) ->int:
    s = FixedStack(n)
    while True:
        if n > 0:  #  스택을 채움
            s.push(n)
            n -= 1
            continue
        if not s.isEmpy():
            n = s.pop()
            print(n)
            n -= 2
            continue
        break
if __name__ == "__main__":
    x = int(input("정수값을 입력 : "))
    recur(x)

# 1
# 2
# 3
# 1
# 4
# 1
# 2

