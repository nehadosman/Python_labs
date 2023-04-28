
#1- Given a list of numbers, create a function that returns a list where element appear once 
# def remove_duplicates(list):
#     new_list= []
#     for i in list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# list = input("Enter items separated by commas: ")
# list = list.split(",")

# new_list = remove_duplicates(list)
# print("List after remove duplicates", new_list)

#################################################################

# # 2- Consider dividing a string into two halves
# def get_combination(a, b):
#     len_of_a = len(a)
#     len_of_b = len(b)
#     a_front = a[:len_of_a // 2 + len_of_a % 2]
#     a_back = a[len_of_a // 2 + len_of_a % 2:]
#     b_front = b[:len_of_b // 2 + len_of_b % 2]
#     b_back = b[len_of_b // 2 + len_of_b % 2:]
#     return a_front + b_front + a_back + b_back

# a = "123456"
# b = "nehad"
# result = get_combination(a, b)
# print(result)

##########################################################

# # 3- Write a Python function that takes a sequence of numbers and determines
# # whether all the numbers are different from each other.
# def is_unique(numbers):
#   if len(numbers) == len(set(numbers)):
#     return True
#   else:
#     return False

# # print(is_unique([1,5,7,9]))
# # print(is_unique([2,4,5,5,7,9]))

# numbers = input("Enter list of numbers separated by commas: ")
# numbers = numbers.split(",")
# result = is_unique(numbers)
# print("Unique data? ",result)

##################################################################

# # 4- Given unordered list, sort it using algorithm bubble sort

# def bubbleSort( list ):
#     n = len( list )

#     for i in range( n - 1 ) :
#         flag = 0

#         for j in range(n - 2) :
            
#             if list[j] > list[j + 1] : 
#                 tmp = list[j]
#                 list[j] = list[j + 1]
#                 list[j + 1] = tmp
#                 flag = 1

#         if flag == 0:
#             break

#     return list

# numbers = input("Enter numbers seperated by commas: ")
# numbers = numbers.split(",")
# result = bubbleSort(numbers)

# print ("Sorted list : ",result)

###############################################################
# 5-Guesses game
import random
def guesses_game():
    answer = random.randint(1,100)
    tries = 10
    guessed_nums = set()

    while tries > 0:
        guess = input("guess a number between 0 and 100: ")
        if int(guess) > 100 or int(guess) < 0:
            print("Please enter a number between 1 and 100.")
            continue
        if int(guess) in guessed_nums:
            print("Try a different one, you guessed that before")
            continue

        guessed_nums.add(int(guess))
                
        if int(guess) == right_answer:
            print("Congratulations! You guessed the number in", 10 - tries + 1, "tries.")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                guesses_game()
            else:
                print("Thanks for playing!")
            return

        if int(guess) < right_answer:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")

        tries -= 1


    print("You used your allowed tries, The answer was", right_answer)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        guesses_game()
    else:
        print("Thanks for playing!")

guesses_game()
