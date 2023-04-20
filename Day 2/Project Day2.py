print("Welcome to the tip calculator.")

total = input("What was the total bill? ")

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
p = int(percentage)
new_percentage = (p/100) + 1

t = float(total) 

new_total = (t * new_percentage)

people = input("How many people to split the bill? ") 

p = int(people)
results = float(new_total / p)
results = round(results, 2)

# print(f"Each person should pay: {results:,.2f} ")
print(f"Each person should pay: {results} ")