def fizz_buzz (number):
        if str(number):
            return "This is not a number!!!"
        elif number %15 == 0:
            return "Fizz Buzz"
        elif number %3 == 0:
            return "Fizz"
        elif number %5 ==0:
            return "Buzz"
        else:
            return str(number)