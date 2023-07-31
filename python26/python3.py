def sort_words(word_string):
    # Remove white spaces from input string
    word_string = word_string.replace(" ", "")
    
    # Sort letters in the string and remove duplicates
    sorted_letters = sorted(set(word_string))
    
    # Convert sorted letters to a comma-separated string
    sorted_letters_str = ",".join(sorted_letters)
    
    # Return the comma-separated string as a list
    return [sorted_letters_str]

print(sort_words("love life"))

