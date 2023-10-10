def fizz_buzz(number):
    # Check if the number is divisible by both 3 and 5.
    # If it is, then it's a FizzBuzz case.
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz 🎉"
    
    # Check if the number is divisible by 3 only.
    # If it is, then it's a Fizz case.
    elif number % 3 == 0:
        return "Fizz 🍾"
    
    # Check if the number is divisible by 5 only.
    # If it is, then it's a Buzz case.
    elif number % 5 == 0:
        return "Buzz 🐝"
    
    # If the number is neither divisible by 3 nor 5,
    # simply return the number itself.
    else:
        return number
