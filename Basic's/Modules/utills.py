def find_max(numbers):
    numbers = [10, 3, 6, 2]
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
