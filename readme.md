# Truth Table Generator
 
### Description
This is a simple truth table generator which uses only basic concepts such as if/else, while loops, and the eval() 
function. It was designed to be understood with concepts learned early on in any Python course and is intended to be 
used as a learning tool. The eval() function is used to evaluate boolean equations given by the user. Up to 3 equations 
can be compared, each with up to 4 variables.

### Usage

1. Run the Program.
2. Input a number corresponding to the amount of boolean equations you want to have evaluated and compared
3. input the amount of different variables you want to use in your equation(s)
4. You will be given instructions on what variable names are valid. Input each equation using only these variable names.
5. A truth table will be displayed in the console with the results of each equation for all possible True/False combinations of variables. True is represented as 1 and False 0. Each equation will correspond to an output column, allowing for easy comparison.

### Sample Outputs
Comparing similar equations
```text
out_1 =  a and b or c
out_2 =  a and (b or c)
out_3 =  (a and b) or c

a   b   c | out_1 out_2 out_3 
1   1   1     1     1     1 
1   1   0     1     1     1 
1   0   1     1     1     1 
1   0   0     0     0     0 
0   1   1     1     0     1 
0   1   0     0     0     0 
0   0   1     1     0     1 
0   0   0     0     0     0 
```
Comparing basic logic gates
```text
out_1 =  a and b
out_2 =  a or b
out_3 =  not (a and b) and (a or b) # XOR gate (one or the other but not both)

a   b | out_1 out_2 out_3
1   1     1     1     0
1   0     0     1     1
0   1     0     1     1
0   0     0     0     0
```
Boolean Multiplexor
```text
out_1 =  (not a and c) or (a and b) # MULTIPLEXOR (outputs b when a == 1, c when a == 0)

a   b   c | out_1
1   1   1     1
1   1   0     1
1   0   1     0
1   0   0     0
0   1   1     1
0   1   0     0
0   0   1     1
0   0   0     0
```