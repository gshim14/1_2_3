import turtle as trtl
import random
#   a123_apple_1.py

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape('pear.gif')
wn.addshape(apple_image) # Make the screen aware of the new file
pear = trtl.Turtle()
apple = trtl.Turtle()
wn.bgpic('background.gif')
drawer = trtl.Turtle()
drawer.ht()
apple.shape(apple_image)
intspawn = random.randint(1,10)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_pear(active_pear):
  active_pear.ht()
  active_pear.shape('pear.gif')
  wn.update()

def drawletter(letter):
  drawer.color('white')
  drawer.pu()
  drawer.goto(apple.xcor()-10,apple.ycor()-30)
  drawer.pd()
  drawer.write(letter, font=("Arial", 30, "bold"))
  
def applespawn(active_apple, x):
  apple.pu()
  active_apple.shape(apple_image)
  apple.ht()
  print('hi')
  xcors = []
  ycors=[]
  x1 = random.randint(-150,150)
  y1= random.randint(0,100)
  apple.st()
  active_apple.clone().goto(x1,y1)
  apple.ht()
  xcors.append(x1)
  ycors.append(y1)
  print(x1)
  print(y1)
  for i in range(x):
      TrueCon = False
      TrueCony = False
      print(i)
      x1 = random.randint(-150,150)
      y1= random.randint(0,100) 
      for xvalues in xcors:
        print( xcors)
        print('x1: ' + str(x1))
        print('Xvalues: '+ str(xvalues))
        if xvalues-50<x1<xvalues+50 or x1==xvalues:
          print('hi')
          TrueCon = True
          break
      if TrueCon == False:
        print(x1)
        xcors.append(x1)


      for yvalues in ycors:
        print(ycors)
        print('y1: ' + str(y1))
        print('yvalues: '+ str(yvalues))
        if yvalues-10<y1<yvalues+10 or y1==yvalues:
          print('hi')
          TrueCony = True
          break
      if TrueCony == False:
        print(y1)
        ycors.append(y1)


  print(xcors)
  print(ycors)
  xcors.pop(0)
  ycors.pop(0)
  for i in range(len(xcors)):
    try:
      active_apple.st()
      clonea = active_apple.clone()
      clonea.goto(xcors[i], ycors[i])
      print(str(clonea.xcor()) + ',' + str(clonea.ycor()))
      active_apple.ht()
    except IndexError:
      continue



      
    



#-----function calls-----
draw_pear(pear)
drawletter('a')
wn.onkeypress(applespawn, 'a')
wn.listen()
wn.mainloop()
