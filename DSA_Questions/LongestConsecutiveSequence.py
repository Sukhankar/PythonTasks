def longest_consecutive(nums: list) -> int:
    if not nums:
        return 0 

    num_set = set(nums) 
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set: 
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
           
            max_length = max(max_length, current_length)
    
    return max_length

try:
    user_input = input("Enter a list of integers separated by spaces: ").strip()
    
    if not user_input:  
        print("Invalid input. Please enter at least one integer.")
    else:
        nums = list(map(int, user_input.split()))
        result = longest_consecutive(nums)
        print(f"The length of the longest consecutive sequence is: {result}")

except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
