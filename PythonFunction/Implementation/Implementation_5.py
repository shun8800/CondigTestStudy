# 알파벳 대문자와 숫자(0, 9)로만 구성된 문자열 입력
# 모든 알파벳을 오름차순으로 정렬하여 출격하고, 그 뒤 모든 숫자를 더해서 출력
# K1KA5CB7 => ABCKK13 으로 정렬

data = input()  # 문자열로 data값 받음
result = []  # 문자열을 받을 result 리스트 선언
value = 0  # 정수 값을 받을 value 선언

for x in data:
    if x.isalpha():  # 문자열 순회 중에 만약에 x가 문자열이라면
        result.append(x)  # result에 추가
    else:  # 아니라면
        value += int(x)  # x를 int형 변환을 통해 value에 저장

result.sort()  # result에 저장된 문자열 정렬

if value != 0:  # 저장된 정수 값이 0이 아니라면
    result.append(str(value))  # 정수로 받은 value를 str형태로 다시 result 리스트에 추가

print(''.join(result))  # result 리스트를 문자열로 정리
