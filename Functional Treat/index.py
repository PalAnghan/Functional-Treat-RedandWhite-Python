from array import *

print("Welcome to the Data Analyzer and Transformer Program\n") #welcome messaage print

OneDArray = array('i')# Create an array to store 1D data.
TwoDArray = [] # Create an empty list to store 2D array rows.

def input_data():
    """
    This function takes array input from the user.
    """
    print(input_data.__doc__)

    print("Option:")
    print("1 for 1D array")
    print("2 for 2D array")

    num = int(input("\nEnter your choice: "))

    global OneDArray # Use the global keyword to access the global arrays inside the function.
    global TwoDArray # Use the global keyword to access the global arrays inside the function.

    if num == 1:
        OneDArray = array('i',map(int,input("\nEnter data for 1D array (separated by spaces): \n").split()))
        TwoDArray.clear()   # Clear the previous 2D array.
        
        print("\nData stored in 1D array\n")
    elif num == 2:
        print("\nEnter data for the 2D array (enter one row per line):\n")

        TwoDArray.clear()  # Clear the previous 2D array before storing new 2D data.
       
        
        for i in range(3):
            row = array('i',map(int,input(f"{i + 1}:  ").split()))
            TwoDArray.append(row)
            

        print()
        print("Data stored in 2D array")
    else :
        print("\nPlease Enter a number between 1 and 2\n")

        return num

def display_data():
    """
    This function displays dataset summary.
    """
    print(display_data.__doc__)
    
    print("Data summary:")

    print("\n1D Array:")

    if len(OneDArray) > 0:
        print(list(OneDArray))
        print("- Total elements:", len(OneDArray))# Calculate the total number of elements using len().
        print("- Minimum value:", min(OneDArray))#  Find the minimum value using min().
        print("- Maximum value:", max(OneDArray))# Find the maximum value using max().
        print("- Sum:", sum(OneDArray))# Calculate the sum of all values using sum().
        print("- Average:", sum(OneDArray) / len(OneDArray))# Calculate the average by dividing the total sum by the number of elements.
    else:
        print("No 1D data available.")

    print("\n2D Array: ")
    for row in TwoDArray:
        print(list(row))
    
    total = 0 # Count the total number of elements in the 2D array.
    for row in TwoDArray:
        total += len(row)

    all_values = [] # Store all 2D array elements in a single list.
    for row in TwoDArray: 
        for value in row:
            all_values.append(value)
    if len(TwoDArray) > 0: 
        print("\nRows :", len(TwoDArray)) # Calculate the number of rows using len().
        print(f"- Total elements :{total}")
        print(f"- Minimum value:",min(all_values))#  Find the minimum value using min().
        print("- Maximum value:", max(all_values))# Find the maximum value using max().
        print("- Sum:", sum(all_values))# Calculate the sum of all values using sum().
        print("- Average:", sum(all_values) / len(all_values))# Calculate the average by dividing the total sum by the number of elements.
    else:
        print("No 2D data available.")
    print("\n")
    
def calculate_factorial(n):
    """
    This function calculates factorial using recursion.
    """

    if n == 0 or n == 1:
        return 1
    elif n < 0:
        print("Please enter a positive number instead of a negative number.")
        return 
    else:
        return n * calculate_factorial(n-1) 
        
def filter_data():
    """
    This function filters array elements using a lambda function.
    """
    print(filter_data.__doc__)
    global OneDArray # Access the global 1D array.
    global TwoDArray # Access the global 2D array.
    
    threshold_value = int(input("Enter a threshold value to filter out data  above this value: \n")) # Get the threshold value from the user.
    check = lambda x :x >= threshold_value # Lambda function to check whether a value meets the condition.
    
    filtered_data = list(filter(check,OneDArray))

    print(f"\nFiltered Data for 1D Array (Values >= {threshold_value}):") # Filter the 1D array using the lambda function.
    
    if len(filtered_data) == 0:
        print("No values found.")
    else:
        for i in range(len(filtered_data)): # Display the filtered values from the 1D array.
            if i == len(filtered_data) - 1:
                print(filtered_data[i])
            else:
                print(filtered_data[i], end=", ")
             
    print(f"\nFiltered Data for 2D Array (Values >= {threshold_value}):")
    for row in TwoDArray:

        filtered_row = list(filter(check, row))

        if len(filtered_row) > 0:

            for i in range(len(filtered_row)):# Filter the current row of the 2D array.
                if i == len(filtered_row) - 1:
                    print(filtered_row[i], end="")
                else:
                    print(filtered_row[i], end=", ")

            print()
    print("\n")

