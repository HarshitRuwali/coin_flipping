import time
import os
import random 
import datetime

starttime = time.time()

heads = 0
tails = 0
flipped = 0
i = 0

print('This shows the number results of tossing a coin randomly')

repeat = int(input('Enter the amount of times you would like the coin to be tossed: '))

print("Flipped a coin", repeat, "times, and the results are as follows:")

while i < repeat:
	flip = random.randrange(2)
	flipped = flipped+1
	i=i+1
	if flip == 0:
		heads = heads+1
		print('Heads')
	else:
		tails = tails+1
		print('Tails')

tailspercent = (100/repeat)*tails
headspercent = (100/repeat)*heads

print("Tails appeared", tails, "times, or", tailspercent, "% of the time.")
print("Heads appeared", heads, "times, or", headspercent, "% of the time.")
