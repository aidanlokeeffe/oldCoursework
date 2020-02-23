import time

import math

divisor = eval(input("How many sides are on your die: "))

T = time.time()

A = math.cos(T)

faceUp = math.ceil(((T + 12) / A) % divisor)

print(faceUp)
