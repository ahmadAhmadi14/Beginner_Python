def function_name():
    print("This is function name")
function_name()

def addition(number_1, number_2):
    addnumber = number_1 + number_2
    print(f"{number_1} + {number_2} = {addnumber}")

addition(3,4)

# this is return function. input --> function ---> output
def multiple(number_3, number_4):
    result = number_3 * number_4
    return result    
print(multiple(8,7))


def multiple(number_3, number_4):
    result = number_3 * number_4
    return result
result_multiple = multiple(8, 7)    
print(result_multiple)


