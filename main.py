# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
name = input( "enter name : ")
age = input("Enter your age : ")
remainder =math.fmod((int(age)*3), 2)
#remainder = int(age)*3 % 2
#str(remainder)

print('My name is: '+ name + ' and my age is: ' +age + ' remainder is: ' + str(remainder) )

