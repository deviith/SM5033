
def palindrome(string):    # Defined Function to check if string is palindrome or not

    # Here the string and its reversed string is compared if equal then return True otherwise False
    # Here Slicing concept is used, The entire string is reversed by putting [ : : -1]
    if string == string[::-1]:
        return True
    else:
        return False


s = "aabbaa"
print(palindrome(s))  # Function is called by providing input string

s = "abdcb"
print(palindrome(s))  # Function is called by providing input string
