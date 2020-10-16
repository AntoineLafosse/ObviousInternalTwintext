import turtle as trtl 
for i in range (6):
  trtl.forward(10)
  trtl.left(15)
trtl.penup()

trtl.pendown()
def draw_axis ():
  trtl.penup()
  trtl.goto(0,0)
  trtl.pendown()
  trtl.forward(100)
  trtl.backward(200)
  trtl.forward(100)
  trtl.left(90)
  trtl.forward(100)
  trtl.backward(200)
draw_axis()
