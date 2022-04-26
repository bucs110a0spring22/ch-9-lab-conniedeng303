from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    self.image = str(filename)
    self.rect = Rectangle(x,y,h,w)
    
  def rect(self,x,y,h,w):
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    
  def getRect(self):
    return self.rect