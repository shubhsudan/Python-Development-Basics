def vowel_counter(string):
    """Counts the vowels in a given string"""
    vowel_count = 0
    #Iterate over a given string
    for char in string:
        if char in 'aeiou':
            vowel_count += 1
    
    return vowel_count

def word_counter(sentence):
    """Counts the words in a given sentence"""
    #Lets remove whitespace from sentence
    sentence = sentence.strip()
    
    space_count = 0
    for char in sentence:
        if char in ' ':
            space_count += 1
    word_count = space_count + 1
    
    return word_count


            
def main():
    while 1 == 1:
        input_string = input("Enter a string: ")
        
        if input_string == '-1':
            break
        
        print(vowel_counter(input_string), "vowels in",input_string)
        print(word_counter(input_string),"words in",input_string)
        
if __name__ == "__main__":
    main()
    
        
        