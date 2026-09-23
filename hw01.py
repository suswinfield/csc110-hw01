# ------------------------------------------------------
#        Name: Susannah Winfield
#       Peers: (add any collaborators)
#  References: https://www.geeksforgeeks.org/python/python-iterate-multiple-lists-simultaneously/
#  https://www.geeksforgeeks.org/python/assigning-multiple-variables-in-one-line-in-python/

# ------------------------------------------------------


def main():
    """
    This is a Docstring for the main function. This is the short description.

    Here, after a blank line, you can add a longer paragraph description.
    Docstrings are like long comments that we put right under the function definition.
    The Docstring goes from one set of "opening" three double-quotes to
    another set of "closing" three double-quotes. We also try to keep the lines short.
    The Docstring has 4 sections:
      - the short one-line description
      - the paragraph description
      - the Params section that indicates input parameters and return values
      - the "how to run" section called "Example Use".

    PARAMS:
        - None. If the function took an input int of "apples" called num, we would
                indicate it like this: - num: int with number of apples
    RETURNS:
        - None. If the function returned something (like the integer half of num),
                we would indicate it like this: int : integer half of num
    """

    # ========== Setup for HW. DO NOT MODIFY ======
    x=0
    y=0
    a=0
    b=0
    c=0
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    result5 = 0
    # End of Setup code ---------------------------



    # Part 1: Basic Operations
    # =============================================
    # Your code for part 1 under this line and before the print statements
    #assigns variable values corresponding to the order they're listed
    numbers = [27,1,1.5,7,-1]
    x,y,a,b,c = numbers
    result = float(b+4*c)
    #need to make the variables strings so the name is printed instead of the value in the for loop
    variables_names = ["x","y","a","b","c"]
    # for loop to print variables and their corresponding values
    for v, n in zip(variables_names, numbers):
        print("Part 1:",v,"=",n)
    print("Part 1: result =",result)
    # End of Part 1 ----------------------


    # Part 2: Power
    # =============================================
    # Your code for part 2 under this line and before the print statements
    x,y = [5, -3]
    result2 = x**2*y**4
    #listing the variables to be used in the for loop
    variables2 = [x,y,result2]
    #prints Part 2 variables to values
    variables2_names = ["x","y","result"]
    for v2,v2_n in zip(variables2,variables2_names):
        print("Part 2:",v2_n,"=",v2)
    # End of Part 2 ----------------------
    # Part 3: Integer divide
    # =============================================
    # Your code for part 3 under this line and before the print statements
    a,b = [100, 13]
    result3 = a//b
    #setting up names of variables and actual values in lists to be used in the for loop
    variables3 = [a,b,result3]
    variables3_names = ["a","b","result"]
    #Print Part 3 variables to values
    for v3,v3_n in zip(variables3,variables3_names):
        print("Part 3:",v3_n,"=",v3)
    # End of Part 3 ----------------------


    # Part 4: Modulo
    # =============================================
    # Your code for part 4 under this line and before the print statements
    result4 = a%b
    #Prints result of modulo operator for Part 4
    print("Part 4: result =",result4)
    # End of Part 4 ----------------------

if __name__ == "__main__":
    main()
