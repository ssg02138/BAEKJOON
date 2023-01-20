# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

import sys

total_cnt = int(input())

if not ((total_cnt >= 1) and (total_cnt <= 100)):
	print('total_cnt Exception')

input_data = input()

if total_cnt != len(input_data):
	print('total_cnt not equal int_list count')

data = list(map(int, list(input_data)))

result = 0
for d in data:
	result += d

print(result)