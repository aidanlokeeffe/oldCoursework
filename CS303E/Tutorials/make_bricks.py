'''def make_bricks(small, big, goal):
  inches_big = 5 * big
  remainder = goal % 5
  if goal - inches_big = 0:
  	return True
  elif goal - inches_big < 0:
  	if remainder - small <= 0
  	  return True
  elif goal - inches_big > 0:
  	if (goal - inches_big) - small <= 0
  	  return True'''

def make_bricks(small, big, goal):
  
  inches_big = 5 * big
  difference = goal - inches_big
  remainder = goal % 5

  if difference == 0 or goal - small == 0:
  	return True
  elif difference < 0:
    return remainder - small <= 0
  elif difference > 0:
  	return difference - small <= 0