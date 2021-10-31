#ask for the number and convert it to roman number

#ask for the number
number = int(input("Enter a number: "))

# convert to roman number the given number, a roman number is a string of letters
# that represent a number.
# The letters are as follows:
#   M = 1000
#   D = 500
#   C = 100
#   L = 50
#   X = 10
#   V = 5
#   I = 1
#   The letters are placed in order of value, starting with the largest.
#   The letters “I” and “X” are always used in pairs, as in “VII” or “XII”.
#   The letters “C” and “M” are used in pairs, as in “CCC” or “MCC”.
#   The letters “D” and “L” are used in pairs, as in “DCC” or “LXX”.
#   The letters “V” and “V” are used in pairs, as in “VIII” or “XIV”.
#   The letters “I” and “X” are used in pairs, as in “IX” or “XI”.

# if the is bigger than 1000 divide it by 1000 and add M to the string n times
roman_number=""
if number >= 1000:
    n = number // 1000
    roman_number = "M" * n
    number = number % 1000
# if the is bigger than 500 divide it by 500 and add C to the string n times
if number >= 500:
    n = number // 500
    roman_number = roman_number + "D" * n
    number = number % 500
# if the is bigger than 100 divide it by 100 and add D to the string n times
if number >= 100:
    n = number // 100
    roman_number = roman_number + "C" * n
    number = number % 100
# if the is bigger than 50 divide it by 50 and add V to the string n times
if number >= 50:
    n = number // 50
    roman_number = roman_number + "L" * n
    number = number % 50
# if the is bigger than 10 divide it by 10 and add X to the string n times
if number >= 10:
    n = number // 10
    roman_number = roman_number + "X" * n
    number = number % 10
# if the is bigger than 5 divide it by 5 and add V to the string n times
if number >= 5 and number < 10:
    n = number // 5
    roman_number = roman_number + "V" * n
    number = number % 5

# if the is bigger than 1 divide it by 1 and add I to the string n times
if number >= 1 and number < 3:
    n = number // 1
    roman_number = roman_number + "I" * n
    number = number % 1
elif number >= 3 and number < 5:
    roman_number = roman_number + "I" + "V"
    number = number % 1


print(' The number is : ' ,  number)
print(roman_number, end="")