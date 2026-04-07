import re

# Read input file
with open("input.txt", "r") as file:
    data = file.read()

# Find email addresses using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", data)

# Save emails to output file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted and saved to emails.txt")
