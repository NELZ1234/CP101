import math

# This is a prompt for the subjects taken to compute the average
# float will be used to calculate as decimals can appear 
mathematics_subject = float(input("Math Grade:"))
science_subject = float(input("Science Grade:"))
english_subject = float(input("English Grade:"))

# This calculates the sum of the three subjects
sum_of_all_subjects = mathematics_subject + science_subject + english_subject

# This calculates the total average
total_average = (sum_of_all_subjects / 3)

# Now this will print the average of the subjects
print(total_average)
