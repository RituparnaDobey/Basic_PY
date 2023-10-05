# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.


def rmv_ltr(text, n):

    return text[n:]
      
text = input("Please enter a text: ")

n = 5

x = rmv_ltr(text, n)

print(x)




