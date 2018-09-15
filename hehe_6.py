#导入random模块
import random

#定义两个列表，A表示NPC的随机选择，win_list表示赢的情况
A = ['石头','剪刀','布']
win_list = ['石头','剪刀'],['剪刀','布'],['布','石头']

#进行用户提示
prompt = """(0)石头
(1)剪刀
(2)布
请选择(0/1/2):"""

nwin = 0
pwin = 0

while nwin < 2 and pwin < 2:
	index = int(input(prompt))
	while index >= 3:
		index = int(input(prompt))

	player = A[index]
	NPC = random.choice(A)
	print("player:%s,NPC:%s" %(player,NPC))
	if player == NPC:
		pass
	elif [player,NPC] in win_list:
		pwin += 1
	else:
		nwin += 1

if pwin == 2:
	print("win")
else:
	print("lose")