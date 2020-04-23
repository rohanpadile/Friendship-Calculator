import re
import random

def hasNumbers(inputString):
    return bool(re.search(r'\d',inputString))

print('Welcome to friendship % calculator, Please follow the instructions\n')

while True:
    person_1 = input('Type your friends name\t')
    person_2 = input('\nType your own name\t')
    
    if hasNumbers(person_1) or hasNumbers(person_2):
        print('Please type proper name\nDo not include integers')
        continue
    else:
        if len(person_1)<=10 and len(person_2)<=10:

            # This logic will work as if both lenght becomes 10 then percentage will be 100

            x = len(person_1)**2
            y = len(person_2)**2
            sum = x*y
            fp = sum/100
           
            if 50 < fp <= 100:
                print(f'The friendship between {person_1} and {person_2} is {fp:1.2f}%\n')
                
            elif 40 < fp <= 50:
                fp = fp + random.randint(40,50)
                print(f'The friendship between {person_1} and {person_2} is {fp:1.2f}%\n')   
                
            elif 30 < fp <= 40:
                fp = fp + random.randint(50,60)
                print(f'The friendship between {person_1} and {person_2} is {fp:1.2f}%\n')   
                
            elif  20 < fp <= 30 :
                fp = fp + random.randint(60,70)
                print(f'The friendship between {person_1} and {person_2} is {fp:1.2f}%\n')   
                
            else:
                fp = fp + random.randint(70,80)
                print(f'The friendship between {person_1} and {person_2} is {fp:1.2f}%\n')   

        else:

                # couldnt find a suitable logic here for length greater than 10

            fp = random.randint(70,100)
            print(f'The friendship between {person_1} and {person_2} is {fp}%\n')
        
        
    answer = input('Do you want to quit? Type YES or NO')
    if answer.upper() == 'YES':
        break
    elif answer.upper() == 'NO':
        continue
    else:
        print('I dont have time for idiots! Bye')
        break



