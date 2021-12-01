#!python3
'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5
'''

def find(a):
    filename = "task02.csv"
    list1 = []
    count = 0 
    for i in filename:
        if a in i:
            x = i.strip()
            data = x.split(",")
            list1.append(data)
            count + count + 1
    return count





if __name__ == "__main__":
    assert find('apple') == 0
    assert find('fish') == 5