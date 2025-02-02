def find_missing_number(arr: list) -> int:
    n = len(arr)  
    expected_sum = (n + 1) * (n + 2) // 2  
    actual_sum = sum(arr)
    return expected_sum - actual_sum


try:
    user_input = input("Enter the array of numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    
    missing_number = find_missing_number(arr)
    print(f"The missing number is: {missing_number}")
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
