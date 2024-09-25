def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:

# 1. What is the for loop doing?
### The loop is incrementally checking i and increasing its' value by one. it will print when i == 20

# 2. When is the function meant to print "You got it"?
### When i == 20

# 3. What are your assumptions about the value of i?
### That it's value will be checked from 1 - 20 incrementally, but it's actually not including 20 due to how 'in range' works
