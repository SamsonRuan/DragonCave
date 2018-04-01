import time
import random
import fight
import  npc
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
		#time.sleep(2)
	caveEnter=int(input("你想进入哪个洞穴？(1/2)"))
	return caveEnter
		
	#print(story1)
def dragonAppear(caveEnter):
	if random.randint(0,1)==0:
		print("你进入了第%d个洞穴..."%caveEnter)
		print("里面看起来又阴暗又潮湿...")
		print("突然，一条巨龙展现在你眼前，像山一样大，像夜一样黑...")
		print("它张开了大口，喷出火焰，向你发起了猛烈的进攻...")
		fight.fighting(player,dragon)
	else:
		print("你进入了第%d个洞穴..."%caveEnter)
		print("里面看起来又阴暗又潮湿...")
		print("突然，一条巨龙展现在你眼前，像山一样大，像夜一样黑...")
		print("它张开了口，吐出一把宝剑和盾牌，让你去杀死恶龙...")
		fight.fighting(player,dragon)
main()
