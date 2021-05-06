""" As there is no Switch Case statement in python, 
    to solve the GENDER problem,
    we can write something like this in C language.....

    #include<stdio.h>

    int main()
    {
        char gender;
        printf("Enter your Gender (M/m or F/f): ");             ...Taking input from the user....
        scanf("%c ", &gender);                                  ...Assigning the user's input to the variable 'gender'...

        switch(gender)
        {
            case 'M':
            case 'm':
                print("You are Male")
                break;
            
            case 'F':
            case 'f':
                print("You are Female")
        }

    }
"""