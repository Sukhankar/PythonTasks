from collections import defaultdict

def group_anagrams(words: list) -> list:
    anagrams = defaultdict(list)  
    
    for word in words:
        sorted_word = "".join(sorted(word.lower()))  
        anagrams[sorted_word].append(word)  
    
    return list(anagrams.values())  

try:
    user_input = input("Enter a list of words separated by spaces: ").strip()
    
    if not user_input:  
        print("No words entered. Please enter a list of words.")
    else:
        words = user_input.split()
        result = group_anagrams(words)
        
        print("Grouped anagrams:")
        for group in result:
            print(group)

except Exception as e:
    print(f"An error occurred: {e}")
