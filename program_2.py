#Author: Faith Lamah
#Date: 10/03/2025
#Title: Math Quiz

import random
def main():
    another_one = 'y'
    while another_one == 'y':
        number1 = random.randint(1, 1000)
        number2 = random.randint(1, 1000)
        answer = int(input(f' {number1}\n+{number2}\n-----\n'))

        if answer == number1 + number2:
            print('Congratulations! You got it!')
        else:
            print(f'Incorrect. The correct answer is {answer}')
        another_one = input('Do you want to try another question? (y/n)')



if __name__ == '__main__':
    main()
#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.