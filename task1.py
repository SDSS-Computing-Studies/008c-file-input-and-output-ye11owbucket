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
input1 = str(input("input: "))
def mayonaise(a):
    x = len(a)
    if x == 0:
        return "no bueno"
    if x > 1:
        mayo = (x + " stocks have that symbol")
        return mayo
    if x == 1:
        return a

def find(needle):
    pyf1 = "task02.csv"
    list1 = []
    count = 0 
    for haystack in pyf1:
        if needle in haystack:
            x = haystack.strip()
            data = x.split(" ")
            list1.append(data)
            count + count + 1
    mayonaise(list1)

find(input1)
            




if __name__ == "__main__":
    assert find('apple') == 0
    assert find('fish') == 5