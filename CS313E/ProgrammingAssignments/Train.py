#  File: Train.py

#  Description: Draws a train

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2 / 12 / 2018

#  Date Last Modified: 2 / 14 / 2018

import turtle
import math

def draw_spokes(out_radius):
  circumference = 2 * math.pi * out_radius
  interval = circumference / 24
  turtle.pendown()
  turtle.circle(out_radius, 7.5)

  for i in range(0, 4):
    turtle.left(90)
    turtle.forward(out_radius * 2)
    turtle.left(90)
    turtle.circle(out_radius, 15)
    turtle.left(90)
    turtle.forward(out_radius * 2)
    turtle.left(90)
    turtle.circle(out_radius, 30)

def main():
  # Set up window
  turtle.setup(800, 800, 0, 0)
  turtle.title("I wanted Ozzy's 'Crazy Train' to play over this because" +
    " this thing would derail horribly if it ever managed to move.")
  turtle.speed(1)
  turtle.pensize(2)

  # Draw tracks
  turtle.penup()
  turtle.goto(-400, -300)
  turtle.pendown()
  turtle.goto(400, -300)
  turtle.penup()
  turtle.goto(400, -305)
  turtle.pendown()
  turtle.goto(-400, -305)

  # Draw sleepers
  x = -388
  for i in range(16):
    turtle.penup()
    turtle.goto(x, -305)
    turtle.pendown()
    turtle.goto(x, -310)
    turtle.goto(x + 25, -310)
    turtle.goto(x + 25, -305)
    x += 50

  # Draw car body
  turtle.color("blue")
  turtle.penup()
  turtle.goto(-350, -200)
  turtle.pendown()
  turtle.goto(-350, 200)
  turtle.goto(-75, 200)
  turtle.goto(-75, 220)
  turtle.goto(-375, 220)
  turtle.goto(-375, 200)
  turtle.goto(-375, 200)
  turtle.goto(-100, 200)
  turtle.goto(-100, -200)
  turtle.goto(-100, 100)
  turtle.goto(300, 100)
  turtle.goto(300, -200)
  turtle.goto(275, -200)
  turtle.penup()
  turtle.goto(175, -200)
  turtle.pendown()
  turtle.goto(75, -200)
  turtle.penup()
  turtle.goto(-25, -200)
  turtle.pendown()
  turtle.goto(-125, -200)
  turtle.penup()
  turtle.goto(-325, -200)
  turtle.pendown()
  turtle.goto(-350, -200)

  # Draw whistle
  turtle.penup()
  turtle.goto(-25, 100)
  turtle.pendown()
  turtle.goto(-25, 120)
  turtle.goto(25, 120)
  turtle.goto(25, 130)
  turtle.goto(0, 130)
  turtle.goto(0, 120)
  turtle.goto(50, 120)
  turtle.goto(50, 100)

  # Draw chimney
  turtle.penup()
  turtle.goto(125, 100)
  turtle.pendown()
  turtle.goto(100, 175)
  turtle.goto(112, 200)
  turtle.goto(188, 200)
  turtle.goto(200, 175)
  turtle.goto(100, 175)
  turtle.goto(200, 175)
  turtle.goto(175, 100)

  # Draw cylinder at front of train
  turtle.penup()
  turtle.goto(300, 50)
  turtle.pendown()
  turtle.goto(325, 50)
  turtle.goto(325, -50)
  turtle.goto(335, -50)
  turtle.goto(335, 0)
  turtle.goto(325, 0)
  turtle.goto(325, -100)
  turtle.goto(300, -100)

  # Draw cowcatcher
  turtle.goto(300, -175)
  turtle.goto(310, -175)
  turtle.goto(375, -275)
  turtle.goto(300, -275)
  turtle.goto(300, -175)

  # Draw decorations on car
  turtle.penup()
  turtle.goto(-100, -40)
  turtle.pendown()
  turtle.goto(300, -40)
  turtle.goto(300, -50)
  turtle.goto(-100, -50)
  turtle.penup()
  turtle.goto(-10, 100)
  turtle.pendown()
  turtle.goto(-10, -40)
  turtle.goto(0, -40)
  turtle.goto(0, 100)
  turtle.goto(200, 100)
  turtle.goto(200, -40)
  turtle.goto(210, -40)
  turtle.goto(210, 100)

  # Draw horizontal rivets
  x = -97
  turtle.penup()
  for i in range(50):
    turtle.goto(x, -45)
    turtle.dot(5, "black")
    x += 8

  # Draw vertical rivets
  for x in [-5, 205]:
    y = 95
    for i in range(17):
      turtle.goto(x, y)
      turtle.dot(5, "black")
      y -= 8
  
  # Draw windows
  turtle.fillcolor("grey")
  for x in [-317, -208]:
    turtle.goto(x, 150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x + 75, 150)
    turtle.goto(x + 75, 25)
    turtle.goto(x, 25)
    turtle.goto(x, 150)
    turtle.end_fill()
    turtle.penup()
  
  # Draw arches above wheels
  # Arch 1
  turtle.goto(-125, -200)
  turtle.left(90)
  turtle.pendown()
  turtle.circle(100, 180)

  # Arch 2
  turtle.penup()
  turtle.goto(75, -200)
  turtle.left(180)
  turtle.pendown()
  turtle.circle(50, 180)

  # Arch 3
  turtle.penup()
  turtle.goto(275, -200)
  turtle.left(180)
  turtle.pendown()
  turtle.circle(50, 180)

  # Draw the wheels
  turtle.color("red")
  turtle.fillcolor("white")
  
  # Wheel 1
  turtle.penup()
  turtle.goto(-135, -200)
  turtle.left(180)
  turtle.pendown()
  turtle.circle(90)

  turtle.penup()
  turtle.goto(-145, -200)
  turtle.pendown()
  turtle.circle(80)
  draw_spokes(80)

  turtle.penup()
  turtle.goto(-203, -200)
  turtle.left(180)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(20)
  turtle.end_fill()

  # Wheel 2
  turtle.penup()
  turtle.goto(65, -200)
  turtle.pendown()
  turtle.circle(40)

  turtle.penup()
  turtle.goto(55, -200)
  turtle.pendown()
  turtle.circle(30)
  draw_spokes(30)

  turtle.penup()
  turtle.goto(35, -200)
  turtle.left(180)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(10)
  turtle.end_fill()

  # Wheel 3
  turtle.penup()
  turtle.goto(265, -200)
  turtle.pendown()
  turtle.circle(40)

  turtle.penup()
  turtle.goto(255, -200)
  turtle.pendown()
  turtle.circle(30)
  draw_spokes(30)

  turtle.penup()
  turtle.goto(235, -202)
  turtle.left(180)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(10)
  turtle.end_fill()












  # Persist the drawing
  turtle.done()


main()