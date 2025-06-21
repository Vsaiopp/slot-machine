# slot machine 

#part 1 defining functions 
def spin_row() :
    pass 

def print_row():
    pass

def payout():
    pass 

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

       if balance <= 0 :
        is_running = False 
        print('current balance is zero cant play further ')
    except ValueError :
        print('Not a valid number ')

print(f'your balance is {balance}')