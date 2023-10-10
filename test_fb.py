from fizz_buzz import fizz_buzz

def test_fizz():
    assert fizz_buzz(3) == "Fizz 🍾"
    assert fizz_buzz(6) == "Fizz 🍾"
    assert fizz_buzz(9) == "Fizz 🍾"

def test_buzz():
    assert fizz_buzz(5) == "Buzz 🐝"
    assert fizz_buzz(10) == "Buzz 🐝"
    assert fizz_buzz(20) == "Buzz 🐝"

def test_fizzbuzz():
    assert fizz_buzz(15) == "FizzBuzz 🎉"
    assert fizz_buzz(30) == "FizzBuzz 🎉"
    assert fizz_buzz(45) == "FizzBuzz 🎉"

def test_neither():
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(4) == 4
