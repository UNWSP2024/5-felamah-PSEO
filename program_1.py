# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.

#Author: Faith Lamah
#Date: 10/03/2025
#Title: Kilometer Conversion

def kilometer_conversion():
    kilometer = int(input('What is the distance in kilometer?'))
    mile = kilometer * 0.621371
    print(f'The distance is {mile:.2f} miles.')

    return mile
#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    kilometer_conversion()

    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!

    # Display the miles
