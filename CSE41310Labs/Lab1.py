#  Python II - Lab 1 - Silvia Maria Lorenzo

#  Part 1 (includes all extra credit)
def palindrome_scan(string2):
    length = len(string2)
    first = 0
    last = length-1
    status = 1
    while(first < last):
        if(string2[first] == string2[last]):
            first = first+1
            last = last-1
        else:
            status = 0
            break
    return int(status)


string = input("Enter a string:  ")
print("Is '" + string + "' a palindrome?")
# Extra Credit: Case insensitive and sentence-long palindromes
stringxcredit = ''.join(string.split()).lower()
status = palindrome_scan(stringxcredit)
if(status):
    print("True")
else:
    print("False")

#  Part 2 (includes all extra credit)
password = input("Enter a password: ")
n = len(password)

hasUpper = False
hasLower = False
hasDigit = False
hasSymbols = False

for i in range(n):
    if password[i].isupper():
        hasUpper = True
    if password[i].islower():
        hasLower = True
    if password[i].isdigit():
        hasDigit = True
    if password[i] in "!@#$%^&*":
        hasSymbols = True

strength = 0
if hasUpper is True:
    strength += 1
if hasLower is True:
    strength += 1
if hasDigit is True:
    strength += 1
if hasSymbols is True:
    strength += 1
if len(password) == 8:
    strength += 1
# Extra Credit: Password length additional points
if len(password) > 8 and len(password) < 16:
    strength += 2
if len(password) >= 16:
    strength += 3
print("Your password score is: " + str(strength))

#  Part 3
principal = float(input("Enter the principal amount (ex: 10000.00): "))
apr = float(input("Enter the interest rate percentage (ex: 4.5): "))
term = int(input("Enter term in years (ex: 10): "))

print(f"{'Year': >3}{'Interest': >15}{'Balance':>15}")
print("==================================")
for n in range(term):
    total = principal * (1 + apr/100.0) ** (n+1)
    interest = (principal * (1 + apr/100.0) ** n) * (apr/100.0)
    print(f"{n+1:>4}{'$':>3}{interest:>12,.2f}{'$':>3}{total:>12,.2f}")
