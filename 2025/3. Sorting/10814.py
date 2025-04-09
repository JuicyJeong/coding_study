'''
10814번
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 
입력은 가입한 순서로 주어진다.

첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.


'''

##########################YOUR CODE##################################

''' 
저장을 어떤 식으로 할지부터 고민해보자
나이순으로 선 정렬 후에 나이 같으면 입력 순서로...
그러면 판정 요소는 1티어 나이, 2티어, 입력순서(이거도 변수로 입력해야할듯?)
리스트로 구성은?[[입력 순서, 나이, 이름], [입력 순서, 나이, 이름], [입력 순서, 나이, 이름], ...]

1차로 돌때, 나이순으로 먼저 입력


'''

num = int(input())
input_total = []
for i in range(num):
    indexNum = i
    age_name = input().split()
    age_name[0] = int(age_name[0])
    age_name.append(indexNum)
    input_total.append(age_name)

# print(input_total)
input_total.sort()
# print(input_total)
input_total.sort(key = lambda x:(x[0], x[2]))
# print(input_total)
for i in range(len(input_total)):
    print(input_total[i][0],input_total[i][1])
