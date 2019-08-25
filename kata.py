# #############
# ===== Kata exercises =====
# #############

# #############
# Take in a number and return that number 
# as a list in reversed order
# #############
def digitize(n):

    # num_str = str(n)
    # num_split = num_str.split()

    n = [int(x) for x in str(n)]
    n.reverse()

# digitize(1234)

# #############
# # Given an array of ints, return new array 
# # with each value doubled (not squared!)
# #############

def square_me(n):
    return n*n

def maps_squared(a):
    result = map(square_me, a)
    print(list(result))

def maps_doubled(a):
    test = map(a+a, a)
    print(list(test))

# # maps_squared([1, 4, 9])
# # maps_doubled([1, 4, 9])

# #############
# # Enumerate practice
# #############
def enumerate_seasons(seasons):
    new_format = list(enumerate(seasons))

    print(new_format)
    print(new_format[0][1])

enumerate_seasons(['Spring', 'Summer', 'Fall', "Winter"])

# #############
# *** FizzBuzzZZZzzzZz *** #
# #############
# i = 1
# while (i <= 100):    
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)
#     i += 1
##############


# #############
# # min & max
# for any list of numbers, return the min and max values
# #############
def min_max(lst):
    print([min(lst), max(lst)])

# min_max([1, 2, 88, 32])
