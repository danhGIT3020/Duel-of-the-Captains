class Player:
  def __init__(self, action):
    self.action = action
    self.loaded = True
    self.bowsprit = True
    self.health = 100
    
  def turn(self):
    if self.action == "1" and self.loaded == True:
      print("You fired your cannons. Fire in the hole!!!")
      self.loaded = False
    elif self.action == "2":
      print("You reloaded your cannons.")
      self.loaded = True
    if self.action == "3" and self.bowsprit == True:
      print("You evaded the enemy's move")
    if self.action == "4" and self.bowsprit == True:
      print("You charged the enemy ship!")
    if self.action == "5":
      print("You escaped the enemy")
      
