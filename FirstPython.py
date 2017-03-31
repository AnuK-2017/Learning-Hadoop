import random
import sys
import os

print("Hello World")

name="Moon"
#################################################
# Strings
# print(name)
# quote1="\"you are unique\""
# print(quote1)
# quote2='''This is beautiful
#           Enjoy.'''
# quote3='howareyou'
# quote=quote1+quote2
# print(quote)
# print("%s %s %s" %('I like the quote',quote1,quote2))
# print(quote[0:4])   # first number represents the starting position, second number represents how many characters of string needed
# print(quote[-5:5])
# print(quote[:-7])
# print(quote.capitalize()) # capitalize first letter of string
# print(quote.isalnum())
# print(quote3.isalpha()) # should be all characters, no space
# print(len(quote))
# print(quote2.replace('Enjoy','Have fun'))
# print(quote.strip())    # strip any white spaces

# convert string to list

# quote_list = quote.split(" ")
# print(quote_list)
#################################################
# lists
# ''' Example using lists
#     This is multi line comment'''
#
# fruits = ['apple','banana','pear','grapes']
# print("fruits[0]",fruits[0])
#
# # changing the item in the list
# fruits[0] = 'oranges'
# print(fruits)
#
# # using list within list
# veggies = ["carrots","cabbage","pepper"]
# new_list = [fruits,veggies]
# print(new_list)
# print((new_list[0][1]))
#
# # using append
# fruits.append('kiwi')
# print(fruits)
#
# # other list attributes
# fruits.insert(1,"pickle")
# fruits.sort()
# print(fruits)
# fruits.remove("pickle")
# del fruits[4]
# print(fruits)
#
# new_list2=fruits+veggies
# print(new_list2)
# print(len(new_list2))
# print(min(new_list2))
# print(max(new_list2))
#
# ############################################################################
# # tuples
#
# emp_id_tuple = (1, 2, 3, 4, 5)
# print(emp_id_tuple)
#
# emp_id_list = list(emp_id_tuple)
# emp_id_list.append(6)
# emp_id_tuple = tuple(emp_id_list)
#
# print(emp_id_tuple)
# print(len(emp_id_tuple),max(emp_id_tuple),min(emp_id_tuple))
# ###############################################################################
# # dictionaries
# flowers = {'pink': 'lotus',
#            'red': 'rose',
#            'white': 'lily',
#            'yellow': 'sunflower'}
# print(flowers['pink'])
# # del flowers['pink']
# print(len(flowers))
# flowers['yellow'] = 'daffodils'
# print(flowers.get('yellow'))
# print(flowers.keys())
# print(flowers.values())
# ################################################################################
# # if statements
#
# temp=80
#
# if temp > 100:
#     print('Its very hot')
# elif temp == 80 :
#     print('Its pleasant')
# else :
#     print('Its very cold')
# ##################################################################################
# # for loop
#
# for x in range(0,10):
#     print(x,'',end="")
# print('\n')  # print new line
# for y in fruits:
#     print(y)
#
# for z in [2,4,6,8,10]:
#     print(z)
#
# num_list=[[1,2,3],[10,20,30],[100,200,300]]
#
# for x in range(0,3):
#     for y in range(0,3):
#         print(num_list[x][y])
# ######################################################################################
# # functions
#
#
# def addNum(num1, num2):
#     sumnum = num1 + num2
#     return sumnum
# print(addNum(2,5))
# #################################################################################
# # reading the input from user
# print('What is your name')
# name = sys.stdin.readline()
# print(name)
#################################################################################
# file I/O
test_file = open("test.txt","wb")
print(test_file.name)
print(test_file.mode)










