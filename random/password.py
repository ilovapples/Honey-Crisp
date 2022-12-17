# Random Password Generation Module

# Imports neccesary modules
import random

# Defines the main password generation function
def generate(len):
    password = ""
    for _ in range(len):
        password += chr(random.randint(33, 126))
    return password

# Defines the customizable password generation function, for more specific tuning
def preciseGenerate(len, specialChrs, numbers, letters, case):
    # Declares password variable
    password = ""
    characterCheck = 0
    for _ in range(len):
        
        # Generate with special characters, numbers and letters
        if specialChrs == True and numbers == True and letters == True: 
            password += chr(random.randint(33, 126))
            
        # Generate with just numbers and letters
        elif specialChrs == False and numbers == True and letters == True: 
            characterCheck = random.randint(1, 3)
            if characterCheck == 1:
                password += chr(random.randint(48, 57))
            elif characterCheck == 2:
                password += chr(random.randint(65, 90))
            elif characterCheck ==  3:
                password += chr(random.randint(97, 122))
                
        # Generate with just letters
        elif specialChrs == False and numbers == False and letters == True: 
            characterCheck = random.randint(1, 2)
            if characterCheck == 1:
                password += chr(random.randint(65, 90))
            elif characterCheck == 2:
                password += chr(random.randint(97, 122))
                
        # Generate with no characters
        elif specialChrs == False and numbers == False and letters == False: 
            password = ""
            
        # Generate with just special characters
        elif specialChrs == True and numbers == False and letters == False: 
            characterCheck = random.randint(1, 4)
            if characterCheck == 1:
                password += chr(random.randint(33, 47))
            elif characterCheck == 2:
                password += chr(random.randint(58, 64))
            elif characterCheck == 3:
                password += chr(random.randint(91, 96))
            elif characterCheck == 4:
                password += chr(random.randint(123, 126))
        
        # Generate with just numbers
        elif specialChrs == False and numbers == True and letters == False: 
            password += chr(random.randint(48, 57))

        # Generate with just special characters and numbers
        elif specialChrs == True and numbers == True and letters == False: 
            characterCheck = random.randint(1, 3)
            if characterCheck == 1:
                password += chr(random.randint(33, 64))
            elif characterCheck == 2:
                password += chr(random.randint(91, 96))
            elif characterCheck == 3:
                password += chr(random.randint(123, 126))

        # Generate with just special characters and letters
        elif specialChrs == True and numbers == False and letters == True: 
            characterCheck = random.randint(1, 2)
            if characterCheck == 1:
                password += chr(random.randint(33, 47))
            elif characterCheck == 2:
                password += chr(random.randint(58, 126))
    # Checks if the case variable is up and sets the password to uppercase
    if case.lower() == "up":
        password = password.upper()
    
    # Checks if the case variable is down and set the password to lowercase
    elif case.lower() == "down":
        password = password.lower()
    else:
    # Otherwise it does nothing to the password
        password = password
    return password
