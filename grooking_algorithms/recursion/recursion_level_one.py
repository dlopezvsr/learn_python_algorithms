# Key points: base case (the one that stops the loop), and recursion case (actual loop that executes the function)
# The call stack is where the execution of every function is saved for later use
def get_factorial(x):
    if x == 1:  # This is the base case where the validation is applied to avoid infinite loops
        return 1  # In case the condition is met, the last value will be returned
    return x * get_factorial(x-1)  # Thi is the recursion case where the function calls itself


print(get_factorial(5))
