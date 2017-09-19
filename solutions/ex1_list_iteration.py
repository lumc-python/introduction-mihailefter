# Exercise 1: Iterate over a list
# ==========
#
# First we are going to make a list and fill it with a simple sequence.
# Then we are going to use this list to print something.
# - Make a list containing the numbers 0, 1, ... 9.
# - Print the last 10 lines of the song ''99 bottles of beer'' using this list.
#
# Song lyrics
# -----------
#
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
#
# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down and pass it around, 97 bottles of beer on the wall.
#
# ...
#
# 9 bottles of beer on the wall, 9 bottles of beer.
# Take one down and pass it around, 8 bottles of beer on the wall.
#
# ...
#
# 2 bottles of beer on the wall, 2 bottles of beer.
# Take one down and pass it around, 1 bottle of beer on the wall.
#
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
#
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.

# Code
# ----

# Creating the list containing the numbers 0, 1, ..., 9.
bottles = range(10)

# Printing the similar lines, i.e., 9 to 3.
for i in bottles[9:2:-1]:
    print "{0} bottles of beer on the wall, {1} bottles of beer.\n"\
          "Take one down and pass it around, "\
          "{2} bottles of beer on the wall.\n".format(i, i, i-1)

# Printing the remaining distinct lines.
print "2 bottles of beer on the wall, 2 bottles of beer.\n"\
       "Take one down and pass it around, 1 bottle of beer on the wall.\n"

print "1 bottle of beer on the wall, 1 bottle of beer.\n"\
       "Take one down and pass it around, no more bottles of beer on the wall.\n"
   
print "No more bottles of beer on the wall, no more bottles of beer.\n"\
      "Go to the store and buy some more, 99 bottles of beer on the wall."
