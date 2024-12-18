# Create a Python code that solves the following exercises by applying the appropriate string 

# Part 1: Basic f-string Formatting
# Prompt the user for input.
name = input("what is your name? ")
course = input("What is your course? ")
favorite_color = input("What is your favorite color? ")

# Using an f-string to format the output
print (f"Hi, my name is {name}, a {course} student and my favorite color is {favorite_color}.")


# Part 2: Using  .format()
# Prompt the user for input.
brand_name1 = input("Favorite brand: ")
brand_name2 = input("Least favorite brand: ")

# Using .format()
message = "My favorite brand is {} and least favorite is {}." .format(brand_name1, brand_name2)
print (message)


# Part 3: Legacy % formatting.
country = "Philippines"
weather_celsious = 29
weather_fahrenheit = 84.2

# Using % operator
print ("Weather in the %s is %d degrees in celcious and %.1f in fahrenheit." % (country, weather_celsious, weather_fahrenheit))
