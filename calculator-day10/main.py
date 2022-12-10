from art import calculator

"""
Calculate the output with the input string for example a + b - c * d
with a b c d is integer value

Step:
1. Extract number and operator into seperated array
2. while len(number_list) > 2 continue to loop through and execute based on the operator
3. Multiply and divide first then other later
"""

print(calculator)

def divide(num1 , num2):
    return num1 / num2

def plus(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def minus(num1, num2):
    return num1 - num2



operation = {
    '+' : plus,
    '-' : minus,
    '*': multiply,
    '/': divide
}


def calculation(calc_str):
    operate_lst, num_lst = extract_calc(calc_str)
    iteration = 0
    while len(num_lst) > 1:
        calc_re = operation[operate_lst[iteration]](num_lst[0], num_lst[1])
        num_lst = num_lst[2:]
        num_lst.insert(0, calc_re)
        iteration += 1
    
    
    print(calc_re)
    
def extract_calc(calc_str):
    calc_str = calc_str.strip() # remove white space if any
    operate = []
    num = []
    num_str = ''

    for char in calc_str:
        if char in operation:
            num.append(int(num_str))
            num_str = ''
            operate.append(char)
        else:
            num_str += char
    num.append(int(num_str))
    return operate, num




if __name__ == "__main__":
    calc_sequence = input("Please input some mathematics equation: ")
    calculation(calc_sequence)