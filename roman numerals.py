#roman numerals using Python
def numerals(number):
    count = number
    numeral = ''
    while count > 0:
        if count >= 1000:
            numeral += 'M'
            count -= 1000
        elif count >= 500:
            numeral += 'D'
            count -= 500
        elif count >= 100:
            numeral += 'C'
            count -= 100
        elif count >= 50:
            numeral += 'L'
            count -= 50
        elif count >= 10:
            numeral += 'X'
            count -= 10
        elif count >= 5:
            numeral += "V"
            count -= 5
        elif count >= 1:
            numeral += "I"
            count -= 1
    return str(number) + " is " + str(numeral) + " in roman numerals"

print(numerals(int(input("Please enter the number you want to be converted into roman numerals: "))))
