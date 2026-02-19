# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder:
# Date:
print("Simple Interest Calculator")

print("Enter principal amount:")
p = float(input().split()[-1])

print("Enter rate of interest:")
r = float(input().split()[-1])

print("Enter time period (in years):")
t = float(input().split()[-1])

si = (p * r * t) / 100

print(f"Simple Interest: {si:.1f}")
# Write your code here
