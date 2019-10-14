import turtle as trtl
import random
turtle = trtl.Turtle()

# create turtle body and set color
turtle = trtl.Turtle("turtle")
turtle.turtlesize(25)
turtle.fillcolor("green")
turtle.setheading(90)

# create turtle 2
shell = trtl.Turtle()

# create turtle shell and set color
shell.penup()
shell.goto(0,-165)
shell.pendown()
shell.pencolor("saddlebrown")
shell.fillcolor("saddlebrown")
shell.begin_fill()
shell.circle(200)
shell.end_fill()
shell.hideturtle()

# create turtle 3
pattern = trtl.Turtle()

# create shell pattern
pattern.penup()
pattern.goto(0, -70)
pattern.pendown()
pattern.pensize(3)
pattern.circle(100, 360, 6)
pattern.setheading(270)
pattern.forward(95)
pattern.penup()
pattern.goto(0,130)
pattern.pendown()
pattern.setheading(90)
pattern.forward(105)

pattern.hideturtle()

# create turtle 4
eyes = trtl.Turtle()

# create list of colors for eyes
colorList = ["rosybrown", "lightcoral", "indianred", "firebrick", "maroon", "tomato", "orangered", "red", "darkred", "blue", "crimson"]
randNum = random.randint(0, 10)

color = colorList[randNum]

# move turtle to head
eyes.penup()
eyes.goto(-20,325)
eyes.pendown()

# create turtle eyes
v=1
while (v>0):
    randNum = random.randint(0, 10)
    color = colorList[randNum]
    eyes.fillcolor(color)
    eyes.begin_fill()
    eyes.circle(10)
    eyes.end_fill()
    if (v%2==0):
        eyes.penup()
        eyes.goto(20,325)
        eyes.pendown()
    if (v%2!=0):
        eyes.penup()
        eyes.goto(-20,325)
        eyes.pendown()
    v+=1

wn = trtl.Screen()
wn.mainloop()
# circle(r, e, s)



