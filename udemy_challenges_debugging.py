## Challenge 1 --- fix it so it runs
def odd_or_even(number):
    if number % 2 == 0: ## corrected this line from = to ==
        return "This is an even number."
    else:
        return "This is an odd number."

## Challenge 2 -- fix it so it runs
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: ## Changed the value on this line from 4000 to 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False


##Challenge 3 -- fix it so it runs
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0: ##corrected 'and' to 'or'
            print("FizzBuzz")
        elif number % 3 == 0: ##changed 'if' to 'elif'
            print("Fizz")
        elif number % 5 == 0:  ##changed 'if' to 'elif'
            print("Buzz")
        else:
            print(number) ##removed random square brackets around number
fizz_buzz(20)