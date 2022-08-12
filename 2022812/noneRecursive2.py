# 마지막 재귀함수를 비 재귀적 표현으로 변경  while
def recur(n:int) ->int:
    while n > 0:
        recur(n - 1)
        print(n)
        n -= 2 # 비 재귀형태로 변경

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

