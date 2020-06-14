import random

dice_rolls = int(input('How many dice would you like to roll? '))

def main():
    dice_sum = 0
    
    for i in range(0,dice_rolls):
        
        roll = random.randint(1,6)
        
        dice_sum += roll #or dice_sum = dice_sum + roll 
        
        if roll == 1:
            print(f'Unlucky af ya rolled da {roll}')
            
        elif roll == 6: #i see no point in that elif tbh
            print(f'Congrats bruh ya rolled da {roll}')
            
        else:
            print(f'You rolled a {roll}')
        
    print(f'You have rolled a total of {dice_sum}')
        
main()