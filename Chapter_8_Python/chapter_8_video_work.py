# def NAME_OF_FUNCTION(PARAMETERS):
    # these line
    # belond to 
    # the code block
    # for the function

#def hello():
#    return "hello"

#print(hello().upper())

#def hello(age, name = "John"):
#    print(f"Hello {name}. You are {age} years old")


#hello(23)

def say_hello(name, age):
    print(f"Hello {name} you are {age} years old.")

def say_goodbye():
    print("Goodbye!")

def greet_back(feeling):
    if feeling == "good":
        print("Awesome, I feel good too.")
    elif feeling == "bad":
        print("I am so sorry!")
    elif feeling == "stressed":
        print("Coding can be hard to learn.")
    else:
        print("Welp, have a good day!")

#DRIVER CODE

while True:
    response = input("What do you want to do?\n Say hello [h]\n Say Goodbye [g]\n Talk to me [t]\n Quit [q]\n")
    if response.lower() == "q":
        say_goodbye()
        break
    elif response.lower() == "h":
        name = input("What is your name?")
        age = input("What is your age?")
        say_hello(name, age)
    elif response.lower() == "g":
        say_goodbye()
    elif response.lower() == "t":
        f= input("How are you today?") 
        greet_back(f)
    else:
        print("Invalid input")
