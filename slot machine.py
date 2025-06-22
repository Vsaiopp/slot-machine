# slot machine 
#part 1 defining functions 
import random
def spin_row() :
    symbols = [ '🍉','⭐','🔔','🍐','🍎' ]
    return [random.choice(symbols) for symbol in range(3)]

def print_row():
   print('-------------')
   print(' | '.join(row))

def get_payout(row,bet):
    if row[0] == row[1] ==row[2] :
       return bet*5
    else :
       return 0

balance = 100
bet = 10
is_running = True 

while is_running :
    print('*****************************')
    print(' Welcome to our slot machine ')
    print('   symbols : 🍉⭐🔔🍐🍎    ')
    print('*****************************')
    print()
    print(f'Your current balance is : {balance}')
    bet = input('Enter a amount to place bet or q to quit : ')

    if bet == 'q'or bet =='Q' :
        print('Exiting the programme ')
        is_running = False 
        break 
    if bet == 10 :
        print( 'Enter a bet ')
        break
       
    try :

       bet = int(bet)
    
       if bet > balance:
        print('INSUFFICIENT FUNDS !!')

       elif bet <= 0:
        print('Bet must be greater than zero')

       else:
         balance -= bet
         row = spin_row()
         print_row()

         payout = get_payout(row,bet)

         if payout>0 :
            print('YOU WON !!!')
            balance+=bet
            chance = input('wanna play again (Y=yes ) and press any key to exit : ').upper()
            if chance == 'Y' :
               is_running =True
            else :
               is_running =False

       if balance <= 0 :
        is_running = False 
        print('current balance is zero cant play further ')
        
    except ValueError :
        print('Not a valid number ')

print(f'your balance is {balance}')