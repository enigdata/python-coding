### Range
def fizz_buzz(numbers):
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'
        elif num%3 == 0:
            numbers[i] = 'fizz'
        elif num%5 == 0:
            numbers[i] = 'buzz'

#### Enumerate
def fizz_buzz2(numbers):
    for idx, num in enumerate(numbers):
        if num%3 == 0 and num%5 == 0:
            numbers[idx] = 'fizzbuzz'
        elif num%3 == 0:
            numbers[i] = 'fizz'
        elif num%5 == 0:
            numbers[i] = 'buzz'


