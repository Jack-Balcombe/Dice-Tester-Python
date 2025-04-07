import numpy as np

# Initialise variables
num_sides = -1
e_value = -1

chi_values = np.array([[2.706, 6.635], [4.605, 9.210], [6.251, 11.341],
[7.779, 13.277], [9.236, 15.086], [10.645, 16.812], [12.017, 18.475],
[13.362, 20.090], [14.684, 21.666], [15.987, 23.209], [17.275, 24.725],
[18.549, 26.217], [19.812, 27.688], [21.064, 29.141], [22.307, 30.578],
[23.542, 32.000], [24.769, 33.409], [25.989, 34.805], [27.204, 36.191]])

# Get user input
while num_sides < 2 or num_sides > 20:
    try:
        num_sides = int(input("How many sides does the die have? Please enter a number from 2 to 20:\n"))

        if num_sides < 2 or num_sides > 20:
            print("\nThe number you entered was too big or too small. The number of sides must be an integer from 2 to 20\n")
    except ValueError:
        print("\nYou entered an invalid integer. The number of sides must be an integer from 2 to 20\n")

while e_value < 5:
    e_value = input("What iterative multiplier do you want to use? (minimum 5, default 10):\n")

    if e_value == "":
        e_value = 10
    else:
        try:
            e_value = int(e_value)

            if e_value < 5:
                print("\nThe number you entered was too small. The iterative multiplier must be at least 5\n")
        except ValueError:
            print("\nYou entered an invalid integer. The iterative multiplier must be an integer, and at least 5\n")
            e_value = -1

num_rolls = num_sides * e_value
tally = np.zeros(num_sides, dtype=int)

print(f"You will need to roll your die {num_rolls} times")
print("Please enter each number when prompted")

for i in range(num_rolls):
    roll = -1
    roll_num = i + 1

    while roll < 1 or roll > num_sides:
        try:
            roll = int(input(f"Input Roll {roll_num} of {num_rolls}: "))

            if 1 <= roll <= num_sides:
                tally[roll - 1] += 1
            else:
                print(f"\nInvalid roll for a {num_sides} sided die: Each roll must be an integer from 1 to {num_sides}\n")
        except ValueError:
            print(f"\nYou entered an invalid integer. Each roll must be an integer from 1 to {num_sides}\n")

# Display results
print()
print("Totals")
for i, count in enumerate(tally):
    print(f"{i+1}: {count}")

result = sum((count - e_value) ** 2 for count in tally) / e_value
chi_value_1 = chi_values[num_sides - 2, 0]
chi_value_2 = chi_values[num_sides - 2, 1]

print()
print(f"Your Chi-Squared value is {result}")

if result < chi_value_1:
    print(f"Which is less than {chi_value_1}")
    print("Your dice appears to be statistically unbiased")
elif chi_value_1 <= result <= chi_value_2:
    print(f"Which is greater than {chi_value_1} and less than {chi_value_2}")
    print("The results were inconclusive. Please try again with a higher iterative multiplier")
else:
    print(f"Which is greater than {chi_value_2}")
    print("Your dice appears to be statistically biased")
