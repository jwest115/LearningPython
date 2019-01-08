'''
Created on Jan 4, 2019

@author: justine
'''

# FOR LOOPS
shows = ["Game of Thrones", "The Walking Dead", "Sons of Anarchy", "Breaking Bad", "Black Mirror"]
print("Some of my favorite shows are: \n")
count = 1
for show in shows:
    print(str(count) + ". " + show + "\n")
    count += 1

# RANGE FUNCTION
print("\n\nI am going to count to 10 \n")
for number in range(1, 11):
    print(number)

# RANGE TO MAKE A LIST OF NUMBERS
range_list = list(range(1, 101))
print(range_list)

# PRINTING RANGE LIST USING FOR LOOP
for number in range_list:
    print(number)
   
        
# RANGE FUNCTION USED TO SKIP 2 REPEATEDLY TIL IT REACHES THE UPPER BOUND OF THE RANGE
print("\n\n")
for number in range(2, 22, 2):
    print(number)

# MIN, MAX, SUM
print("\n\n")
num_list = [10, 2, 11, 62, 66, 3]
print("Max: " + str(max(num_list)))
print("Min: " + str(min(num_list)))
print("Sum: " + str(sum(num_list)))
print("\n")

# SLICING A LIST
# WORK WITH A SPECIFIC GROUP OF ITEMS IN A LIST
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(colors[0:3])
print(colors[3:])
print(colors[:4])
print(colors[:-1])

# LOOPING THROUGH A SLICE
print("\nFirst three colors in the list:")
for color in colors[0:3]:
    print(color)
    
# COPYING A LIST
new_colors = colors[:]
print("\nOriginal List:")
for color in colors:
    print(color)
    
print("\nCopied List:")
for color in new_colors:
    print(color)
    
# TUPLES
# LIST OF ITEMS THAT CANNOT CHANGE ---> IMMUTABLE
print("\n")

dimensions = (5, 7)
print(dimensions)

print("\nPrinting tuple with a loop: ")
for dimension in dimensions:
    print(dimension)
    
# WRITING OVER A TUPLE
dimensions = (1, 2)
print("\nWriting over the dimensions tuple:\n" + str(dimensions))
