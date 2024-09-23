#prompt user for two distinct integers 
num1 = 5
num2 = 20

# Ensure the integers are distinct 
if num1 == num2:
    print("The numers must be distinct")
else:
# logical comparisons using 'and'
comparison1 = (num1 > 0 and num2 > 0)
comparison2 = (num1 % 2 == 0 and num2 % 2 == 0)

# logical comprisons using 'or'
comparison3 = (num1 < 0 or num2 < 0)
comparison4 = (num1 % 5 == 0 or num2 % 5 == 0)

# logical comparisons using 'not'
comparison5 = not (num1 == num2)
comparison6 = not (num1 < 10 and num2 < 10)

# display results 
print(f"\n logical comparisons:\n")
print(f"1. Is num1 > o and num2 > 0? : {comparison1}")
print(f"2. Is num1 even and num2 even? : {comparison2}")
print(f"3. is num1 < 0 or num2 < 0? : {comparison3}")
print(f"4. is num1 divisible by 5 or num2 divisible by 5? : {comparison4}")
print(f"5. Are num1 and num2 distinct? (not num 1 == num2) : {comparison5})")
print(f"6. Are both num1 and num2 less than 20? (not (num1 < 10 and num2 < 10)) ")