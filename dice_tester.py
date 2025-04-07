import numpy as np

roll_num = 1

# Define the chi-squared values
chi_values = np.array([[2.706, 6.635],
                       [4.605, 9.210],
                       [6.251, 11.341],
                       [7.779, 13.277],
                       [9.236, 15.086],
                       [10.645, 16.812],
                       [12.017, 18.475],
                       [13.362, 20.090],
                       [14.684, 21.666],
                       [15.987, 23.209],
                       [17.275, 24.725],
                       [18.549, 26.217],
                       [19.812, 27.688],
                       [21.064, 29.141],
                       [22.307, 30.578],
                       [23.542, 32.000],
                       [24.769, 33.409],
                       [25.989, 34.805],
                       [27.204, 36.191]])

# Get user input
while True:
    num_sides = int(input("How many sides does the die have? "))
    if 1 < num_sides <= 20:
        break
    print("Value must be between 1 and 20")

while True:
    e_value = input("What iterative multiplier do you want to use? (default 10) ")
    if e_value == "":
        e_value = 10
    else:
        e_value = int(e_value)
    if e_value >= 5:
        break
    print("Value must be greater than 5")

num_rolls = num_sides * e_value
print(f"You will need to roll your die {num_rolls} times")
print("Please enter each number when prompted")

tally = [0] * 20
for _ in range(num_rolls):
    while True:
        roll = int(input(f"Input Roll #{roll_num}: "))
        if 0 <= roll < num_sides:
            tally[roll] += 1
            roll_num += 1
            break
        print("Invalid Roll")

print("\nTotals")
for i, count in enumerate(tally):
    print(f"{i+1}: {count}")

result = sum((count - e_value) ** 2 for count in tally) / e_value
print("\nYour Chi-Squared value is", result)

if result < chi_values[num_sides - 2, 0]:
    print("Which is less than", chi_values[num_sides - 2, 0])
    print("Your dice appears to be statistically unbiased")
elif chi_values[num_sides - 2, 0] <= result <= chi_values[num_sides - 2, 1]:
    print("Which is greater than", chi_values[num_sides - 2, 0], "and less than", chi_values[num_sides - 2, 1])
    print("The results were inconclusive please try again with a higher iterative multiplier")
else:
    print("Which is greater than", chi_values[num_sides - 2, 1])
    print("Your dice appears to be statistically biased")
