# Validate user input
while True:
    function_amount = int(input("Input the amount of equations would you like to evaluate (1 - 3): "))
    if 1 <= function_amount <= 3:
        break
    print("try again")

while True:
    var_amount = int(input("Input the amount of variables you want to use (2 - 4): "))
    # If it's a number, make sure it's in the acceptable range
    if 2 <= var_amount <= 4:
        break
    print("try again")

print()

# Instruct user on acceptable variable names given the number they chose
if var_amount == 2:
    print('You have chosen to use two variables, use only the variable names a and b in your equation')
elif var_amount == 3:
    print('You have chosen to use three variables, use only the variable names a, b and c in your equation')
else:
    print('You have chosen to use four variables, use only the variable names a, b, c and d in your equation')

# Prompt user for up to 3 equations
function_1 = input("Enter the first equation you wish to evaluate: ")
function_2 = ""
function_3 = ""

if function_amount >= 2:
    function_2 = input("Enter the second equation you wish to evaluate: ")
if function_amount >= 3:
    function_3 = input("Enter the third equation you wish to evaluate: ")
print()

# Display function definitions to reference with output columns
print('out_1 = ', function_1)
if function_amount >= 2:
    print('out_2 = ', function_2)
if function_amount >= 3:
    print('out_3 = ', function_3)
print()

# set baseline for all while loops
count = 0

if var_amount == 2:

    # Display header
    print('a   b | out_1', end=' ')
    if function_amount >= 2:
        print('out_2', end=' ')
    if function_amount >= 3:
        print('out_3', end=' ')
    print()

    # Loop for values of a and b in truth table format
    while count < 2 ** var_amount:
        # Cover every combination of a and b, a flips halfway through and b flips every time
        if count < 2 ** (var_amount - 1):
            a = 1
        else:
            a = 0
        if count % 2 == 0:
            b = 1
        else:
            b = 0

        # Print results from this arrangement of variables then iterate count variable.
        print(a, ' ', b, '   ', int(eval(function_1)),  end='     ')
        if function_amount >= 2:
            print(int(eval(function_2)), end='     ')
        if function_amount >= 3:
            print(int(eval(function_3)), end=' ')
        print()

        count += 1

elif var_amount == 3:
    # Display header
    print('a   b   c | out_1', end=' ')
    if function_amount >= 2:
        print('out_2', end=' ')
    if function_amount >= 3:
        print('out_3', end=' ')
    print('')

    # set up some variables to flip-flop the value of b in truth table format
    b = 0
    parity_b = 1

    while count < 2 ** var_amount:
        # Cover every combination of a, b and c

        # a flips halfway through
        if count < 2 ** (var_amount - 1):
            a = 1
        else:
            a = 0
        # b flips every 2 times
        if count % 2 == 0:
            b += parity_b
            parity_b = parity_b * -1
        # c flips every time
        if count % 2 == 0:
            c = 1
        else:
            c = 0
        # Print the values of the variables and the results from the function, so they line up with the template
        print(a, ' ', b, ' ', c, '   ', int(eval(function_1)),  end='     ')
        if function_amount >= 2:
            print(int(eval(function_2)), end='     ')
        if function_amount >= 3:
            print(int(eval(function_3)), end=' ')
        print()
        count += 1
else:
    # Display header
    print('a   b   c   d | out_1', end=' ')
    if function_amount >= 2:
        print('out_2', end=' ')
    if function_amount >= 3:
        print('out_3', end=' ')
    print('')

    # b and c will flip every second and fourth count, keep track of parities individually
    b = 0
    parity_b = 1
    c = 0
    parity_c = 1

    while count < 2 ** var_amount:
        # a flips halfway through
        if count < 2 ** (var_amount - 1):
            a = 1
        else:
            a = 0
        # b flips every 4 counts
        if count % 4 == 0:
            b += parity_b
            parity_b = parity_b * -1
        # c flips every 2 counts
        if count % 2 == 0:
            c += parity_c
            parity_c = parity_c * -1
        # d flips every time
        if count % 2 == 0:
            d = 1
        else:
            d = 0

        # Print results from this arrangement of variables then iterate count variable.
        print(a, ' ', b, ' ', c, ' ', d, '   ', int(eval(function_1)),  end='     ')
        if function_amount >= 2:
            print(int(eval(function_2)), end='     ')
        if function_amount >= 3:
            print(int(eval(function_3)), end=' ')
        print()
        count += 1
