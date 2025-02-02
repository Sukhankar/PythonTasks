def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False  
        else:
            
            stack.append(char)
    
    return not stack  


user_input = input("Enter a string of parentheses (e.g., (), {}, []): ").strip()

if all(c in "(){}[]" for c in user_input):
    result = is_valid(user_input)
    print(f"Is the string valid? {result}")
else:
    print("Invalid input. Please enter only parentheses: (), {}, [].")
