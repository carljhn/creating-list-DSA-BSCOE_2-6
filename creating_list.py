# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

name = input("Enter your name: ")
print("Hello,", name) 
ready = input("Press 'y' if you are ready and 'n' if not: ")
if ready == "y":

    again = "y"
    while again == "y":
        list1 = [23, 12, 5, 67, 33, 90, 24, 86, 2, 10]
        print("Welcome to my program")
        print("Here is the array: ", list1)
        print("1. Add an element") #append()
        print("2. Insert an element") #insert()
        print("3. Modify an element") #mutate/modify
        print("4. Delete an element") #pop()
        print("5. Arrange in ascending order") #sort()
        print("6. Arrange in descending order") #sort_descending
        print("7. Determine the number of an element in the array") #count()
        print("8. Obtain the sum of all the elements") #sum()
        print("9. Determine the largest value in the array") #max()
        print("10. Determine the smallest value in the array") #min()
        operation = input("Please select the number of the operation you want to perform: ")

        if operation == "1":
            print("These are the elements of the array", list1)
            element = input("What number you want to add?: ")
            list1.append(element)
            print("This is the new array: ")
            print(list1)

        elif operation == "2":
            print("These are the elements of the array", list1)
            index = input("Enter your chosen index here: ")
            element = input("What number do you want to insert?: ")
            list1.insert(int(index), int(element))
            print("This is the new array:")
            print(list1)

        elif operation == "3":
            print("These are the elements of the array", list1)
            index = input("Enter your chosen index here: ")
            element = input("What number do you want to modify?: ")
            list1[int(index)] = element
            print("This is the new array:")
            print(list1)

        elif operation == "4":
            print("These are the elements of the array", list1)
            index = input("Enter the index you want to delete: ")
            list1.pop(int(index))
            print("This is the new array:")
            print(list1)
            
        elif operation == "5":
            print("These are the elements of the array", list1)
            list1.sort()
            print("This is the new array:")
            print(list1)

        elif operation == "6":
            print("These are the elements of the array", list1)
            list1.sort(reverse=True)
            print("This is the array in descending order:")
            print(list1)

        elif operation == "7":
            print("These are the elements of the array", list1)
            element = input("Enter the value in the array that you want to count: ")
            counter = list1.count(int(element))
            print("The number of element/s is:")
            print(counter)

        elif operation == "8":
            print("These are the elements of the array", list1)
            sum = sum(list1)
            print("The sum of all the elements in the array is:")
            print(sum)

        elif operation == "9":
            print("These are the elements of the array", list1)
            max_num = max(list1)
            print("The largest number in the array is:")
            print(max_num)

        elif operation == "10":
            print("These are the elements of the array", list1)
            min_num = min(list1)
            print("The smallest number in the array is:")
            print(min_num)
        else:
            print("Invalid number, please try again")

        again = input("Do you want to test use this program again? (y/n): ")
        if again == "n":
            print("Thank you for using this program")

elif ready=="n": 
    print("Thank you for using this program")

else:
    print("Uknown input, repeat the program.")
    
