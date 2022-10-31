#magicians.py exersise
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#        print(magician)

#for magician in magicians:
#    print(magician.title() + ", that was a great trick!")
#    print("I can't wait to see your next trick," + magician.title() + ".\n")

#print("Thank you, everyone. That was a great magic show!")


#pizzas = ["one bite", "homerun", "jacks", "tombstone"]
#    print("I like " + pizza.title() + "!")

#print("I guess I like all pizzas?\n")     

#Playing around with making it look better and more spaced out using the \n. Wondering if there are better ways that doing print("n") at the begining

#print("\n")
#reptiles = ["snakes", "turtles", "lizards"]
#for reptile in reptiles:
#    print(reptile.title() + " are gross!")


#print("\nThat's right, I think all reptiles are gross!\n")

#Definetly looks better. Not sure if its the most effecient way though.

# Making numerical Lists :

#for value in range(1,6):
#    print(value)

#even_numbers=list(range(2,21,2))
#print(even_numbers)

#squares=[]
#for value in range(1,11):
#    squares.append(value**2)

#print(squares)

#List Comprehnsion version of the list manipulation above, raising is the the second power. Way tighter.

#squares = [value**2 for value in range(1,11)]
#print(squares)

#for value in range(1,21):   
#    print(value)

#million = []
#for value in range(1,1000001):
#    million.append(value)

#print(million)

#print(min(million))
#print(max(million))
#print(sum(million))

#odd_numbers = []
#for value in range(1,21,2):
#    odd_numbers.append(value)
#print(odd_numbers)

#multiples_3 = []
#for value in range(3,31,3):
#    multiples_3.append(value)
#print(multiples_3)

#cubed = []
#for value in range(1,11):
#    cubed.append(value**3)
#print(cubed)

#cubed_comp =[value**3 for value in range(1,11)]
#print(cubed_comp)

#players = ['charles', 'martina', 'michael', 'florence', 'eli']
#print(players[0:3])
#print(players[:4])
#print(players[-3:])

#print("\nHere's a list of the first three players on my team.")
#for player in players[:3]:
#    print(player.title())

#my_foods = ['pizza', 'falafel', 'carrot cake']
#friends_foods = my_foods[:]

#my_foods.append('cannoli')
#friends_foods.append('ice cream')

#print("My favorite foods are:")
#print(my_foods)



#print("\nMy friends favorite foods are:")
#print(friends_foods)


#Tuples work

#dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])

#for dimension in dimensions:
#    print(dimension)

#print("Original Dimensions:")
#for dimension in dimensions:
#    print(dimension)

#dimensions = (400, 100)
#print("\nModified Dimensions:")
#for dimension in dimensions:
#    print(dimension)

#buffet_items = ("mashed potatoes", "green beans", "salsbury steak", "sweet potatoes", "collard greens")
#print("\nOriginal Buffet Items:\n")
#for buffet_item in buffet_items:
#    print(buffet_item.title())
#print("\n")

#buffet_items = ("mashed potatoes", "green beans", "salsbury steak", "creamed corn", "bacon")
#print("\nRevised Buffet Items:\n")
#for buffet_item in buffet_items:
#    print(buffet_item.title())
#print("\n")

