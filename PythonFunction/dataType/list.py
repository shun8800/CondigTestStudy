a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[3])
print(a[-1]) # 뒤에서 부터
print(a[-3])
print(a[1:4])
# 1번째 인덱스부터 3번째 인덱스 까지
# a[x:y+1] : x번째 인덱스부터 y번째 인덱스까지

n = 10
a = [2] * n
print(a)

# 리스트 컴프리헨션

array = [i for i in range(10)]
# i 값을 array 원소로 넣는데, i 값을 in range(10)로 설정한다
print(array)

array = [i for i in range(20) if i%2==1]
print(array)

array = [i*i for i in range(1, 10)]
print(array)


# N*M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0]*m for _ in range(n)]
# array = [[0]*m]*n 은 잘못된 방법
# _는 연관된 값이 없을때? 사용
print(array)

# 변수명.append() : 원소 하나 삽입
# 변수명.sort() : 오름차순 정렬
# 변수명.sort(reverse = True) : 내림차순 정렬
# 변수명.reverse() : 리스트의 원소의 순서를 모두 뒤집음
# insert(삽입할 위치 인덱스, 삽입할 값) : 특정 인덱스에 값 삽입
# 변수명.count(특정 값) : 리스트에서 특정한 값을 가지는 데이터의 개수를 셈
# 변수명.remove(특정 값) : 특정 원소 값 제거(여러개면 하나만 제거)

a = [1, 4, 3]
print("기본 리스트 : ", a)

a.append(2)
print("삽입 : " , a)

a.sort()
print("정렬 : " , a)

a.sort(reverse=True)
print("내림차순 정렬 : " , a)

a.reverse()
print("원소 뒤집기 : ", a)

a.insert(2, 3)
print("인덱스 2 위치에 3 추가 : ", a)

print("3 값 세기 : ", a.count(3))

a.remove(1)
print("값 1 제거 " , a)

a = [1, 2, 3, 3, 4, 4, 5, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print("remove_set(3, 5)이 제외된 리스트 : ", result)