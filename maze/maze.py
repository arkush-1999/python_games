import turtle
import os
import math
import random
import winsound
#screen 600 600
#each box 24 24
#grid 25 25
#top left block -288,288 tr++ bottom left-- bottom right +-




#creating window
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Virushka-the search of love")
wn.setup(700,700)
wn.tracer(0)


#registering shapes
turtle.register_shape("virat.gif")
turtle.register_shape("anushka.gif")
turtle.register_shape("villian.gif")

turtle.register_shape("maze.gif")

#creating pen
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self) #initialize turtle module
		self.shape("maze.gif")
		self.color("white")
		self.penup() #no trail
		self.speed(0) #animation speed
		



pen1= turtle.Turtle()
#creating player class
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("virat.gif")
		self.color("blue")
		self.penup()
		self.speed(0)
		self.lives=3
		
		pen1.hideturtle() #hides the pointer
		pen1.speed(0)
		pen1.shape("square")
		pen1.color("white")
		pen1.penup()
		pen1.goto(0,300)
		font=("Courier",24,"bold")
		pen1.write("Lives:{}".format(self.lives), align="center", font=font)
		
		
	def go_up(self):
		#check where will we move if pressed up
		#if that isnt in our walls coord list, can move there
		move_to_x = player.xcor()
		move_to_y = player.ycor() + 24

		if(move_to_x,move_to_y) not in walls:
			winsound.PlaySound("walk.wav",winsound.SND_ASYNC)
			self.goto(move_to_x,move_to_y)

	def go_down(self):
		move_to_x = player.xcor()
		move_to_y = player.ycor() - 24

		if(move_to_x,move_to_y) not in walls:
			winsound.PlaySound("walk.wav",winsound.SND_ASYNC)
			self.goto(move_to_x,move_to_y)

	def go_left(self):
		move_to_x = player.xcor()-24
		move_to_y = player.ycor() 

		if(move_to_x,move_to_y) not in walls:
			winsound.PlaySound("walk.wav",winsound.SND_ASYNC)
			self.goto(move_to_x,move_to_y)

	def go_right(self):
		move_to_x = player.xcor() +24
		move_to_y = player.ycor() 

		if(move_to_x,move_to_y) not in walls:
			winsound.PlaySound("walk.wav",winsound.SND_ASYNC)
			self.goto(move_to_x,move_to_y)

	def is_collision(self,other):
		a=self.xcor()-other.xcor()
		b=self.ycor()-other.ycor()
		distance = math.sqrt((a**2)+(b**2)) #distance between self and other(demon) usinf pyth thn

		if distance<20: #return collision value
			winsound.PlaySound("collision.wav",winsound.SND_ASYNC)
			self.lives-=1
			return True
		else:
			return False


class Treasure(turtle.Turtle):   #anushka is the treasure
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("anushka.gif")
		self.color("gold")
		self.penup()
		self.speed(0)
		
	
'''class Demon(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.shape("villian.gif")
		self.color("red")
		self.penup()
		self.speed(0)
		self.goto(x,y)
		self.dx=0.9'''

