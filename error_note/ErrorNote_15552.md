## 15552번

### 문제

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

### 입력

첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

### 출력

각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

### 내가 작성한 코드

```python
import sys

case_num = sys.stdin.readline().rstrip()
for i in range(0,case_num):
    a,b = sys.stdin.readline().rstrip().split(" ")
    print(a+b)
```

### 수정 사항 및 놓친 부분

- 입력 값을 int 값으로 받아야하는거 까먹지 말기
- 입력 받을 때 split()에서 굳이 구분자를 넣지 않아도 잘 구분하니깐 비워두기?
- 두개 이상을 받을 때에는 map 함수 활용하기

### 변경된 코드 혹은 정답

```python
import sys

case_num = int(sys.stdin.readline().rstrip())
for i in range(0,case_num):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
    
```