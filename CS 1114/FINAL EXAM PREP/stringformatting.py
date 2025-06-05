# 1. Insert Variables into Strings using f-strings
# Write an f-string that prints the following sentence using variables:
first_name = "Alice"
last_name = "Smith"
age = 30

print(f'My name is {first_name} {last_name} and I am {age} years old')
print("My name is {0} {1} and I am {2} years old".format(first_name,last_name,age))
# Output:
# "My name is Alice Smith and I am 30 years old."


# 2. Format Numbers with Decimal Precision using f-strings
# Given:
number = 3.1415926535
print(f'{number:.3f}')
# Use an f-string to print the number with 3 decimal places.
# Output:
# "3.142"


# 3. Align Text using the format() method
# Format the following variables to output text aligned to the left, right, and center:
word1 = "apple"
word2 = "banana"
word3 = "cherry"
print(f'{word1:<8}')
print(f'{word2:>8}')
print(f'{word3:^8}')
# Output (with spaces added for clarity):
# 'apple '
# ' banana'
# ' cherry '

# 4. Display a Percentage using f-strings
# Given:
score = 85
total = 100
print(f'{score/total:.0%}')


# Print the score as a percentage using f-strings, including the percent symbol.
# Output:
# "85%"


# 5. Dynamic Width Formatting using the format() method
# Given:
num1 = 12
num2 = 345
num3 = 6789
print("{0:>6}".format(num1))
print("{0:>6}".format(num2))
print("{0:>6}".format(num3))
# Use the format() method to ensure each number takes up 6 characters, aligned to the right.
# Output:
# 12
# 345
# 6789

# 6. Pad Numbers with Leading Zeros using f-strings
# Given:
number = 42
# Use an f-string to print the number padded with leading zeros, making the total length 5 digits.
# Output:
# "00042"
print(f"{number:0>5}")

# 7. Combine f-strings and Expressions
# Given:
length = 5
width = 10
# Use an f-string to print the area of a rectangle (length × width).
# Output:
# "The area of the rectangle is 50."
print(f'The area of the rectangle is {length * width}')

# 8. Right-align Strings using f-strings
# Given:
name = "Tom"
# Use an f-string to print the name right-aligned within 10 characters.
# Output:
# " Tom"
print("{0:>10}".format(name))

# 9. Format Floats using the format() method
# Given:
pi = 3.14159
# Use the format() method to print the value of pi with 2 decimal places.
# Output:
# "3.14"
print("{0:.2f}".format(pi))


# 10. Insert Variables with Specific Width using f-strings
# Given:
age = 25
name = "John"
# Use an f-string to print the following sentence, ensuring the name takes up at least 10
# characters (left-aligned):
# "John is 25 years old."
# Output:
# "John is 25 years old."
print(f"{name:<10} is {age} years old.")

# 11. Format and Display Salary Details
# You are given the following variables:
employee_name = "Jane Doe"
monthly_salary = 3500.456
months_worked = 12
bonus = 500
total_salary = monthly_salary * months_worked + bonus
# Use f-strings to display the salary details in the following format:
# ○ The employee’s name should be left-aligned within 15 characters.
# ○ The monthly salary should be printed with 2 decimal places.
# ○ The total salary should also be displayed with 2 decimal places, after applying the
# bonus.
# Example Output:
# Employee: Jane Doe
# Monthly Salary: $3500.46
# Total Salary (including bonus): $42505.47

print(f"Employee: {employee_name:>15}")
print(f"Monthly Salary: {monthly_salary:.2f}")
print(f"Total Salary (including bonus): {total_salary:.2f}")



# 12. Display Product Price with Taxes
# You are given the following variables:
# product_name = "Smartphone"
# price_before_tax = 799.99
# tax_rate = 0.075 # 7.5% tax rate
# tax_amount = price_before_tax * tax_rate
# final_price = price_before_tax + tax_amount
# Use f-strings to print:
# ○ The product name left-aligned within 20 characters.
# ○ The price before tax and the final price (after tax) formatted with 2 decimal places.
# ○ The tax amount formatted with 3 decimal places.
# Example Output:
# Product: Smartphone
# Price Before Tax: $799.99
# Tax Amount (7.5%): $59.999
# Final Price: $859.99