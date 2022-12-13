# Define the function to convert different base-systems to the decimal number system
def toDec(base: int, number):
    
    # Define input variable
    input = str(number)

    # Value of digit if not a numeral (0 to 9)
    digitValue = 0

    # Index of the input to check
    inputIndex = -1
    # Final Ouput
    inputToDec = 0
    
    # Value to add to inputToDec based on what part of the input it is looking at
    addToDec = 1

    # List of all base11 to base36 specific digits
    base11toBase36Digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Loop to check every character in the input number
    for _ in range(len(number)):
        # Trying to just convert using int() statements, which raises exceptions if character is specfic to base11 or above
        try:
            int(input[inputIndex])
            inputToDec += addToDec * int(input[inputIndex])
            addToDec *= base
            inputIndex -= 1
            return inputToDec
        # Run this if character is not a number, and is a letter
        except ValueError:
            # Check if the minimum base the digit is available in is larger than the inputed base and print a 'BaseError' message if so
            if (base11toBase36Digits.index(input[inputIndex])+11) > base:
                print("\nBaseError: the digit \'%s\' is not available in base-%d" % (input[inputIndex], base))
                inputToDec = ""
            # Check if the digit is in the list of digits and run this if so
            elif input[inputIndex] in base11toBase36Digits:
                digitValue = 10 + base11toBase36Digits.index(input[inputIndex])
                inputToDec += addToDec * digitValue
                inputIndex -= 1
                addToDec *= base
                return inputToDec
            # Check if the character is specific to a base above base36 and print a 'BaseError' message if so
            elif input[inputIndex] not in base11toBase36Digits:
                print("\nBaseError: no support for bases above 36")
                inputToDec = ""
    return inputToDec
