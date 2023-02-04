def get_secrets(file_name):
    """
    helper function to read in secret login details 
    
    Inputs:
        file_name - a string pointing to the secret file path and file name

    Returns a list containing secret information
    """
    # open file and read contents line by line, saving to a list
    with open(file_name, mode='r') as file:
        secrets = []
        for line in file:
            secrets.append(line.strip())
    return secrets
    

def test_get_secrets():
    """ Implements unit tests for get_secrets() """
    
    def tests(file_name):
        # call get_secrets
        secrets = get_secrets(file_name)
        # returned type is a list
        is_list = type(secrets) == type([])
        # contents are strings
        contains_strings = False
        if len(secrets) != 0:
            contains_strings = True
        for secret in secrets:
            if type(secret) != type(str()):
                contains_strings = False
        # returned length
        list_len = len(secrets)
        # no leading or trailing whitespace
        whitespace = True
        for secret in secrets:
            if secret[0].isspace() or secret[-1].isspace():
                whitespace = False
        return is_list, contains_strings, list_len, whitespace
        
    # test 1
    file_name = 'test_get_secrets1.txt'
    test1 = tests(file_name)
    print(f"Test 1: input file: {file_name}")
    print(f"\tget_secrets() returned a list? {test1[0]}")
    print(f"\tget_secrets contains only strings? {test1[1]}")
    print(f"\tExpected length of 3. Pass? {3 == test1[2]}")
    print(f"\tLeading/Trailing whitespaces stripped? {test1[3]}")
    print(f"All pass? {test1[0] and test1[1] and test1[2] and test1[3]}")