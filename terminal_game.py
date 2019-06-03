from constructors import dealer, deck, player

#create the player
print('Welcome to blackjack on the command line,\nYou have $200 to start with good luck!')
user = input('Please enter your name:\n')
Player = player.Player(user)
print('Welcome ' + Player.name + '! You have $200, good luck!')

#create the dealer
Dealer = dealer.Dealer()

#create a deck
playing_deck = deck.Deck()
playing_deck.initialize()

still_playing = True

#main game structure
while still_playing == True:

    #placing bet
    print('You have $' + str(Player.money) + ' currently.')
    bet_status = False
    while bet_status == False:
        try:
            bet = int(input('Please enter the amount of money you want to bet: \n'))
            if bet > Player.money:
                print('You have entered a bet that is greater than the amount of money you have.')
            elif bet <= 0:
                print('You have entered a bet that is 0 or negative.')
            else:
                Player.money -= bet
                Dealer.money += bet
                bet_status = True
        except ValueError:
            print('Error, you must enter a numerical money value.')
    
    #shuffle and deal cards
    playing_deck.shuffle()
    Dealer.deal(playing_deck, Player)
    dealer_faceup = Dealer.hand[0]
    print('Dealers face up card is ' + dealer_faceup.card_name + ' of ' + dealer_faceup.suit + '.')   

    #player takes turn        
    hit_status = True
    while hit_status == True:
        print('Your hand is:')
        for i in range(len(Player.hand)):
            print(Player.hand[i].card_name + ' of ' + Player.hand[i].suit)
        print('Your hand count is now at ' + str(Player.hand_count) + '.')
        if Player.hand_count < 21:
            player_wants_hit = input('Would you like to hit? You can enter y/n for yes/no:\n')
            if (player_wants_hit.lower()=='y' or player_wants_hit.lower()=='yes'):
                Player.hit(playing_deck)
            elif (player_wants_hit.lower()=='n' or player_wants_hit.lower()=='no'):
                hit_status = False
            else:
                print('\nPlease enter a valid yes/no. You can use y/n.')
        elif Player.hand_count == 21:
            print("You have hit 21!!!\n")
            hit_status = False
        else:
            hit_status = False

    #dealer takes turn
    Dealer.strategy(playing_deck)
    print('Dealers hand is:')
    for i in range(len(Dealer.hand)):
        print(Dealer.hand[i].card_name + ' of ' + Dealer.hand[i].suit)
    print('Dealer hand count is at ' + str(Dealer.hand_count) + '.\n')

    #determine outcome
    if (Dealer.hand_count==Player.hand_count and Dealer.hand_count<22 and Player.hand_count<22):
        print('You have tied the dealer, you bet has been returned.')
        Player.money += bet
        Dealer.money -= bet
    elif (Dealer.hand_count>21 and Player.hand_count<21):
        print('The dealer has gone over, you win!')
        Player.money += bet*2
        Dealer.money -= bet*2
    elif (Dealer.hand_count<22 and Player.hand_count>21):
        print('You have gone over...')
    elif (Dealer.hand_count<22 and Player.hand_count<22 and Player.hand_count>Dealer.hand_count):
        print('You beat the dealer, you win!')
        Player.money += bet*2
        Dealer.money -= bet*2
    elif (Dealer.hand_count<22 and Player.hand_count<22 and Player.hand_count<Dealer.hand_count): 
        print('You have lost to the dealer...')
    
    #reset the table
    Dealer.reset_table(playing_deck, Player)

    #determine if player is still playing
    right_syntax = False
    while right_syntax == False:
        if Player.money == 0:
            still_playing = False
            right_syntax = True
            print('You have run out of money, better luck next time!')
        elif Dealer.money < 0:
            still_playing = False
            right_syntax = True
            print('Congrats you have broken the house!!!!!!!!')
        else:
            cont = input('Would you like to continue playing? You can enter y/n for yes/no:\n')
            if (cont.lower()=='y' or cont.lower()=='yes'):
                right_syntax = True
            elif (cont.lower()=='n' or cont.lower()=='no'):
                still_playing = False
                right_syntax = True
                print('Thanks for playing!')
            else:
                print('\nPlease enter a valid yes/no. You can use y/n.')