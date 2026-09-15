# While loop example

while True:
		string = input("Enter a string: ")
		print(string)



# 2nd Code 

correct_pass = "Some_pass"
not_found = True

while not_found:
    user_pass = input("Enter the password: ")
    if user_pass == correct_pass:
        print("Access granted")
        not_found = False

print("Password Matched!")   

# 3rd Code - table of numbers

i = 1
num = int(input("Enter a number to print its table: "))
while i <= 10: 
        print(num * i)
        i += 1


# 4th Code - Break statement example

correct_pass = "Some_pass"
not_found = True

while not_found:
    user_pass = input("Enter the password: ")
    if user_pass == correct_pass:
        break


# 5th Code - Buggy code - infinite loop

i = 0
while i < 10:
       if i == 5:
           continue
       print(i)
       i += 1

# Solution: 
i = 0
while i < 10:
       if i == 5:
           i += 1
           continue
       print(i)
       i += 1
       

