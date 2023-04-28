# #!/usr/bin/env python3
# # name = "Nehad "
# # age = 20
# # print('My name {0} gtrg {1} hththth'.format(name, age))

# # x = input('Enter \n')
# # print(x.isdigit())
# # students = [10, 'ahmed', ['iti', 'bbb']]
# # students[2].append('H')
# # s = tuple(students)

# # sets = {'s','n','m'}
# # print(sets.discard('m'))
# # print(sets)

# data = {
#     'Track' : 'python',
#     'Course' : 'fvfeve',
#     '2':[1,2,3,5],
#     'result':{
#         'k':'v',
#         'k2':['v','Ref']
#     }
# }
# print(data['2'][0])


# # 1- Write a Python program which accepts the user's first and last name and print them in
# # reverse order with a space between them.

# first_name = input('Enter your first name:')
# last_name = input('Enter your last name:')
# print(last_name +' '+first_name)


# # 2- Write a Python program that accepts an integer (n) and computes the value of
# # n+nn+nnn
# n1 = int(input("Enter an integer : "))
# n2 = int( "%s%s" % (n1,n1) )
# n3 = int( "%s%s%s" % (n1,n1,n1) )
# result = n1+n2+n3
# print (result)


# # 3- Write a Python program to print the following here document.
# print("""a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example""")


# 4- Write a Python program to get the volume of a sphere with radius 6
# volume = 4/3 * 3.14 * 6.0**3
# print("Volume of the sphere is: ",volume)

# 5- Write a Python program that will accept the base and height of a triangle and compute
# the area
# base = float(input('Enter your base:'))
# height = float(input('Enter your height:'))
# area = 1/2 * base * height
# print("The area of the triangle is: ",area)

#6- Write a Python program to construct the following pattern, using a nested for loop.
# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(rows):
#     for j in range(rows-i):
#         print("*", end=" ")
#     print()

# 7- Write a Python program that accepts a word from the user and reverse it.
# word = input('Enter the word you want to reverse:')
# reverse = word[::-1]
# print(reverse)

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# for i in range(6):
#     if(i==3 or i==6):
#         continue
#     print(i,end=' ')

# 9-Write a Python program to get the Fibonacci series between 0 to 50
# x, y = 0, 1
# while y<50:
#     print(y)
#     x, y = y, x+y
	
# 10-Write a Python program that accepts a string and print how many digits an dnumbers

string = input("Enter a string:")
digits = 0
letters = 0
for i in string:
    if i.isdigit():
        digits+=1
    if i.isalpha():
        letters+=1

print("Number of digits is: " , digits)
print("Number of letters is: " , letters)