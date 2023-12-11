# This project was created by: Owen Pence

# I'm interested in creating a tool that gives a person an entire month of meal planning based on affordability, foods they enjoy, don't enjoy, allergic to, and healthy choices 
# Reason for interest: I want to do something like this because so many Americans and growing adults consistently eat poorly, and many of them don't eat well because they claim there's no meal plan for them

'''
Goals:
Create a data structer with categories
Create 4 categories
Have each category contain 5 food options
Include the amount of calories in each food option
Generate a healthy meal for someone that contains one food from each category
'''
import pandas

df = pandas.read_csv("data.csv")

print(df)

