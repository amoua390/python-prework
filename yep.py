#Question 1 Write a function to print 
#"hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name + "!")
   
hello_name('USERNAME')




#Question 2
#Write a python function, first_odds 
#that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    current_number = 1
    while current_number <= 100:
            if current_number % 2 != 0: 
                print(current_number)
            current_number += 1
    
print(first_odds())




#Question 3
#Please write a Python function, max_num_in_list to return the max number of
#a given list.

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
print(max_num_in_list([0, 1, 5, 13, 22]))




#Question 4
#Write a function to return if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100, unless
#it is also divisible by 400. The return should be boolean
#Type (true/false)

def is_leap_year(a_year):
    leap = False

    if (a_year % 4 == 0) and (a_year % 100 != 0): 
        leap = True
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        leap = False
    elif (a_year % 400 == 0):
        leap = True
    else:
        leap = False

    return leap

print(is_leap_year(2018))




#Question 5
#Write an function to check if all number in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

a_list = [1, 2, 5, 6]
print(is_consecutive(a_list))