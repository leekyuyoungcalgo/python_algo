# 재귀알고리즘 분석
# 하양식 분석(top-down)   상향식  bottom - up 분석
def recur(n:int) ->int:
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2) # 비 재귀형태로 변경

if __name__ == "__main__":
    x = int(input("정수값을 입력 : "))
    recur(x)

