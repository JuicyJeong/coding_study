import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값 찾은 경우 인덱스 반환
        if array[mid] == target:
            return mid
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
        elif array[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            start = mid + 1

    return None

N = int(sys.stdin.readline())
given_cards = list(map(int, sys.stdin.readline().split()))
given_cards.sort()

M = int(sys.stdin.readline())
task_cards = list(map(int, sys.stdin.readline().split()))
# task_cards.sort()

answer = []
for i in range(len(task_cards)):


    
    result = binary_search(given_cards, task_cards[i], 0, N - 1)
    if result is None:
        answer.append(0)
    else:
        answer.append(1)

print(*answer)
