# Multiplication using recursion
def mult(a,b):
    if b is 1:
        return a
    else:
        return a+mult(a,b-1)

# Factorials using recursion
def factorial(a):
    if a is 1:
        return 1
    else:
        return a*factorial(a-1)

# Fibonacci
def fibonacci(n):
    if n is 1 or n is 0:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


# Identifying palindromes using recursion
def ispalindrome(str):
    actual_str = ""
    for i in str:
        if i.isalpha():
            actual_str += i
    new_str = actual_str.lower()

    if len(new_str)==1 or len(new_str)==0:
        return True
    if new_str[0] == new_str[-1] and ispalindrome(new_str[1:-1]):
        return True
    return False

# Using dictionary to identify lyrics





# print(mult(4,56))
# print(factorial(6))
# print(fibonacci(4))

string= "Eva, can I see bees in a cave?"
print(ispalindrome(string))
