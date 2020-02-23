#  File: Geom.py

#  Description: Defines and tests three classes of geometric objects 

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 1 / 31 / 2018

#  Date Last Modified: 2 / 1 / 2018

import math

class Point(object):
  # Constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # Returns distance between two points
  def dist(self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  # Returns appropriate string representaion for points
  def __str__(self):
    return "(" + str(self.x) + ", " + str(self.y) + ")"

  # Tests that two points are equal
  def __eq__(self, other):
    tol = 1.0e-16
    return abs(self.x - other.x) < tol and abs(self.y - other.y) < tol


class Circle(object):
  # Constructor
  def __init__(self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point(x, y)

  # Returns circumference of given circle
  def circumference(self):
    return 2.0 * math.pi * self.radius

  # Returns area of given circle
  def area(self):
    return math.pi * self.radius ** 2

  # Determines if a point is strictly inside given circle
  def point_inside(self, p):
    return self.center.dist(p) < self.radius

  # Determines if another circle is strictly inside given circle
  def circle_inside(self, c):
    distance = self.center.dist(c.center)
    return distance + c.radius < self.radius

  # Determines if another circle intersects given circle
  def does_intersect(self, c):
    distance = self.center.dist(c.center)
    return distance < self.radius + c.radius

  # Determines smallest circle circumscribing given rectangle
  def circle_circumscribes(self, r):
    rec_center = Point((r.ul.x + r.lr.x) / 2, (r.ul.y + r.lr.y) / 2)
    new_radius = rec_center.dist(r.ul)
    return Circle(new_radius, (r.ul.x + r.lr.x) / 2, (r.ul.y + r.lr.y) / 2)

  # Returns appropriate string representation for circles
  def __str__(self):
    return("Center: (" + str(self.center.x) + ", " + str(self.center.y) + "), Radius: "
           + str(self.radius))

  # Determines if two circles are congruent
  def __eq__(self, other):
    tol = 1.0e-16
    return abs(self.radius - other.radius) < tol


class Rectangle(object):
  # Constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # Returns x dimension of rectangle
  def length(self):
    return self.lr.x - self.ul.x

  # Returns y dimension of rectangle
  def width(self):
    return self.ul.y - self.lr.y

  # Returns perimeter
  def perimeter(self):
    return 2 * (self.length() + self.width())

  # Returns area
  def area(self):
    return self.length() * self.width()

  # Determines if given point is inside the rectangle
  def point_inside(self, p):
    return((p.x > self.ul.x and p.x < self.lr.x) and 
    	  (p.y > self.lr.y and p.y < self.ul.y))

  # Determines if another rectangle is strictly insides the rectangle
  def rectangle_inside(self, r):
    # Check that r.ul meets criteria
    is_inside = r.ul.x > self.ul.x
    is_inside = is_inside and r.ul.x < self.lr.x
    is_inside = is_inside and r.ul.y > self.lr.y 
    is_inside = is_inside and r.ul.y < self.ul.y 

    # Check that r.lr meets the same criteria
    is_inside = is_inside and r.lr.x > self.ul.x
    is_inside = is_inside and r.lr.x < self.lr.x
    is_inside = is_inside and r.lr.y > self.lr.y 
    is_inside = is_inside and r.lr.y < self.ul.y

    return is_inside

  # Determines if two rectangles overlap
  def does_intersect(self, r):
    # Check for total overlap
    if self.rectangle_inside(r) or r.rectangle_inside(self):
      return True

    # Check for any corner overlap
    r_ll = Point(r.ul.x, r.lr.y)
    r_ur = Point(r.lr.x, r.ul.y)
    
    corner_inside = self.point_inside(r.ul)
    corner_inside = corner_inside or self.point_inside(r.lr)
    corner_inside = corner_inside or self.point_inside(r_ll)
    corner_inside = corner_inside or self.point_inside(r_ur)

    if corner_inside:
      return True

    # Check for non-corner, non-total overlap
    vert_overlap = r.ul.x > self.ul.x
    vert_overlap = vert_overlap and r.lr.x < self.lr.x
    vert_overlap = vert_overlap and r.ul.y > self.ul.y 
    vert_overlap = vert_overlap and r.lr.y < self.lr.y 

    hor_overlap = r.ul.y < self.ul.y
    hor_overlap = hor_overlap and r.lr.y > self.lr.y 
    hor_overlap = hor_overlap and r.ul.x < self.ul.x
    hor_overlap = hor_overlap and r.lr.x < self.lr.x

    if vert_overlap or hor_overlap:
      return True

    return False


  # Determines the smallest rectangle circumscribing a given circle
  def rect_circumscribe(self, c):
    new_rect_ul_x = c.center.x - c.radius
    new_rect_ul_y = c.center.y + c.radius
    new_rect_lr_x = c.center.x + c.radius
    new_rect_lr_y = c.center.y - c.radius

    new_rect = Rectangle(new_rect_ul_x, new_rect_ul_y, new_rect_lr_x, new_rect_lr_y)
    return new_rect

    # Gives string representation of a rectangle
  def __str__(self):
    ul = "UL: (" + str(self.ul.x) + ", " + str(self.ul.y) + "), "
    lr = "LR: (" + str(self.lr.x) + ", " + str(self.lr.y) + ")"
    return ul + lr

  # Determines if two rectangles are congruent
  def __eq__(self, other):
    tol = 1.0e-16
    are_equal = abs(self.length() - other.length()) < tol
    are_equal = are_equal and abs(self.width() - self.width()) < tol
    return are_equal


def main():
  # Open the file geom.txt and process lines
  in_file = open("geom.txt", "r")
  attribute_list = []
  for line in in_file:
    line = line.strip()
    line_list = line.split()
    attribute_list.append(line_list)

  # Create Point objects P and Q
  p_list = attribute_list[0]
  q_list = attribute_list[1]
  point_P = Point(float(p_list[0]), float(p_list[1]))
  point_Q = Point(float(q_list[0]), float(q_list[1]))

  # Print the coordinates of the points P and Q
  print("Coordinates of P:", point_P)
  print("Coordinates of Q:", point_Q)

  # Find the distance between the points P and Q
  dist = point_P.dist(point_Q)
  print("Distance between P and Q:", dist)
 
  # Create two Circle objects C and D
  c_list = attribute_list[2]
  d_list = attribute_list[3]
  circle_C = Circle(float(c_list[2]), float(c_list[0]), float(c_list[1]))
  circle_D = Circle(float(d_list[2]), float(d_list[0]), float(d_list[1]))

  # Print C and D
  print("Circle C:", circle_C)
  print("Circle D:", circle_D)

  # Compute the circumference of C
  print("Circumference of C:", circle_C.circumference())

  # Compute the area of D
  print("Area of D:", circle_D.area())

  # Determine if P is strictly inside C
  if circle_C.point_inside(point_P):
    print("P is inside C")
  else:
    print("P is not inside C")

  # Determine if C is strictly inside D
  if circle_D.circle_inside(circle_C):
    print("C is inside D")
  else:
  	print("C is not inside D")

  # Determine if C and D intersect (non zero area of intersection)
  if circle_C.does_intersect(circle_D):
  	print("C does intersect D")
  else:
    print("C does not intersect D")

  # Determine if C and D are equal (have the same radius)
  if circle_C.__eq__(circle_D):
    print("C is equal to D")
  else:
  	print("C is not equal to D")

  # Create two rectangle objects G and H
  g_list = attribute_list[4]
  h_list = attribute_list[5]
  rect_G = Rectangle(float(g_list[0]), float(g_list[1]), float(g_list[2]), float(g_list[3]))
  rect_H = Rectangle(float(h_list[0]), float(h_list[1]), float(h_list[2]), float(h_list[3]))

  # Clear unnecessary data
  in_file.close()
  del attribute_list
  del p_list
  del q_list
  del c_list
  del d_list
  del g_list
  del h_list

  # Print the two rectangles G and H
  print("Rectangle G:", rect_G)
  print("Rectangle H:", rect_H)

  # Determine the length of G (distance along x axis)
  print("Length of G:", rect_G.length())

  # Determine the width of H (distance along y axis)
  print("Width of H:", rect_H.width())

  # Determine the perimeter of G
  print("Perimeter of G:", rect_G.perimeter())

  # Determine the area of H
  print("Area of H:", rect_H.area())

  # Determine if point P is strictly inside rectangle G
  if rect_G.point_inside(point_P):
    print("P is inside G")
  else:
    print("P is not inside G")

  # Determine if rectangle G is strictly inside rectangle H
  if rect_H.rectangle_inside(rect_G):
    print("G is inside H")
  else:
    print("G is not inside H")

  # determine if rectangles G and H overlap (non-zero area of overlap)
  if rect_H.does_intersect(rect_G):
    print("G does overlap H")
  else:
    print("G does not overlap H")

  # Find the smallest circle that circumscribes rectangle G
  # Goes through the four vertices of the rectangle
  circum_rect = circle_D.circle_circumscribes(rect_G)
  print("Circle that circumscribes G:", circum_rect)

  # Find the smallest rectangle that circumscribes circle D
  # Fll four sides of the rectangle are tangents to the circle
  circum_circ = rect_G.rect_circumscribe(circle_D)
  print("Rectangle that circumscribes D:", circum_circ)

  # Determine if the two rectangles have the same length and width
  if rect_G.__eq__(rect_H):
    print("Rectangle G is equal to H")
  else:
    print("Rectangle G is not equal to H")


main()