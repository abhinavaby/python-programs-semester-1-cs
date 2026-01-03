print("--- Biodata Form ---")

# Collect personal information
name = input("Enter your Name: ")
father_name = input("Enter your Father's Name: ")
locality = input("Enter your Locality: ")
date_of_birth = input("Enter your Date of Birth (DD/MM/YYYY): ")
age = int(input("Enter your Age: ")) # Convert age to an integer
nation = input("Enter your Nationality: ")
email = input("Enter your Email Address: ")
phone_number = input("Enter your Phone Number: ")

print("\n--- Your Biodata ---")
print(f"Name: {name}")
print(f"Father's Name: {father_name}")
print(f"Locality: {locality}")
print(f"Date of Birth: {date_of_birth}")
print(f"Age: {age} years old")
print(f"Nationality: {nation}")
print(f"Email: {email}")
print(f"Phone Number: {phone_number}")
