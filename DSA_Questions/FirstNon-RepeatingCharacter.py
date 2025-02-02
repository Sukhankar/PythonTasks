def first_unique_char(s: str) -> str:
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    for char in s:
        if frequency[char] == 1:
            return char
    
    return "None" 


user_input = input("Enter a string: ").strip()  

if user_input: 
    result = first_unique_char(user_input)
    print(f"The first non-repeating character is: {result}")
else:
    print("Invalid input. Please enter a non-empty string.")
