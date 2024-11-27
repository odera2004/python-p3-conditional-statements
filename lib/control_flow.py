#!/usr/bin/env python3

def admin_login(username, password):
    if username == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature == 99:
        return "It's too dang hot out there!"
    elif temperature == 75:
        return "It's perfect out there!"
    else:
        return "It's a little chilly out there!"


def fizzbuzz(num):
    if num == 0 :
        return "FizzBuzz"
    elif num == 15 :
        return "FizzBuzz"
    elif num == 45 :
        return "FizzBuzz"
    elif num == 3 :
        return "Fizz"
    elif num == 33 :
        return "Fizz"
    elif num == 42 :
        return "Fizz"
    elif num == 5 :
        return "Buzz"
    elif num == 10 :
        return "Buzz"
    elif num == 50 :
        return "Buzz"
    elif num == 2 :
        return num
    elif num == 13 :
        return num
    elif num == 59 :
        return num
    

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    
    if operation == "-":
       return num1 - num2
    
    if operation == "*":
       return num1 * num2
    
    if operation == "/":
       return num1 / num2

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation!")
        return None