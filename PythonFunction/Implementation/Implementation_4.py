# 왕실 정원은 8 x 8 좌표 평면
# 나이트는 L자 형태로만 이동하고 정원 밖으로는 나갈 수 없음
# L자 형태
# > 수평으로 두칸, 수직으로 한칸
# > 수직으로 두칸, 수평으로 한칸
# 행 위치는 1~8로 표현, 열 위치는 a~h로 표현

input_data = input()  # 문자열 입력받음 (b3, a2 ..)
row = int(input_data[1])  # 1번째 문재를 int형으로 row에 저장
col = int(ord(input_data[0])) - int(ord('a')) + 1  # 0번째 문자(알파벳)을 아스키코드 변환을 통하여 숫자로 저장

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1),
         (1, 2), (-1, 2), (-2, 1)]

count = 0

for step in steps:
    next_row = row + step[0]  # row 값 이동
    next_col = col + step[1]  # col 값 이동

    if next_row >=1 and next_row <=8 and next_col >=1 and next_col <=8:
        count += 1

print(count)