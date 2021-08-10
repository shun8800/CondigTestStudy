# 0~9로 이루어진 문자열 S
# 왼쪽부터 오른쪽까지 * 또는 + 연산자를 넣음
# 연산자 우선순위와 상관 없이 왼쪽부터 수행
# 가장 큰 수를 만들어보자

# 조건 : 1 <= 문자열 S <= 20
# 보통 +보다 *가 값을 더 크게 만듦
# 하지만 하나라도 0, 1인 경우 *보다 +가 값을 더 크게 만듦
# 즉, 두 수가 하나라도 1 이하라면 +, 아니라면 *

data = list(map(int, input().split()))   # 입력값을 여러개를 받음

result = data[0]  # 그 중 첫번째 값을 정수형으로 변환

for i in range(1, len(data)):   # 두번째 값부터 마지막 값까지 반복
    num = data[i]  # i번째 값을 정수형으로 변환해서 num에 대입

    if num <= 1 or result <= 1:     # 만약 num 또는 result가 1보다 작다면
        result += num   # 0번째 값 + num

    else: # 그게 아니라면
        result *= num # 0번째 값 * num

print(result)
