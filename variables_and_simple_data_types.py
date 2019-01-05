'''
Created on Jan 3, 2019

@author: justine
'''

# SIMPLE PRINT STATEMENTS
print("Hello Word!")
print("Print statements in python are way simpler than Java print statements!")

# CREATING VARIABLES
my_name = "Justine"
my_age = 21
favorite_game = "Red Dead Redemption 2"
# WHEN CONCATENATING INTS WITH STRINGS, MUST USE str() TO PARSE INT AS A STRING
# IF NOT, RESULTS IN TYPE ERROR
print("My name is "  + my_name + ", I am " + str(my_age) + " and currently my favorite game is " + favorite_game)

# SOME USEFUL FUNCIONS FOR STRING MANIPULATION
name_in_upper = "JUSTNE"
# CONVERTS A STRING TO UPPER CASE
print("justine".upper())
# CONVERTS A STRING TO LOWER CASE
print(name_in_upper.lower())
# MAKES EVERY FIRST LETTER IN EACH WORD UPPER CASE AND EVERY NON FIRST LETTER LOWERCASE
print("the shining".title())
print(name_in_upper.title())

whitespace = "   Here is some whitespace       "
# USE rstrip() TO STRIP WHITESPACE FROM THE RIGHT OF A STRING
print(whitespace.rstrip())
# USE lstrip() TO STRIP WHITESPACE FROM THE LEFT SIDE OF A STRING
print(whitespace.lstrip())
# USE strip() TO STRIP WHITESPACE FROM BOTH SIDES OF A STRING
print(whitespace.strip())


# SIMPLE MATH OPERATIONS

int_1 = 4
int_2 = 5

# ADDITION
print(int_1 + int_2)
print(5 + 2)

# SUBTRACTION
print(int_1 - int_2)
print(5 - 2)

# MULTIPLICATION
print(int_1 * int_2)
print(5 * 2)

# TWO ASTERIKS FOR EXPONENTS
print(int_1 ** 2)
print(int_1 ** int_2)
print(2 ** 2)

# DIVISION
print(10 / 2)
print(int_1 / int_2)

# MODULO
print(20 % 2)
print(5 % 2)