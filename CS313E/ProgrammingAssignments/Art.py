#  File: Art.py

#  Description: Draws a recursive figure

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2 / 28 / 2018

#  Date Last Modified:

import turtle
import random

# Draw a line from point p1 to point p2
def drawLine(ttl, p1, p2):
  x1 = p1[0]
  y1 = p1[1]
  x2 = p2[0]
  y2 = p2[1]
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# Draw an arc around given center or radius rad
def drawArc(ttl, rad, cent_x, cent_y, level, start):
  ttl.penup()
  ttl.goto(start[0], start[1])
  ttl.pendown()
  if level % 2 == 0:
    ttl.setheading(180)
  else:
  	ttl.setheading(0)
  ttl.circle(rad, 180)
  ttl.penup()


# Draw recursive figure
def rec_art(ttl, order, colors):
  
  if order > 0:

    # Set color
    ttl.color(colors[order - 1])

    # Define points
    top_y_list = [256, 128, 64, 32, 16, 8]
    bot_y_list = [-256, -128, -64, -32, -16, -8]
    x_list = [0, 128, 64, 96, 80, 88]
    tip_x_list = [256, 0, 128, 64, 96, 88]

    top = [x_list[order - 1], top_y_list[order - 1]]
    bot = [x_list[order - 1], bot_y_list[order - 1]]
    tip = [tip_x_list[order - 1], 0]

    # Draw inscribed triangle
    drawLine(ttl, top, tip)
    drawLine(ttl, tip, bot)
    drawLine(ttl, bot, top)

    # Draw circumscribing arc
    if order % 2 != 0:
      drawArc(ttl, (top_y_list[order - 1]), x_list[order - 1], 0, order, bot)
    else:
      drawArc(ttl, (top_y_list[order - 1]), x_list[order - 1], 0, order, top)


    # Draw rest of figure recursively
    rec_art(ttl, order - 1, colors)


def random_dot(ttl, order):
  for i in range((7 * order) + (random.randint(1, 3) * random.randint(-1, 1))):
    ttl.penup()
    rand_x = random.randint(-254, -3)
    rand_y = random.randint(-254, 254)
    ttl.goto(rand_x, rand_y)
    ttl.dot(5, "black")
    ttl.penup()
  

def main():
  # Print header
  print("Recursive Art" + "\n")

  # Prompt the user for order of recursion with error checking
  order = int(input("Enter a level of recursion between 1 and 6: "))
  while order not in range(1, 7):
    order = int(input("Enter a level of recusrion between 1 and 6: "))

  # Set window label
  turtle.title("You can only structure so much of your life.")

  # Set up window
  turtle.setup(800, 800, 0, 0)

  # Create and setup a passable turtle object
  ttl = turtle.Turtle()
  ttl.pensize(4)
  ttl.speed(10)

  # Create background
  ttl.penup()
  ttl.goto(-400, -400)
  ttl.color("orange red")
  ttl.begin_fill()
  ttl.goto(-400, 400)
  ttl.goto(400, 400)
  ttl.goto(400, -400)
  ttl.goto(-400, -400)
  ttl.end_fill()

  # Create widescreen bars
  ttl.color("black")
  for y in [-400, 320]:
    ttl.penup()
    ttl.goto(-400, y)
    ttl.pendown()
    ttl.begin_fill()
    ttl.goto(-400, y + 80)
    ttl.goto(400, y + 80)
    ttl.goto(400, y)
    ttl.goto(-400, y)
    ttl.end_fill()
    ttl.penup()


  # Create color list for ttl object to access
  color_list = ["black", "red", "black", "red", "black", "red"]

  # Draw structured part
  rec_art(ttl, order, color_list)


  # Draw unstructured part
  random_dot(ttl, order)

  # Persist drawing
  turtle.done()


main()