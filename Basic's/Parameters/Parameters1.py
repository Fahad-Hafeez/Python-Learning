def per_calc(numbers_obtained):
    total = 100
    increase = total - numbers_obtained
    result = (numbers_obtained / increase) * 100
    print(result)

per_calc(90)

def diff_calc(numbers_obtained):
    total = 200
    result = total - numbers_obtained
    print(result)


diff_calc(70)


def greet_user(first_name, last_name):
    print(f'Hi{first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("Fahad", "Hafeez")
print("Finish")
