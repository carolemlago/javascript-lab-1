"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
       print(item)
  


def get_all_evens(nums):
    even_nums_list = []

    for num in nums:
        if num % 2 == 0:
            even_nums_list.append(num)
  
    return even_nums_list

def get_odd_indices(items):
    result = []

    for i in enumerate(items):
        if i % 2 != 0:
            result.append(i)
  
    return result


def print_as_numbered_list(items):
    i = 1
    
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    nums = []
    for num in range (start,stop):
        nums.append(num)

    return nums


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter == ("aeiou"):
            chars.append('*')
        else:
            chars.append(letter)
  
    return chars.join('')


def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper())
        camel_case.append(word[1:])


    return "".join(camel_case)

def longest_word_length(words):
    longest = len(words[0])


    for i in words:
        if len(i) > longest:
            longest = len(i)
           
    return longest

def truncate(string):
    result = set(string)

    result = "".join(dict.fromkeys(result))
  
    return result




def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(": 
            parens += 1
        elif char == ")":
            parens -= 1

            if parens < 0:
                return True
            else:
                return False

return parens == 0               
  
    


def compress(string):
    pass  # TODO: replace this line with your code
