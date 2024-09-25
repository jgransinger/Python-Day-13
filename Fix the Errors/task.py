try:
    age = int(input("How old are you?"))  ## Added the try / except methods to catch the valueerror (if letters entered)
except ValueError:
    print("Please try again, and enter only a number: ")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.") ## add f to string, indented line.
