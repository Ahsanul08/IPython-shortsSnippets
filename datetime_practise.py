from datetime import datetime

print "Today is {dt:%d-%m-%Y} and now it is {dt:%H}'o clock with {dt:%M} minutes and {dt:%S} seconds".format(dt = datetime.now())
