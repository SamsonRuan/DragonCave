import time
import random
import fight
import npc
player=npc.Player()
dragon=npc.Dragon()
'''
作者:SamsonRuan
时间：2018-3-31
描述：这是控制整个游戏流程的顶层文件，主要进行故事情节的描述
'''
def main():
	caveEnter=story()
	dragonAppear(caveEnter)
	
def story():
	f=open("story.txt",'r')
	story1=f.readlines()
	for i in story1:
		print(i)
		time.sleep(2)
	caveEnter=int(input("你想进入哪个洞穴？(1/2)"))
	print("\n")
	return caveEnter
		
	#print(story1)
def fightCall(player,gameRole):		
	fight.fighting(player,gameRole)	
def dragonAppear(caveEnter):
	if random.randint(0,1)==0:
		print("你进入了第%d个洞穴..."%caveEnter,end='\n\n')
		time.sleep(2)
		print("里面看起来又阴暗又潮湿...",end='\n\n')
		time.sleep(2)
		print("突然，一条巨龙展现在你眼前，像山一样大，像夜一样黑...",end='\n\n')
		time.sleep(2)
		print("它张开了大口，喷出火焰，向你发起了猛烈的进攻...",end='\n\n')
		time.sleep(2)
		fight.fighting(player,dragon)
	else:
		print("你进入了第%d个洞穴..."%caveEnter,end='\n\n')
		time.sleep(2)
		print("里面看起来又阴暗又潮湿...",end='\n\n')
		time.sleep(2)
		print("突然，一条巨龙展现在你眼前，像山一样大，像夜一样黑...",end='\n\n')
		time.sleep(2)
		print("它张开了口，吐出一把宝剑和盾牌，让你去杀死恶龙...",end='\n\n')
		time.sleep(2)
		player.setAttack(10)
		player.setDefence(15)
		print("于是，你来到了居住着邪恶巨龙的洞穴,洞口中有气流逸出，散发出浑浊的恶臭，深不见底的洞穴中时断时续地传来阵阵哀嚎...",end='\n\n')
		time.sleep(2)
		if input("真的要进去吗？(y/n)").lower().startswith("y"):
			print('\n')
			print("你进入了居住着恶龙的洞穴中，找到了巨龙，展开了激烈的战斗...",end='\n')
			time.sleep(2)
			fightCall(player,dragon)
		else:
			print('\n')
			print("你刚往里走了几步，就觉得实在是有点慌，打了个寒颤，不由自主地退了出来...")
			time.sleep(2)
			print("你觉得，没有必要因为一时冲动而丢掉了小命...")
			time.sleep(2)
			print("还是先打几个小怪提升一下level比较好...")
		
main()
