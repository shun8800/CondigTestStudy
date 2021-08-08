# 내장 함수 : 기본 입출력 함수부터 정렬 함수 등을 제공
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능
# - 순열 / 조합 라이브러리
# heapq : 힙 자료구조 제공
# - 우선순위 큐 기능을 구현하기 위해 사용(다익스트라 등)
# bisect : 이진 탐색 기능 제공
# collections : 덱, 카운터 등의 유용한 자료구조 포함
# math : 필수적인 수학기능 제공
# - 팩토리얼, 제곱근, 최대공약수 등..

sum_result = sum((1, 2, 3, 4, 5)) # sum() = 리스트나 튜플의 합 반환
min_result = min(5, 4, 2, 5) # min() = 가장 작은 값 반환
max_result = max(5, 10, 8 ,6) # max() = 가장 큰 값 반환
eval_result = eval("(3+5)*7") # eval() = ""로 표현된 식의 값 반환
sort_result = sorted([5, 4, 2, 3]) # sorted() = 리스트나 튜플 오름차순 정렬
sort_reverse_result = sorted([5, 4, 2, 3], reverse=True)
# reverse로 내림차순 정렬

array = [('홍길동', 54), ('이순신', 75), ('아무개', 42)]
lambda_result = sorted(array, key=lambda x:x[1], reverse=True)
# 묶음으로 정의된 리스트 array
# array를 sort 할 건데 key(기준)을 x값 중 2번째 값(x[1])으로 잡을 것이다
# lambda는 묶음으로 정의된 리스트를 구분할 때 사용하는듯?


# 순열과 조합 경우의 수 뽑기(라이브러리 사용)

from itertools import permutations, combinations

data = ['A', 'B', 'C']
result_per = list(permutations(data, 3)) # data에서 3개를 뽑아서 순열 결과
result_com = list(combinations(data, 3)) # data에서 3개를 뽑아서 조합 결과

from itertools import product, combinations_with_replacement

data = ['A', 'B', 'C']
result_pro = list(product(data, repeat=2)) # data에서 순열 2개를 뽑는데 중복 허용
result_repl = list(combinations_with_replacement(data, 2))
# data에서 조합 2개 뽑는데 중복 허용
print(result_pro)
print(result_repl)

# Collections 라이브러이의 Counter는 등장 횟수를 세는 기능
# 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부 원소가 몇 번 등장하는지 확인

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'green', 'blue'])

print(counter) # Counter(dict) 형태로 정리
print(counter['red']) # counter에서 red가 몇개?
print(counter['green']) # counter에서 green이 몇개?
print(counter['blue']) # counter에서 blue가 몇개?
print(dict(counter)) # counter에서 dict 정보만 가져오기
# {red 몇개? blue 몇개? green 몇개?}


# 최대 공약수 = math 라이브러리의 gcd() 함수
# 최소 공배수 = lcm = a*b // math.gcd(a,b)

import math

def lcm(a, b): # 최소 공배수 구하는 함수
    return a*b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(a, b)) # a와 b의 최대공약수
print(lcm(a, b)) # a와 b의 최소공배수 = a*b // gcd(a,b)