def sort_data():
    """
    This function sorts data.
    """
    print(sort_data.__doc__)
    global OneDArray
    global TwoDArray

    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        if len(OneDArray) > 0:
            sorted_data = sorted(OneDArray)# Sort the 1D array in ascending order.
            print("\nSorted Data for 1D Array in Ascending Order:\n")

            for i in range(len(sorted_data)):
                if i == len(sorted_data) - 1:
                    print(sorted_data[i])
                else:
                    print(sorted_data[i], end=", ")

        if len(TwoDArray) > 0:
            print("\nSorted Data for 2D Array in Ascending Order:\n")

            for row in TwoDArray:
                sorted_row = sorted(row)# Sort each row of the 2D array in ascending order.

                for i in range(len(sorted_row)):
                    if i == len(sorted_row) - 1:
                        print(sorted_row[i], end="")
                    else:
                        print(sorted_row[i], end=", ")

                print()

    elif choice == 2:

        if len(OneDArray) > 0:
            sorted_data = sorted(OneDArray, reverse=True)
            print("\nSorted Data for 1D Array in Descending Order:\n")

            for i in range(len(sorted_data)):
                if i == len(sorted_data) - 1:
                    print(sorted_data[i])
                else:
                    print(sorted_data[i], end=", ")

        if len(TwoDArray) > 0:
            print("\nSorted Data for 2D Array in Descending Order:\n")

            for row in TwoDArray:
                sorted_row = sorted(row, reverse=True)

                for i in range(len(sorted_row)):
                    if i == len(sorted_row) - 1:
                        print(sorted_row[i], end="")
                    else:
                        print(sorted_row[i], end=", ")

                print()

    else:
        print("\nPlease enter 1 or 2.")

def display_dataset(*args, **kwargs):
    """
    This function displays dataset statistics using *args and **kwargs.
    """
    print(display_dataset.__doc__)

    if len(args) > 0:
        print(args[0])

    for key, value in kwargs.items():
        print(f"{key} : {value}")

    if len(OneDArray) > 0:

        print("\n==== 1D Array Statistics ====")

        minimum = min(OneDArray)
        maximum = max(OneDArray)
        total = sum(OneDArray)
        average = total / len(OneDArray)

        print("Minimum Value :", minimum)
        print("Maximum Value :", maximum)
        print("Sum of Values :", total)
        print("Average Value :", average)

    if len(TwoDArray) > 0:

        print("\n==== 2D Array Statistics ====")

        all_values = []

        for row in TwoDArray:
            for value in row:
                all_values.append(value)

        minimum = min(all_values)
        maximum = max(all_values)
        total = sum(all_values)
        average = total / len(all_values)

        print("Minimum Value :", minimum)
        print("Maximum Value :", maximum)
        print("Sum of Values :", total)
        print("Average Value :", average)

    if len(OneDArray) == 0 and len(TwoDArray) == 0:
        print("No data available.")

while True:

    print("Menu:")
    print("1. Input Data")
    print("2. Display Data")
    print("3. Calculate Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            input_data()
        case 2:
            display_data()
        case 3:
            print(calculate_factorial.__doc__)
            find_number = int(input("Enter a number to calculate its factorial: "))
            result = calculate_factorial(find_number)
            print(f"\nFactorial of {find_number} is: {result}\n")
        case 4:
            filter_data()
        case 5:
            sort_data()
        case 6:
            display_dataset("Dataset Statistics")
            
        case 7:
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        case _:
            print("Please enter a valid choice between 1 and 7.")
                  
