import random

print('Welcome to friendship % calculator,follow the instructions below \n')

person_1 = input('Type your friends name\t')
person_2 = input('\nType your own name\t')

if len(person_1)<=10 and len(person_2)<=10:
    # This logic will work as if both lenght becomes 10 then percentage will be 100
    x = len(person_1)**2
    y = len(person_2)**2
    sum = x*y
    fp = sum/100
    print(f'The friendship between {person_1} and {person_2} is {fp}%')    
else:
    # couldnt find a suitable logic here for length greater than 10
    z = random.randint(0,100)
    print(f'The friendship between {person_1} and {person_2} is {z}%')

