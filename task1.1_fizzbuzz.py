# Task 1.1 - Fizzbuzz
# for numbers from 1 to 100,
# if the number is divisible by 3, print Fizz
# if it is divisible by 5, print Buzz
# if it is divisible by 3 and 5 (ie. 15) print FizzBuzz
# if not, print the number

for i in range(101):
    a=""
    if i%3==0: a+="Fizz"
    if i%5==0: a+="Buzz"
    print(a) if a else print(i)