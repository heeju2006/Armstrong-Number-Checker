n = int(input("Enter a number: "))

digits = str(n)
power = len(digits)
total = 0

for d in digits:
    total += int(d) ** power

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

print("\n--- Armstrong Numbers in a Range ---")

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    if total == num:
        print(num)
