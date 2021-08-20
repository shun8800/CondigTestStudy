# 정렬 : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
# 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용 됨

# 선택 정렬 : 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸는 것

# 선택 정렬 : O(N^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)




