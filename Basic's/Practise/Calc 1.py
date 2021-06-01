number_1 = int(input('Enter your first number:'))
number_2 = int(input('Enter your second number:'))
operator = str(input('Enter your operator'))

if operator=='+':
    print(number_1 + number_2)
elif operator=='-':
    print(number_1 - number_2)
elif operator=='*':
    print(number_1 * number_2)
elif operator=='/':
    print(number_1 / number_2)
else:
    print('Invalid operator')
