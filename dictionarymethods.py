# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.


# declare dictionary of personal data
personal_data = {
  "fullname" : "Irish Micole Cando",
  "age" : 20,
  "address" : "85 Interior Derupa St. Maysan, Valenzuela City",
  "gender": "Female",
  "phonenumber" : "09454678505",
  "email" : "irishmicolecando@gmail.com",
  "fullyvaccinated": "Yes",
  "booster": "Yes",
  "boosternumber": "1st"
}

# display menu of options
print("""
  Menu:
    1 -> Add an item
    2 -> Search
    3 -> Exit (y/n)
""")

# ask user to select an item in the menu
userChoiceMenuInput = int(input("What do you want to do? (1-3): "))

# if user choose 1, add the item on the dictionary 
if userChoiceMenuInput == 1:
  # ask user for input
  # ask user for full name
  fullName = input("Enter your full name: ")
  # ask user for age
  age = int(input("Enter your age: "))
  # ask user for address
  address = input("Enter your address: ")
  # ask gender
  # ask phone number
  # ask email
  # ask if fully vaccinated
    # ask if they have booster
        # if yes, ask how many 1st or 2nd 

  # add in dictionary variable
  # print saved if added

# if 2
# check if the name is in the dictionary list
  # if yes, display all the information
  # if no, print no records found

# if 3
# ask the user if they want to exit or retry
# if exit, exit the program
# if retry display the menu of options and have the user selct an item in menu
