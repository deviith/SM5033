
def monotonic(inp):  # Defined a function to check The array is  Monotonic or not

    # the length of array, starts from 0 to n-1
    l = len(inp) - 1

    # Check if the value is less than the next one,  similarly for all the position in array
    if all(inp[i] <= inp[i + 1] for i in range(0, l)):
        return True

    # Check if the value is greater than the next one, similarly for all the position in array
    elif all(inp[i] >= inp[i + 1] for i in range(0, l)):
        return True

    # If the above both condition does not satisfied then return False
    else:
        return False


a = [10, 8, 2, 2]
print(monotonic(a))  # calling a function by providing the given value

a = [1, 1, 2, 4]
print(monotonic(a))  # calling a function by providing the given value

a = [1, 5, 2, 7]
print(monotonic(a))  # calling a function by providing the given value
