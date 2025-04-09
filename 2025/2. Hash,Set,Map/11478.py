'''
https://www.acmicpc.net/problem/11478
서로 다른 부분 문자열의 개수

문제
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.
부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.
예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

출력
첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.
'''
S = input()
num = []

# 1 ~ S까지의 길이를 다 돌려야함
for i in range(1, len(S)+1):
    # print(f'{i}번째 길이')
    num.append(S[0:i])

    up_count = 1
    while i+up_count<len(S)+1:
        num.append(S[up_count:i+up_count])
        up_count+=1
# print(*num)
ans = set(num)
print(len(ans))