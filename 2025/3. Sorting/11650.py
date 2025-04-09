'''
11650번
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.


첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

##########################YOUR CODE##################################

''' 
2중 리스트로 받은 다음에 소팅하는 방법을 쓰면 안되나?
'''

num = int(input())


input_total = []
for i in range(num):
    add = list(map(int, input().split()))
    input_total.append(add)

##################### 입력귀찮아서 테스트용 ###########################
# input_total = [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]
# print(input_total)
# print(len(input_total))

### KEY_LINE ###
input_total.sort(key = lambda x:(x[0], x[1])) 
### KEY_LINE ###


for i in range(len(input_total)):
    print(input_total[i][0],input_total[i][1])

