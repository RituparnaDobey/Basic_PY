#  Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


def stri_index(text):

    evn_txt = ""

    for i in range(0, len(text), 2):
        evn_txt += text[i]
    return evn_txt
    
usr_input = input("Write a text: ")

x = stri_index(usr_input)

print(x)

