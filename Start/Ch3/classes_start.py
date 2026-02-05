# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#
print('='*15)

# Creating Classes
class Cars:
  def __init__(self, style):
    self.style = style

  def drive(self, speed):
    self.mode = 'driving'
    self.speed = speed

class Sedan(Cars):
  def __init__(self, engine):
    super().__init__('Sedan')
    self.wheels = 4
    self.doors = 4
    self.engine = engine

class Sports(Cars):
  def __init__(self, engine, isconvertible):
    super().__init__("Sports")
    if (isconvertible):
      self.doors = 2
    else:
      self.doors = 4 or 2

    self.wheels = 4
    self.engine = engine

  def drive(self, speed):
    super().drive(speed)
    print('Driving my', self.engine, 'sports car at', self.speed, 'mph.')

# Creating objects
car1 = Sedan('electric')
car2 = Sports('jet fuel', False)
car3 = Sports('gas', True)

print(car2.engine)
print(car1.doors)
print(car1.engine)
car1.drive(30)
car2.drive(100)