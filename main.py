'''
04/29/21
Recursion
'''

# Factorial
# 5! = 5 * 4 * 3 * 2 * 1 * 1
# 5! = 5 * 4!
#.   = 5 * 4 * 3!
#.   = 5 * 4 * 3 * 2!
#.   = 5 * 4 * 3 * 2 * 1!
#.   = 5 * 4 * 3 * 2 * 1 * 0!
#.   = 5 * 4 * 3 * 2 * 1 * 1

# 1. With a Loop
num = int(input("Enter a positive int: "))
factorial = 1

for i in range(1, num + 1):
	factorial *= i

print ("The factorial of " + str(num) + " is " + str(factorial))

# 2. With a recursive function
def factorial(n):
	if (n == 1):
		return 1
	else:
		return n * factorial(n - 1)

num = int(input("Enter a positive int: "))

print ("The factorial of " + str(num) + " is " + str(factorial(num)))



# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21,...

# 1. With A Loop