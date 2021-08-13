# 어떠한 수 N이 1이 될 때 까지 두 과정 중 하나를 반복적으로 선택하여 수행하려고 함
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있음
# 1. N에서 1을 뺌
# 2. N을 K로 나눔
# 예를 들어, N = 17, K = 4
# 1번을 선택하여 N - 1 = 16
# 2번을 2번 선택하여 16 / 4 / 4 = 1, 총 3번의 연산


# 조건 : 1 <= N <= 100,000 / 2 <= K <= 100,000
# 가능하면 K 값으로 최대한 많이 나누기를 수행하면 됨
# 2번이 가능할 때까지 1번을 수행(최적의 해 구하기 - 그리디)

n, k = map(int, input().split()) # 공백을 기준으로 두 수 입력
result = 0 # 최적의 연산 횟수

while True:
    target = (n//k) * k   # n을 k로 나눈 몫에 k를 곱함
    result += (n-target)  # 1번 연산(-1)을 몇 번 수행하는지 확인
    n = target  # 나누기 연산이 되는 값을 n에 대입

    if n < k:
        break
    n //= k # 나누기 연산
    result += 1 # 2번 연산(n/k)이 수행될 때마다 연산 횟수 +1

result += (n-1)
print(result)

