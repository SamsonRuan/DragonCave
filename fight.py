import time
def fighting(player,dragon):
	while player.getHp()>0 and dragon.getHp()>0:
		damage1=player.attacking(dragon.getDefence())
		print("你一剑刺向巨龙，巨龙仿佛感觉是在搔痒...,你一共对巨龙造成了%d点伤害..."%damage1)
		time.sleep(2)
		dragon.setHp(dragon.getHp()-damage1)
		print("Dragon:"+str(dragon))
		damage2=dragon.attacking(player.getDefence())
		print("巨龙反身就是一翅膀,你就像三两重的棉花一样飞了出去，你一共收到了%d点伤害..."%damage2)
		time.sleep(2)
		player.setHp(player.getHp()-damage2)
		print("Player:"+str(player))
	if player.hp>0:
		print("虽然被打得鼻青脸肿，但最终还是打趴了巨龙，你感到了一阵蜜汁骄傲涌上心头...")
		time.sleep(2)
	else:
		print("巨龙把你打得抱头鼠窜，你连裤子都来不及提，就落荒而逃...")
		time.sleep(2)
	
