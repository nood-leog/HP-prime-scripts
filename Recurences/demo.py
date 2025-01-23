# demo.py
# file designed to test python code on hp-prime calculator

# a program that takes an input string and repeats it 5 times then waits for a new string

# function to repeat string 5 times
def repeat_string(string):
    # repeat string 5 times
    for i in range(5):
        print(string)

# driver code to keep program running until user exits with "ex"
while True:
    string = input("Enter a string: ")
    if string == "ex":
        print("Exiting program")
        break
    repeat_string(string)

