import turtle
import random
import winsound

score=0
lives=3


#creating the window
wn=turtle.Screen()
wn.title("Hit Hit Hitler!")
wn.bgcolor("green")
wn.bgpic("war.gif")
wn.setup(width=800,height=600)
wn.tracer(0)


#register images used
wn.register_shape("hitler.gif")
wn.register_shape("bomb.gif")
wn.register_shape("flag.gif")




#adding general player
player = turtle.Turtle()
player.speed(0) #speed of turtle to draw things
player.shape("hitler.gif")
player.color("white")
player.penup() #doesnt let turtle draw a line while drawing or moving object
player.goto(0,-250)
player.direction = "stop" #initially, no direction.

#creating many good guys using lists
helpers = []
bombs=[]



#adding helper falling down
for _ in range(10):
	helper = turtle.Turtle()
	helper.speed(0) #speed of turtle to draw things
	helper.shape("flag.gif")
	helper.color("blue")
	helper.penup() #doesnt let turtle draw a line while drawing or moving object
	helper.goto(-100,250)
	helper.speed= random.uniform(0.5,1.5) #randomizing speed of helpers
	helpers.append(helper) #add all helpers in helpers list


#adding bombs falling down
for _ in range(10):
	bomb = turtle.Turtle()
	bomb.speed(0) #speed of turtle to draw things
	bomb.shape("bomb.gif")
	bomb.color("black")
	bomb.penup() #doesnt let turtle draw a line while drawing or moving object
	bomb.goto(100,250)
	bomb.speed= random.uniform(0.5,1.5) #randomizing speed of helpers
	bombs.append(bomb) #add all helpers in helpers list



#adding pen to display
pen= turtle.Turtle()
pen.hideturtle() #hides the pointer
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
font=("Courier",24,"normal")
pen.write("Score: {} Lives:{}".format(score,lives), align="center", font=font)






# function for moving hitler
def go_left():
	player.direction="left"
def go_right():
	player.direction="right"



#keyboard binding
wn.listen() #telling the window to listen
wn.onkeypress(go_left,"Left") #calls go_left when left arrow pressed
wn.onkeypress(go_right,"Right")






while True: #main loop


	#updating the screen
	wn.update()

	

	#move the player
	if player.direction == "left":
		x= player.xcor() #get current x
		x-=1 #change x coordination to move left
		player.setx(x) #set new value of x
	if player.direction == "right":
		x= player.xcor() #get current x
		x+=1 #change x coordination to move right
		player.setx(x) #set new value of x
	

	#moving the helpers
	for helper in helpers: #for all helper objects created
		y=helper.ycor()
		y-=helper.speed
		helper.sety(y)

		#if helper reaches bottom, go to top again
		if y<-300:
			#randomizing the fall
			x=random.randint(-380,380) #any x location
			y=random.randint(300,400) #y at top
			helper.goto(x,y)

		#collision with hitler
		if helper.distance(player) <45: #20 is height of the player(sq and circ)
			winsound.PlaySound("hitler.wav",winsound.SND_ASYNC)
			
			#in case of collision too, need new helper
			x=random.randint(-380,380) #any x location
			y=random.randint(300,400) #y at top
			helper.goto(x,y)
			score-=10
			lives -=1
			pen.clear()
			pen.write("Score: {} Lives:{}".format(score,lives), align="center", font=font)


	#moving the bombs
	for bomb in bombs: #for all helper objects created
		y=bomb.ycor()
		y-=bomb.speed
		bomb.sety(y)

		#if helper reaches bottom, go to top again
		if y<-300:
			#randomizing the fall
			x=random.randint(-380,380) #any x location
			y=random.randint(300,400) #y at top
			bomb.goto(x,y)

		#collision with hitler
		if bomb.distance(player) <45: #20 is height of the player(sq and circ)
			#in case of collision too, need new helper
			winsound.PlaySound("bomb.wav",winsound.SND_ASYNC)
			x=random.randint(-380,380) #any x location
			y=random.randint(300,400) #y at top
			bomb.goto(x,y)
			score+=10
			pen.clear()
			pen.write("Score: {} Lives:{}".format(score,lives), align="center", font=font)

		if(lives<=0):
			winsound.PlaySound("over.wav",winsound.SND_ASYNC)
			pen.clear()
			pen.goto(0,0)
			pen.color("light grey")
			pen.write("!!!!! Hitler Wins !!!!!", align="center", font=("Ariel", 40, "bold"))

			turtle.exitonclick()






wn.mainloop() #doesnt let the window close arbitrarily