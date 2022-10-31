foods = ["pizza", "tacos", "dim sum", "sushi"]

#LOOPS , syntax
# for PLACEHOLDER in THE LIST WE WANT TO LOOK AT:
    #this is a codeblock
    #this code block
    #will run every item in the list

#for food in foods:
#    print("\n")
#    print(f"I like to eat {food.title()}.")
#    print(type(food))
#print("\n")   

#for food in foods:
#    if food == "dim sum":
#        continue
#    print(f"I like {food} because they are yummy.")

#for index in range(len(foods)):
#    print(index)
#    print(foods[index])

#print(list(enumerate(foods)))
#for index, food in enumerate(foods):
#    print(f"My No. {index+1} food is {food.title()}")

#TUPLES

#my_tup = (1,2)
#print(type(my_tup))
#print(my_tup)

#for num in my_tup:
#    print(num)

#my_tup = my_tup +(3,4)
#print(my_tup)

#SLICING

#my_string = "Hey Guys Lets Learn Python"
#my_list = ["pizza", "tacos", "dim sum", "sushi"]

#To get "Guy"
#print(my_string[4:7])

#print whole list, good for copying lists
#print(my_string[:])

#print(my_list[1:4:2])

#print(my_list[-1])

my_list = [1,3.0, ["a","b",["A","B","C"],"d"], "John"]
print(my_list)
print(my_list[2])
print(my_list[2][2])
