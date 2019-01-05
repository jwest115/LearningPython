'''
Created on Jan 3, 2019

@author: justine
'''

# CREATING A LIST
names = ["stan", "kyle", "cartman", "kenny"]
print(names)

# FIRST ELEMENT IN LIST
# INDEX STARTS AT 0
print(names[0])
print(names[0].title())

# LAST ITEM IN LIST
# USE -1 TO ACCESS LAST THE ELEMENT IN THE LIST
print(names[-1])
print(names[-1].title())


# ADD AN ELEMENT TO THE END OF THE LIST
names.append("butters")
print(names)

# USE insert(index, object) TO INSERT AN ELEMENT INTO A SPECIFIC INDEX IN A LIST
names.insert(2, "Timmy")
print(names)

# REMOVING AN ELEMENT AT A SPECIFIC INDEX
del(names[-1])
print(names)

# USE pop() TO RETURN AND DELETE THE LAST ELEMENT FROM A LIST
name_last = names.pop()
print("Just deleted " + name_last.title())
print(names)

name_second = names.pop(1)
print("Just deleted " + name_second)
print(names)

# REMOVES ONLY FIRST OCCURENCE OF SPECIFIED VALUE
names.remove("Timmy")
print(names)

# ORGANIZING LISTS
cars = ["Jeep", "Volkswagen", "Porsche", "Ford", "Dodge"]

# ALPHABETICAL ORDER SORT
print(cars)
cars.sort()
print(cars)

# REVERSE ALPHABTEICAL ORDER
cars.sort(reverse=True)
print(cars)

# TEMPORARILY SORT LIST
print(sorted(cars))
print(cars)

# REVERSE OF CURRENT LIST ORDERING
people = ["John", "Arya", "Khaleesi", "Tyrion", "Khal Drogo"]
people.reverse()
print(people)

# LENGTH OF A LIST
print(len(people))