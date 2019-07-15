def seq(str):
  str = str[1:-1]
  operate_str, num = input().split('(')
  num = int(num)
  print(operate_str, num)

def operate_calc(str):
  operate_list = []
  return [[1, 1]]

n = int(input())

board = []
operate = []  # [dx, dy]

for i in range(n):
  board.append(list(input()))

operate_str = str(input())

operate = operate_calc(operate_str)
print(seq("(UDR)3"))