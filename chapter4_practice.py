classes = ["CS3337", "PHYS2200", "CS2148", "ENGR1540"]
for c in classes:
	print(c)


# DICTIONARY OF ALIENS WITH KEY VALUE PAIRS COLOR AND POINTS
aliens = {"green" : "5", "red" : "2", "blue" : "3", "purple" : "4"}

for color in sorted(aliens.keys()) :
	print("color is " + str(color))


for point in sorted(aliens.values()) :
	print("number of points is " + str(point))

for key, value in aliens.items():
	print("color is " + key + " and number of points is " + value)


members = {"kai" : "exo", "jk" : "bts"}
for name, band in members.items():
	print("name is " + name + " and band is " + band)