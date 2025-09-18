age_years = int(input("Enter your age in years: "))

days = age_years * 365
hours = days * 24
seconds = hours * 3600

print("You are approximately:")
print(f"{days} days old")
print(f"{hours} hours old")
print(f"{seconds} seconds old")