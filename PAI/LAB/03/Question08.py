try:
    num1 = int(input('Enter the number 1: '))
    num2 = int(input('Enter the number 2: '))
    div = num1 / num2
    print(div)

except ZeroDivisionError as e:
    print('Denominator is 0')
except ValueError as v:
    print('Given number is not a integer')