# sys import is for exceeding the recursion limit, default limit is  998
import sys

# setting recursion limit to 1500

sys.setrecursionlimit(1500)

# importing time module for the checking the time of execution of the program
import time

start_time = time.time()

number = int(input("Enter the Number for factorial"))

def large_fact(number):
	if number == 0 or number ==1:
		return 1
	else:
		return number * large_fact(number-1)


print(large_fact(number))

end_time = time.time()
execution_time = end_time - start_time
# mac or linux user run $time python large_fact.py command in the terminal to see the actual execution time
# Windows user uncomment the following line to know the execution time of the code. 
#print ("Execution time of the code :", execution_time)


