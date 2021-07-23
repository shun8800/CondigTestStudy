# 사전 자료형 : 키와 값을 쌍으로 가지는 자료형
# 키와 값의 쌍을 데이터로 가지고, 변경 불가능한 값을 자료형을 키로 사용
# 해시 테이블을 이용하기 때문에 데이터의 조회 및 수정을 O(1)에 가능
# 키 데이터만 뽑아서 리스트를 사용할 때는 keys() 함수
# 값 데이터만 뽑아서 리스트를 사용할 때는 values() 함수

data = dict()
data["사과"] = 'Apple'
data["바나나"] = 'Banana'
data["코코넛"] = "Coconut"

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

key_lists = data.keys()
value_lists = data.values()

print(key_lists)
print(value_lists)
# 이렇게 하면 하나의 객체로 받음

key_lists = list(data.keys())
value_lists = list(data.values())
# 이렇게 하면 하나의 객체였던 것을 리스트로 받음(list 형변환)

print(key_lists)
print(value_lists)
# 이렇게 하면 하나의 객체로 받음


for key in key_lists:
    print(data[key])
# 접근은 키-값 으로만 가능
# 값 - 키로는 불가능