variable_x = "this is global variable x"

def testfunction():
    variable_x = "this is local variable x"
    global variable_y
    variable_y = "this is local variable y"
    print(variable_x, '\n', variable_y)

testfunction()

print(variable_x)
print(variable_y)