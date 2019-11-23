import random
class Creature(object):
  """
  BASE CLASS 
  """
  def __init__(self,map=map, hp=0, mana=0, pos_x=0, pos_y=0, base_attack=5):
    self.hp = hp
    self.mana = mana
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.alive = True
    self.base_attack = base_attack
    self.map = map
    
  def die(self):
    print("{}: AAAA Umarlem".format(self.typ))
    self.alive = False
    map.mapp[self.pos_y-1][self.pos_x-1]= None
    

  def move(self, x, y):
    if map.mapp[self.pos_y+y-1][self.pos_x+x-1] == None:
      map.mapp[self.pos_y-1][self.pos_x-1]= None
      map.mapp[self.pos_y+y-1][self.pos_x+x-1]= self
      self.pos_x += x
      self.pos_y += y
    else:
      self.hit(map.mapp[self.pos_y+y-1][self.pos_x+x-1])
      if map.mapp[self.pos_y+y-1][self.pos_x+x-1] != None:
        print("Gra: Bijesz sie z {} i zostalo mu {} hp".format(map.mapp[self.pos_y+y-1][self.pos_x+x-1].typ,map.mapp[self.pos_y+y-1][self.pos_x+x-1].hp))
    
    
  def hit(self, target):
    target.hp -= self.base_attack
    self.try_to_kill(target)
  
  def try_to_kill(self, target):
    if target.hp<=0:
      target.die()
      print("Gra: Zabiles {}".format(target.typ))


class Map(object):
  def __init__(self, width=5, height=5):
    self.width = width
    self.height = height
    self.mapp = [[None for x in range(width)] for y in range(height)] 
    
  def display(self):
    for i in range(self.width):
      for j in range(self.height):
        if self.mapp[i][j] == None:
          print("[ ]", end='')
        else:
          if self.mapp[i][j].__class__.__name__ == "Player":
            print("[p]", end='')
          else:
            print("[x]", end='')
      print("")
        
    
class Orki(Creature):
  def __init__(self, map, pos_x, pos_y, hp=20,typ="Ork"):
    Creature.__init__(self)
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.hp = hp
    self.map = map
    self.typ = typ
    map.mapp[self.pos_y-1][self.pos_x-1]= self

class Player(Creature):
  def __init__(self, map, pos_x, pos_y, hp=69,typ="Gracz"):
    Creature.__init__(self)
    self.map = map
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.hp = hp
    self.typ = typ
    map.mapp[self.pos_y-1][self.pos_x-1]= self
    
    
    
def bruszanie():
  if rand == 1:
    if b.pos_y-1>0:
      b.move(0,-1)
    else:
        b.pos_y+1<len(map.mapp)+1
        b.move(0,1)
        
  elif rand== 2:
    if b.pos_y+1<len(map.mapp)+1:
      b.move(0,1)
    else:
       b.move(0,-1)
      
  elif rand == 3:
    if b.pos_x-1>0:
      b.move(-1,0)
    else:
      b.move(1,0)
      
  elif  rand== 4:
    if b.pos_x+1<len(map.mapp)+1:
      b.move(1,0)
    else:
      b.move(-1,0)
      

def cruszanie():
  if rand == 1:
    if c.pos_y-1>0:
      c.move(0,-1)
    else:
        c.pos_y+1<len(map.mapp)+1
        c.move(0,1)
        
  elif rand== 2:
    if c.pos_y+1<len(map.mapp)+1:
      c.move(0,1)
    else:
       c.move(0,-1)
      
  elif rand == 3:
    if c.pos_x-1>0:
      c.move(-1,0)
    else:
     c.move(1,0)
      
  elif  rand== 4:
    if c.pos_x+1<len(map.mapp)+1:
      c.move(1,0)
    else:
      c.move(-1,0)   
      
def druszanie():
  if rand == 1:
    if d.pos_y-1>0:
      d.move(0,-1)
    else:
        d.pos_y+1<len(map.mapp)+1
        d.move(0,1)
        
  elif rand== 2:
    if d.pos_y+1<len(map.mapp)+1:
      d.move(0,1)
    else:
       d.move(0,-1)
      
  elif rand == 3:
    if d.pos_x-1>0:
      d.move(-1,0)
    else:
     d.move(1,0)
      
  elif  rand== 4:
    if d.pos_x+1<len(map.mapp)+1:
      d.move(1,0)
    else:
      d.move(-1,0)

def randoming():
  licz = random.randint(1, 5)
  return licz
    
def randoming2():
  baa = random.randint(1, 5)
  return baa


map = Map()
a = Player(map,randoming(), randoming2())
b = Orki(map,randoming(),randoming2())
c = Orki(map,randoming(),randoming2())
d = Orki(map,randoming(),randoming2())

while True:
  if b.hp==0:
      liczbaa = random.randint(1, 5)
      aabzcil = random.randint(1, 5)
      b = Orki(map,liczbaa,aabzcil)
  if c.hp==0:
      liczbaa = random.randint(1, 5)
      aabzcil = random.randint(1, 5)
      c = Orki(map,liczbaa,aabzcil)
  if d.hp==0:
      liczbaa = random.randint(1, 5)
      aabzcil = random.randint(1, 5)
      d = Orki(map,liczbaa,aabzcil)
  if b.hp>0:
    rand = random.randint(1,4)
    bruszanie()
  if c.hp>0:
    rand = random.randint(1,4)
    cruszanie()
  if d.hp>0:
    rand = random.randint(1,4)
    druszanie()


  map.display()
  n = input("Gra: Co chcesz zrobic?")
  if n == "up":
    if a.pos_y-1>0:
      a.move(0,-1)
    else:
      print("Gra: Nie mozesz sie tam ruszyc")
  elif n == "down":
    if a.pos_y+1<len(map.mapp)+1:
      a.move(0,1)
    else:
      print("Gra: Nie mozesz sie tam ruszyc")
  elif n == "left":
    if a.pos_x-1>0:
      a.move(-1,0)
    else:
      print("Gra: Nie mozesz sie tam ruszyc")
  elif n == "right":
    if a.pos_x+1<len(map.mapp)+1:
      a.move(1,0)
    else:
      print("Gra: Nie mozesz sie tam ruszyc")
  else:
    print("Gra: nie wiem o co chodzi???")
  






