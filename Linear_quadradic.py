import math 

equation = input('Which equation are you solving, linear or quadratic? ')
options1 = ["linear", "quadratic"]
if equation not in options1:
    print(' ')
    print("Chose one of the following options")
    print("linear")
    print("quadratic")
    print(' ')

    equation = input('Which equation are you solving, linear or quadradic? ')

    #part1


if equation == 'quadratic':
    print(" ")
    print("The equation for form standard is y = ax^2+bx+c and the equation form for intercept is y = (ax + m)(bx+n)")
    form1 = input('What form are you solving, standard, or intercept? ')
    
    options2 = ["standard", "intercept"]

    print(form1)
    if form1 not in options2:
        print(' ')
        print("Chose one of the following options")
        print("standard")
        print("intercept") 
        print(' ')

        form1 = input('What form are you solving, standard or intercept? ') 

        #part

    if form1 == 'standard':
        variable = input("Which variable are you solving for x or y ? ")

        option3 = ["x", "y"]

        if variable not in option3:
            print(' ')
            print("Choose one of the following options") 
            print('x')
            print('y')
            print(' ') 

            variable = input("Which variable are you solving for x or y ? ")

            #part
    
    

        if variable == 'y':
            a = input("What is the value of a? ")
            c = input("What is the value of c? ")
            x = input("What is the vlaue of x? ")
            b = input("What is the value of b?")

            a = int(a)
            c = int(c)
            x = int(x)
            b = int(b)

            y = a*x**2+b*x+c
            print(" ")
            print("y is equal to", y)    


            #part


        if variable == 'x':
            a = input("What is the value of a? ")
            c = input("What is the value of c? ")
            y = input("What is the value of x? ")
            b = input("What is the value of b? ")

            a = int(a)
            c = int(c)
            y = int(y)
            b = int(b)

            x = (y-c)/(a*x+b)
            print(" ")
            print("x is equal to", x)    


            #part

    if form1 == 'intercept':        
            m = input("What is the value of m? ")
            n = input("What is the value of n? ")
            x = input("What is the vlaue of x? ")
            a = input("What is the value of a?")
            b = input("What is the value of b?")

            m = int(m)
            n = int(n)
            x = int(x)
            a = int(a)
            b = int(b)

            y = (a*x+m)*(b*x+n)
            print(" ")
            print("y is equal to", y)    


            #part
            #(x+m)(x+n)

        

        


if equation == 'linear':
    print("The equation for standard form is ax+by=c and slope-intercept is y=mx+c")
    form1 = input('What form are you solving, standard, or slope-intercept? ')
    
    options2 = ["standard", "slope-intercept"]

    
    if equation not in options2:
        print(' ')
        print("Chose one of the following options")
        print("standard")
        print("slope-intercept") 
        print(' ')

        form1 = input('What form are you solving, standard or slope-intercept? ') 

        #part2

    if form1 == 'standard':
        variable = input("Which variable are you solving for x or y ? ")

        option3 = ["x", "y"]

        if variable not in option3:
            print(' ')
            print("Choose one of the following options")
            print('x')
            print('y')
            print(' ') 

            variable = input("Which variable are you solving for x or y ? ")

            #part

        if variable == 'y':
            a = input("What is the value of a? ")
            c = input("What is the value of c? ")
            x = input("What is the vlaue of x? ")
            b = input("What is the value of b?")

            a = int(a)
            c = int(c)
            x = int(x)
            b = int(b)

            y = (c-a*x)/b
            print(" ")
            print("y is equal to", y)    


            #part
        
        if variable == 'x':
            a = input("What is the value of a? ")
            c = input("What is the value of c? ")
            y = input("What is the vlaue of x? ")
            b = input("What is the value of b?")

            a = int(a)
            c = int(c)
            y = int(y)
            b = int(b)

            x = (c-b*y)/a
            print(" ")
            print("x is equal to", x)    


            #part    

    if form1 == 'slope-intercept':
        variable = input("Which variable are you solving for x or y ? ")

        option3 = ["x", "y"]

        if variable not in option3:
            print(' ')
            print("Choose one of the following options")
            print('x')
            print('y')
            print(' ') 

            variable = input("Which variable are you solving for x or y ? ")

             #part3

        if variable == 'y':
            m = input("What is the value of m? ")
            c = input("What is the value of c? ")
            x = input("What is the vlaue of x? ")

            m = int(m)
            c = int(c)
            x = int(x)

            y = m*x+c
            print(" ")
            print("y is equal to", y)

            #part4
        
        if variable == 'x':
            m = input("What is the value of m? ")
            c = input("What is the value of c? ")
            y = input("What is the vlaue of y? ")

            m = int(m)
            c = int(c)
            y = int(y)

            x = (y-c)/m 
            print(" ")
            print("x is equal to", x)

            #part5



