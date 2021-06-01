try:
    age: str = input('Age: ')
    income = 20000
    # noinspection PyTypeChecker
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
