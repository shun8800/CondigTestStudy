# 퀵정렬 : 기준 데이터를 설정하고 그 기준보다 작은 데이터의 위치를 바꾸는 방법
# 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# 첫 번째 데이터를 기준 데이터(Pivot)으로 설정

# 퀵정렬 : O(NlogN) or O(N^2)
'''
방법 1

def quick_sort(array, start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end

    while(left<=right):
        while(left<=end and array[left]<=array[pivot]):
            left +=1
        while(right>start and array[right]>=array[pivot]):
            right -=1
        if(left>=right):
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array)-1)
print(array)
'''

# 방법 2 : 이게 더 쉬움
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if(len(array)<=1):
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))