import random
def rolldice():
    res=random.randint(1,6)
    if res == 6:
        print('You got 6...you will get one more chance.. ' )
        res=res + rolldice()
    return res
def main():
    while True:
        prompt=input('Do you want to roll the dice:[y/n] ')
        if prompt == 'y':
            result=rolldice()
            print('You got ', str(result))
        elif prompt == 'n':
            print('Ending the game')
            break
        else:
            print('Please enter y or n')
            continue
main()

