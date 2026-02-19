# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder:
# Date:
print("Simple Interest Calculator")

print("Enter the principal amount:")
p = float(input())

print("Enter the rate of interest:")
r = float(input())

print("Enter the time period (in years):")
t = float(input())

si = (p * r * t) / 100

print(f"Simple Interest: {si:.1f}")
# Write your code here
