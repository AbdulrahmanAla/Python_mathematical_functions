###########################################################################################################################################
##
## Source Code
##
## Computer Project #4 design and testing of a Python program to calculate and display the values of mathematical functions
##
## defined a function for each of the mathematical values and calculate it using formulas given in the PDF  0
##   
## create a function named main which will print a menu and with different options of what mathmetical function they want to calculate 
##
## if the user eneters any letter other than the specified ones, it would print an error statment and ask them to enter a letter again
##
###########################################################################################################################################



import math
EPSILON = 0.0000001 

MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''
# create a factorial function that calculate the factorial of a given number
def factorial(N): 
    ''' Docstring ''' 
    total=1
    N= int(N)
    if N <0:
        return None
    for i in range(1,N+1):
        total *= i
        
    return total 
    
 
# create an e function that calculate the value of e given the mathmetical equation that was given in the pdf and round the final answer to 10 decimal places
def e(): 
    ''' Docstring ''' 
    e_value=0
    M=0
    while  (1/factorial(M)) > EPSILON:
        e_value+= 1/factorial(M)
        M+=1
    return round(e_value,10)
    
# create a pi function that calculate the value of pi given the mathmetical equation that was given in the pdf and round the final answer to 10 decimal places
def pi():
    ''' Docstring ''' 
    n=0
    pi_value=0
    while EPSILON < abs(((-1)**n) /(2*n+1)):
        pi_value += 4*(((-1)**n) /(2*n+1))
        n+=1
    
    return round(pi_value,10)

    
# create a hyperpolic sin function   that calculate the value of sinh given the mathmetical equation that was given in the pdf and round the final answer to 10 decimal places
# the function would return a value error because the value of x might be a negative number so I used try and except to skip this value 
def sinh(x): 
    ''' Docstring ''' 
    try:
        x=float(x)
    except ValueError:
        return None
    n=0
    sinh_value= 0
    term= float(x)
    while EPSILON <= math.fabs(term):
        sinh_value += term
        n+=1
        term = ((x**(2*n +1))/(factorial(2*n +1)))
    return round(sinh_value,10)
        
#create a main function that would print the menu and ask if the user want to use any of the options which is the functions that we created above
#for each of the functions it will caclulate the value of our function rounded to 10 decmial places and the value using the python built in function and display the results for each of the mathmetical functions and then calculate and display the difference between the two
def main(): 
    print(MENU) 
    letter= input("\nChoose an option: ")
    original_letter= letter
    letter = letter.lower()
    while letter != "x":
        
        if letter == "f":
            print("\nFactorial")
            N= input("Input non-negative integer N: ")
            if N.isdigit() == True:
                N= int(N)
                print("\nCalculated:", (factorial(N)))
                print("Math:", math.factorial(N))
                print("Diff:", (int(math.fabs( math.factorial(N)- factorial(N)))))
            else:
                print("\nInvalid N.")
        elif letter == "e":

            print("\ne")
            print("Calculated:",e())
            print("Math:",round(math.e,10))
            print("Diff: {0:.10f}".format(math.fabs((math.e-(e())))))
            
        elif letter == "p":
            print("\npi")
            print("Calculated:",pi())
            print("Math:",round(math.pi,10))
            print("Diff: {0:.10f}".format(math.fabs((math.pi-(pi())))))


        elif letter =="s":
            print("\nsinh")
            x= input("X in radians: ")
            if "." in x:

                x= float(x)
                print("\nCalculated:",sinh(x))
                print("Math:",round(math.sinh(x),10))
                print("Diff: {0:.10f}".format(math.fabs((math.sinh(x)-(sinh(x))))))
            elif x.isdigit() == True:
                x= int(x)
                print("\nCalculated:",sinh(x))
                print("Math:",round(math.sinh(x),10))
                print("Diff: {0:.10f}".format(math.fabs((math.sinh(x)-(sinh(x))))))

            else:
                print("\nInvalid X.")
                

        elif letter == "m":
            print(MENU)
        # if the user enter any other value it would print this message
        else:
            print("\nInvalid option:",letter.upper())
            print(MENU)
            

            
        letter= input("\nChoose an option: ")
        original_letter= letter
        letter = letter.lower()
    print("\nThank you for playing.")

# replace with your code

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()
