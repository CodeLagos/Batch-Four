#To get the inbuilt function "random"
import random

#To prepare the list of automobiles 
def get_word():
    cars = ['Peugeot',
            'Hyundai',
            'Acura',
            'Ferrari',
            'Porsche',
            'Cardillac',
            'Toyota',
            'Nissan',
            'Volkswagen',
            'Bmw',
            'Honda',
            'Chevrolet',
            'Bugatti',
            'Volvo',
            'Kia',
            'Maserati',
            'Opel',
            'Chrysler',
            'Ford']
#to sort and return any of the elements from the list "cars"
    return random.choice(cars).upper()
    
def check(car,answers,response):
    response= response.upper()
    
    #Using "status" to store what is to be displayed to the user
    status=''
    i = 0
    correct = 0
    for letter in car:
        if letter in answers:
            status += letter
        else:
             status +='*'
             
        if letter==response:
           correct += 1
            
    if correct > 1:
        print('Yes! The word contains',correct,'"'+response+'"'+'s')
    elif correct == 1:
        print('Yes! The word contains the letter','"'+response+'"')
    else:
        print('Sorry, The word does not contain the letter','"'+response+'"')
    return status
             
def main():
    car = get_word()
    
    #To keep track of the guessed letters or word
    answers = []
    guessed = False
    name=str(input('Please enter your name: '))
    print('Welcome! '+name+', This is the car quiz game.')
    print('*HINT: This particular car comprises of',len(car),'letters.')
    while not guessed:
        text = 'Please enter a letter or name of the car: '.format(len(car))
        response=input(text)
        response=response.upper()
        if response in answers:
            print('You already guessed"'+response+'"')
        elif len(response) == len(car):
            answers.append(response)
            if response==car:
                guessed=True
            else:
                 print('Sorry, that is incorrect.')
        elif len(response) == 1:
            answers.append(response)
            result=check(car,answers,response)
            if result == car:
                guessed = True
                
            else:
                 print(result)
        else:
             print('Invalid entry!')
    print('Congrats! The car is',car+'!''You got it in',len(answers),'tries')

main()

"""Author:      Adesanya Oluwatobi Betty
Contact number: 08170600477
E-mail address: oluwatobiadesanya36@yahoo.com"""
