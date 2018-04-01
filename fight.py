

def fighting(player,dragon):
	while player.hp>0 and dragon.hp>0:
		damage1=player.attacking(dragon.getDefence())
		dragon.setHp(dragon.getHp()-damage1)
		print("Dragon:"+str(dragon))
		damage2=dragon.attacking(player.getDefence())
		player.setHp(player.getHp()-damage2)
		print("Player:"+str(player))
	if player.hp>0:
		print("you win")
	else:
		print("you lose")
	
	print(player.getHp())
