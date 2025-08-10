
def function():

    hand_size=7
    bonus_point=50
    vowels=set('aeiou')
    score=0
    
    while True:
        word=input('Enter a word: ')
        if word.isalpha() and len(word) <= hand_size:
            break
        else:
            print('Invalid input. Please enter a word containing only letters and not exceeding the hand size of', hand_size)

    word=word.lower()

    for char in word:
        if char in vowels:
            score += 1
        elif char.isalpha():
            score += 2


    if len(word) == hand_size:
        score= (score * len(word))+ bonus_point
    else:
        score = score * len(word)

    print('Your score is: ', score)






if __name__== '__main__':
    
    while True:
        function()
        again = input('Do you want to play again? (y/n): ').strip().lower()
        if again == 'n':
            print('Thank you for playing!')
            break
    




