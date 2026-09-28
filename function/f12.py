# count vowels in a string

def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
           count += 1

        return count

print(count_vowels("Hello World"))

#Reverse astring

def reverse_string(text):
    return text[::-1]
print(reverse_string("Hello"))

#Check Palindrome

def  palindrome(text):
    if text == text[::-1]:
        print("palindrome")
    else:
        print("Not Palindrome")
        
palindrome("madam")

# Sum of all elements in a list

def list_sum(numbers):
    total = 0

    for n in numbers:
        total += n
        
    return total
print(list_sum([10,20,30,40]))

# Largest element in a list

def largest(numbers):
    return max(numbers)

print(largest([10,20,30,40]))

# Remove duplicate element

def remove_duplicates(numbers):
    result = []
    for n in numbers:
       if n not in result:
           result.append(n)

    return result
print(remove_duplicates([1, 2, 3, 3, 4, 4]))

#


















