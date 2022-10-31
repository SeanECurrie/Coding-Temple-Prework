#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

from asyncio import SendfileNotAvailableError


def hello_name(user_name):
    user_name = "Sean"
    print(f"hello {user_name}")

hello_name(" ")



#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    num = 1
    while num < 100:
        
        print(num)
        num += 2

    else:
        return None

first_odds()
    

