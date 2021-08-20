# 재귀함수 : 자기 자신을 다시 호출(종료 조건 필요)

'''
def factorial(n):
    result = 1

    for i in range(1, n+1):
        result = result * i

    return result

def factorial_recursive(n):
    if n<=1:
        return 1

    else:
        return n * factorial_recursive(n-1)

print('반복적으로 구현 : ', factorial(5))
print('재귀적으로 구현 : ', factorial_recursive(5))
'''

# 최대공약수 계산 (유클리드 호제법)
# 두 자연수 A와 B에 대하여 A와 B를 나눈 나머지를 R로 정의
# A와 B의 최대 공약수는 B와 R의 최대공약수와 같음


def uclid(a, b):
    r = a % b

    if r == 0:
        return b
    else:
        return uclid(b, r)

uclid(192, 160)
