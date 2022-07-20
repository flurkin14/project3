import turtle
shape =input("what shape  ")
length=input("what length  ")
color=input("what color  ")

bob=turtle.Turtle()



def circle(length, color):
  bob.fillcolor(color) 
  bob.begin_fill()
  bob.circle(int(length))
  bob.end_fill()

def square(length, color):
  print("making square")
  sides=0
  bob.fillcolor(color) 
  bob.begin_fill()
  
  while (sides<4):
    bob.forward (int(length))
    bob.right(90)
    sides+=1
    
  bob.end_fill()
def triangle(length, color):
  print("making triangle")
  tsides=0
  bob.fillcolor(color) 
  bob.begin_fill()

  
  while (tsides<3):
    bob.forward(int(length))
    bob.right(120)
    tsides+=1

  bob.end_fill()

if (shape=="triangle"):
  triangle(length, color)

elif (shape=="circle"):
  circle(length, color)
  
elif (shape=="square"):
  square(length, color)





