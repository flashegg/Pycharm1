import random

all_choice = ['石头','剪刀','布']
win_list = ['石头','剪刀'],['剪刀','布'],['布','石头']

#进行用户提示
prompt = """(0)石头
(1)剪刀
(2)布
请选择(0/1/2):"""

nwin = 0
pwin = 0

while nwin <2 and pwin <2:
    index = int(input(prompt))

    while index >=3:
        index = int(input(prompt))
player = all_choice[index]

NPC = random.choice(all_choice)

print("player:%s,NPC:%s" %(player,NPC))


if player == NPC:
    print ("\033[32;43;1m平局\033[0m")
elif [player,NPC] in win_list:
    print ("\033[31;43;1m你赢了\033[0m")
else:
    print ("\033[31;43;1m你输了\033[0m")

if pwin == 2:
    print("win")
else:
    print("lose")


