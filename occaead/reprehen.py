# Python code to demonstrate working of
# Get Current Date and Time
# Using strftime()

# importing datetime module
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# using strftime() to convert to string
result = current_time.strftime("%Y-%m-%d %H:%M:%S")

# printing result
print("Current Date and Time is:", result)
