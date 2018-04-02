class Role:
	def __init__(self):
		self.hp=0
		self.defence=0
		self.attack=0
	def getHp(self):
		return self.hp
	def getAttack(self):
		return self.attack
	def getDefence(self):
		return self.defence
	def attacking(self,defence):
		return  (self.attack*0.8+0.2*self.hp)/(1+0.3*defence)
		
	def __str__(self):
		return "hp:%d attack:%d defence:%d"%(self.hp,self.attack,self.defence)
		
class Dragon(Role):
	def __init__(self):
		self.hp=200
		self.defence=35
		self.attack=40
	def setHp(self,newHp):
		self.hp=newHp
	def setAttack(self):	
		pass
	def setDefence(self):
		pass
class Player(Role):
	def __init__(self):
		self.hp=80
		self.defence=10
		self.attack=15
	def setHp(self,newHp):
		self.hp=newHp
	def setAttack(self,deltaAttack):	
		self.attack=self.attack+deltaAttack
	def setDefence(self,deltaDefence):
		self.defence=self.defence+deltaDefence
class Beaset(Role):
	def __init__():
		self.hp=50
		self.defence=12
		self.attack=8
	def setHp(self,newHp):
		self.hp=newHp
	def setAttack(self):	
		pass
	def setDefence(self):
		pass
	
		
		
		
		
		
		
		
		
		
		
		