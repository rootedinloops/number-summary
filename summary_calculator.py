#start a loop that runs until a user inputs 0
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
tot = 0
pos = 0
neg = 0

while True:
    
    num = int(input("Number: "))

    if num == 0:
        break

    if num != 0:
        count = count + 1 
        tot += num
        mid = tot / count
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {tot}")
print(f"The mean of the numbers is {mid}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")
