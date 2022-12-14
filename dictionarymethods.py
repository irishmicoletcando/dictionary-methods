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
def mainProgram():
  while True:
    personal_data = {
      "person1" : {
        "Full Name" : "Irish Micole Cando",
        "Age" : 20,
        "Address" : "85 Interior Derupa St. Maysan, Valenzuela City",
        "Gender": "Female",
        "Phonenumber" : "09454678505",
        "Email" : "irishmicolecando@gmail.com",
        "Fully Vaccinated": "Yes",
        "Booster": "Yes",
        "Booster Number": "1st"
      },
      "person2" : {
      }
    }

    # validating the user's input is its from 1 to 3
    while True:
      try:
        # ask user to select an item in the menu
        userChoiceMenuInput = int(input("What do you want to do? (1-3): "))
        # if the input of the user is not from 1 to 3
        if userChoiceMenuInput not in range(0, 4):
          print("Invalid! Please enter 1 to 3 only.")
      # if the user inputted a letter
      except ValueError:
        print("Invalid! Please enter a number only.")
      else:
        break
      
    # if 1
    # if user choose 1, add the item on the dictionary 
    if userChoiceMenuInput == 1:
      # ask user for input and adding in dictionary variable
      # personal_data["person2"] = {}
      # ask user for full name
      fullName = input("Enter your full name: ")
      personal_data["person2"]["Full Name"] = fullName
      # ask user for age
      age = int(input("Enter your age: "))
      personal_data["person2"]["Age"] = age
      # ask user for address
      address = input("Enter your address: ")
      personal_data["person2"]["Address"] = address
      # ask gender
      gender = input("Enter your gender: ")
      personal_data["person2"]["Gender"] = gender 
      # ask phone number
      phonenumber = input("Enter your phone number: ")
      personal_data["person2"]["Phone Number"] = phonenumber
      # ask email
      email = input("Enter your email: ")
      personal_data["person2"]["Email"] = email 
      # ask if fully vaccinated
      fullyvaccinated = input("Are you fully vaccinated? (Yes/No): ").lower()
      personal_data["person2"]["Fully Vaccinated"] = fullyvaccinated 
      # ask if they have booster
      if fullyvaccinated == "yes":
        booster = input("Do you have a booster? (Yes/No): ").lower()
        personal_data["person2"]["Booster"] = booster
        # if yes, ask how many 1st or 2nd
        if booster == "yes":
          boosternumber = input("Do you have 1st or 2nd booster?: ")
          personal_data["person2"]["Booster Number"] = boosternumber
      # print saved if added
      print("Information saved!")

    # if 2, check if the name is in the dictionary list
    if userChoiceMenuInput == 2:
      fullNameOptionTwo = input("Enter your full name: ")
      if fullNameOptionTwo in personal_data["person1"]["Full Name"] or personal_data["person2"]["Full Name"]:
        for person, information in personal_data["person1"].items() or personal_data["person2"].items():
          print(f"{person} : {information}")
      else:
        print("No record saved!")
    
    # if 3, exit or retry program
    if userChoiceMenuInput == 3:
      while True:
        # ask the user if they want to exit or retry
        exitInput = input("Do you want to exit? (Y/N): ").lower()
        # if retry display the menu of options and have the user selct an item in menu
        if exitInput == "n":
          mainProgram()
        # if exit, exit the program
        elif exitInput == "y": 
          print("-------------------------------\nThank you!")
          exit()


# display menu of options
print("""
  Menu:
    1 -> Add an item
    2 -> Search
    3 -> Exit (y/n)
""")

mainProgram()