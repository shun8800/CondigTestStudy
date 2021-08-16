# 재귀함수 : 자기 자신을 다시 호출(종료 조건 필요)

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