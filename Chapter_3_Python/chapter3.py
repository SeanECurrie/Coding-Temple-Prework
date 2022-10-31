# Index    0  1  2     3   4
numbers = [2, 6, 10, 12.5, 0] #this is also comment
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print(numbers[1]*2.5)

print(numbers[3])

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods[1])
print(foods[1].upper())

x = 12
y = 15.5
z = "Z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))
print(random_list[1])
print(type(random_list[1]))
print(random_list[2])
print(type(random_list[2]))

my_fav_num = random_list[0]
print(my_fav_num)


foods.append("cheeseburger")
print(foods)
foods = ["pizza", "tacos", "dim sum", "sushi"]

foods.insert(0, "pho")
print(foods)

foods.remove("pho")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]

foods.append("pizza")
print(foods)
foods.remove("pizza")
print(foods)
foods.remove("pizza")
foods = ["pizza", "tacos", "dim sum", "sushi"]

del foods[1]
print(foods)

#POP PRACTICE
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.pop())
print(foods)

# method of the list class called .sort
# built in function called sorted()
#sort is in place
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

#sorted is Out of Place
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(sorted(foods))
print(foods)
foods = sorted(foods)
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.reverse()
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]











