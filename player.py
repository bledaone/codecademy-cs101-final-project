class Player:
  def __init__(self, name):
    self.name = name.title()
    self.introduce()
    
  def introduce(self):
    print("{}: Hello, my name is {}, nice to meet you".format(self.name, self.name))