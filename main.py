# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder:
# Date:
print("Simple Interest Calculator")
p = float(input("Enter principal amount:"))
r = float(input("Enter rate of interest:"))
t = float(input("Enter time period (in years):"))

si = (p * r * t) / 100

print(f"Simple Interest: {si:.1f}")
# Write your code here
