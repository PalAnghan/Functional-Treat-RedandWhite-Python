from array import *

print("Welcome to the Data Analyzer and Transformer Program\n")# welcome messaage print


user = [] # Create an empty list to store user data.

def input_data():
    """This function takes array input from the user."""
    print(input_data.__doc__)
    
    global user # Use the global keyword to access the user list inside the function.
    
    user = list(map(int,input("\nEnter data for 1D array (separated by space): \n").split())) # Get input from the user.

    print("\nData has been stored successfully!\n")


def display_data(*args):
    """This function displays dataset summary."""
    print(display_data.__doc__)

    print("\nData Summary:\n")

    total_elements = len(user)# Calculate the total number of elements using len().
    print(f"- Total elements: {total_elements}")

    min_value = min(user) #  Find the minimum value using min().
    print(f"- Minimum value: {min_value}")

    max_value = max(user) # Find the maximum value using max().
    print(f"- Maximum value: {max_value}")

    sum_values = sum(user) # Calculate the sum of all values using sum().
    print(f"- Sum of all values: {sum_values}")

    avg_value = sum_values/len(user)# Calculate the average by dividing the total sum by the number of elements.
    print(f"- Average value: {avg_value}\n")


def factorial_data(n):
    """This function calculates factorial using recursion."""
    print(factorial_data.__doc__)
    
    if n<=1:
        return 1
    else:
        return n * factorial_data(n-1)

def filter_data():
     """This function filters data using lambda."""
     print(filter_data.__doc__)
     
     threshold_value = int(input("Enter a threshold value to filter out data above this value: \n")) # Get the threshold value from the user.

     check = lambda x: x >= threshold_value # Lambda function to check whether a value meets the condition.
     filtered_data = list(filter(check, user))# Filter the data using the filter() function.

     print(f"\nFiltered Data (values >= {threshold_value}):")
     for i in range(len(filtered_data)):
         if i == len(filtered_data) - 1:
            print(filtered_data[i])
         else:
             print(filtered_data[i], end=", ")
    
def sort_data():
     """This function sorts data."""
     print(sort_data.__doc__)
     
     print("Choose sorting option:\n1. Ascending\n2. Descending\n")

     choice = int(input("Enter Your Choice: "))

     if choice == 1 :
         sorted_data = sorted(user)
         print("Sorted Data in Ascending Order: \n")
        
         for i in range(len(user)):
             if i == len(user) - 1:
                 print(sorted_data[i])
             else:
                 print(sorted_data[i], end=", ")
        
     elif choice ==2:
         sorted_data = sorted(user,reverse=True)
         print("Sorted Data in Descending Order: \n")
        
         for i in range(len(user)):
             if i == len(user) - 1:
                print(sorted_data[i])
             else:
                print(sorted_data[i], end=", ")

def display_dataset_statistics(**kwargs):
    """This function returns dataset statistics."""
    print(display_dataset_statistics.__doc__)

    print("\nDataset Statistics:\n")

    for key, value in kwargs.items():
        print(f"- {key}: {value}")

    #return min_value, max_value, sum_values, avg_value
 

while True:

    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))

    match choice:

        case 1:
            input_data()
        
        case 2:
            display_data(*user)

        case 3:
            num = int(input("\nEnter a number to calculate its factorial: "))
            answer = factorial_data(num)
            print(f"\nFactorial of {num} is: {answer}\n")
            
        case 4:
            filter_data()

        case 5:
            sort_data()
            
        case 6:
            display_dataset_statistics(
                Minimum=min(user),
                Maximum=max(user),
                Sum=sum(user),
                Average=sum(user) / len(user)
            )
        case 7:
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye! ")
            break
        case _:
             print("\nInvalid input. Please choose an option from 1 to 7.\n")
                
            


    
