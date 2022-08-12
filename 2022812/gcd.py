#  최대 공약수
# 약수  자신을 나눌수 있는수 들의 집합
# 16 : 1 2 4 8 16
# 14  : 1 2 7 14
# gcd

## 16,14
# 16 % 14  : 2

# 14,2
# 14 % 2  0

def gcd(x:int, y:int)->int:
    if y == 0:
        return x
    else:
        return gcd( y, x % y)

if __name__ =="__main__":
    print("두 정수값을 입력하세요 : ")
    x = int(input("첫번째 정수 : "))
    y = int(input("두번째 정수 : "))
    print(f"두 정수 {x} {y}의 최대공약수(gcd) = {gcd(x,y)}")