class Enemy(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.shape("villian.gif")
		self.penup()
		self.speed(0)
		self.goto(x,y)
		#villian can go randomly
		self.direction = random.choice(["up","down","left","right"])

	def move(self):
		if self.direction == "up":
			dx=0
			dy=24
		elif self.direction == "down":
			dx=0
			dy=-24
	
		elif self.direction == "left":
			dx=-24
			dy=0
	
		elif self.direction == "right":
			dx=24
			dy=0
		else:
			dx=0
			dy=0

		#check if player is close
		#if so, go in that direction
		if self.is_close(player):
			if player.xcor()<self.xcor():
				self.direction="left"
			elif player.xcor()>self.xcor():
				self.direction="right"
			elif player.ycor()<self.ycor():
				self.direction="down"
			elif player.ycor()<self.ycor():
				self.direction="up"
		

		#where to move?
		move_to_x=self.xcor()+dx
		move_to_y=self.ycor()+dy
		#check wall
		if(move_to_x,move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)
		else:
			#choose a diff direction
			self.direction = random.choice(["up","down","left","right"])

		#timer to move next time
		turtle.ontimer(self.move,t=random.randint(100,300))

	def is_close(self,other): #check if player iss close based upon comparision of distance
		a=self.xcor()-other.xcor()
		b=self.ycor()-other.ycor()
		distance= math.sqrt((a**2)+(b**2))

		if distance<75:
			return True
		else:
			return False





#creating levels
levels = [""] #making different levels


#first level
level_1=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXX         XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X    D  XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X       XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                 XXXXXXX",
"XXXXXXXXXXXX  D  XXXX  XX",
"XXXXXXXXXXXXXX   XXXX  XX",
"XXX  XXXXXXXXXX         X",
"XXX         D           X",
"XXX          XXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX  D           X",
"X A     XX              X",
"X  D    XXXXXXXXXX  XXXXX",
"X       XXXXXXXXXX  XXXXX",
"X     D      XX  X     XX",
"XXXXXXX                 X", 
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]


#add a demon list for multiple demons
#demons=[]
enemies=[]


#add these mazes to list
levels.append(level_1)


#function to setup maze
#rows are y
#cols are x

def setup_maze(level):
	for y in range(len(level)): #0 to 24\
		for x in range(len(level[y])): #basically a 2d matrix
			#get the character at each x,y
			#note the order of y and x in each line
			character = level[y][x]
			#calculate x and y on screen
			screen_x = -288 + (x*24) #24 is the sixe of the square adding 24 as we move ahead. x tells which column youre in
			screen_y = 288 - (y*24)

			#if wall is encountered
			if character == 'X':
				pen.goto(screen_x,screen_y)
				pen.stamp()  #stamps a square wherever there is X

				#appending wall coords to wall list
				walls.append((screen_x,screen_y))
			#if player is encountered
			if character == "P":
				player.goto(screen_x,screen_y)

			if character=="A":
				treasure.goto(screen_x,screen_y)

			if character == "D":
				enemies.append(Enemy(screen_x,screen_y))

			

			




#create class instance of pen
pen=Pen()
player = Player()
treasure= Treasure()




#to stop collision of virat and wall, we first create a wall list
#then we append all x and y coords of all walls into this list
walls=[]



#setting up maze. calling up the function.
setup_maze(levels[1]) #levels is our list...levels[1] indicate first object of the list, that we appended after creating above
# print (walls)
#returns all walls coords


#keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")


#close windows close arbitrarily
wn.tracer(0)

#start moving enemies
for enemy in enemies:
	turtle.ontimer(enemy.move,t=250)


#main game loop
while True:
	
	if(player.lives==0):
		winsound.PlaySound("over.wav",winsound.SND_ASYNC)
		pen1.clear()
		pen1.goto(0,0)
		pen1.color("light grey")
		pen1.write("!!!!! Virat lost !!!!!", align="center", font=("Ariel", 40, "bold"))
		turtle.exitonclick()



	if((player.xcor()==treasure.xcor()) and (player.ycor()==treasure.ycor())):
		winsound.PlaySound("win.wav",winsound.SND_ASYNC)
		pen.goto(0,0)
		pen.clear()
		pen.clear()
		pen.color("white")
		font=("Courier",24,"bold")
		pen.write("Virushka Forever!", align="center", font=font)
		turtle.exitonclick()

	#checking for collision
	
	for enemy in enemies:
		if player.is_collision(enemy):
			font=("Courier",24,"bold")
			pen1.clear()
			pen1.write("Lives:{}".format(player.lives), align="center", font=font)

			player.goto(-288+24,288-24)
			
	'''for demon in demons:
		
		demon.setx(demon.xcor()+demon.dx)
		if (demon.xcor()>-150+24 or demon.xcor()<-288+24) and (demon.xcor()>264 or demon.xcor()<=-288+264):
			demon.dx *=-1

		if player.is_collision(demon):
			player.lives-=1
			player.goto(-288+24,288-24)'''
	wn.update()
		

	


	



wn.mainloop()
