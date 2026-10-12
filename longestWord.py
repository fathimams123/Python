def longestWord(words_list):     
    if not words_list:
        return 0
        
    max_length = len(words_list[0]) 
    for item in words_list:         
        length = len(item)         
        if length > max_length:             
            max_length = length     
    return max_length 

user_input = input("Enter a list of words separated by spaces: ") 
word_tokens = user_input.split() 

result = longestWord(word_tokens) 
print(f"The length of the longest word is {result}")
