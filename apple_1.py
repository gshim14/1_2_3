#   a123_apple_1.py
import turtle

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = turtle.Turtle()
drawer = turtle.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_an_A()
  
def drop_apple():
  apple.up()
  drawer.hideturtle()
  drawer.clear()
  apple.goto(0,-160)
  apple.down()

def draw_an_A():
  drawer.up()
  drawer.goto(-25,-33)
  drawer.down()
  drawer.color("white")
  drawer.write("A", font=("Arial", 40, "bold")) 

#-----function calls-----

draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.mainloop()

