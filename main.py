# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder:
# Date:
print("Simple Interest Calculator")

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period (in years): "))

si = (p * r * t) / 100

print(f"Simple Interest: {si:.1f}")
# Write your code here
