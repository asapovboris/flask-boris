def check_id_valid(id_number):
    """
    function check if the given number is a valid ID number
    boolean , return True if valid or False if not
    """
    try:
        digits = [int(d) for d in str(id_number)]   # Convert the given number to list of digits
    except ValueError:
        return 0
    for index, digit in enumerate(digits):      # Iterate over the list and saving the index
        if index % 2 == 1:                      # check if index is not equal and multiple the digit by two
            if digit*2 > 9:                     # if multiple is bigger than two digits , sum the digits
                digits[index] = sum(int(x) for x in str(digits[index]*2))
            else:
                digits[index] = digits[index]*2

    return sum(digits) % 10 == 0                # return boolean for valid ID number

def id_generator(start):
    """
    function to generate next 10 vaild ID using generator
    """
    start += 1                                  # start from next number
    stop = 0                                    # configure an index
    while stop < 10 and start <= 999999999:     # stop when index is 10 or number is 999999999
        if check_id_valid(start):               # if the number in valid ID yield
            yield start
            stop += 1                           # add +1 to the index
        start += 1                              # next number

def check_input(ID):
    """
    function to check for valid input from the user
    """
    if len(str(ID)) != 9:       # check if number is 9 digits
        return 'not 9 digits'
    try:
        int(ID)
    except ValueError:          # check if number is a number
        return "not a number"

    return False                 # return False if valid input
