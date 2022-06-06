import time

print("This is my first Python program!")
print("It is beautiful")

print()

#counting with loops
x = 2
while(x < 100000):
  print(x)
  x = x**2

print("")

print("Getting ready to count....")
for x in range(10):
  print("I'm counting and at ", x)
  time.sleep(1)
print("Done counting!!!!")

#Favorite food
fruit = input("what is your favorite fruit?..\n")
print(f"Your favorite fruit is {fruit}")

a = ["a", "bc", "rye", "hello", "c", ""]

print()

#Find letters in a list of strings that are greater than 2
for letters in a:
  if len(letters) >= 2: 
    print(letters)
  else:
    print("less than 2")

#Find the fruit
fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]

while fruit != "stop":
  fruit = input("enter the name of a fruit or stop to exit: ")
  if fruit.lower() == "stop": 
    break
  if fruit in fruit_list:
    print("your fruit is at index " + str(fruit_list.index(fruit)) + " in the list.")
  else:
    print("try again!!!")
print("thank you for playing")