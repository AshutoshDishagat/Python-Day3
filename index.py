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