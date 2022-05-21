from random import *

def blackjack():
    print('Welcome to Blackjack. \n____________________________________')
    game_start = input('Do you wish to start a new game? (y/n):')

    while (game_start != 'y' and game_start != 'n'):
            print('Input can only be y or n.')
            game_start = input('Do you wish to start a new game? (y/n):')

    if game_start != 'y':
        print("bye bye")
        return 0

    player = randint(1, 10)
    player_1 = randint(1, 10)
    dealer = randint(1, 10)
    dealer_1 = randint(1, 10)
    player_sum = player + player_1
    dealer_sum = dealer + dealer_1

    print(f'You draw {player} and a {player_1}. Your total is {player_sum}.')
    print(f'The dealer draws a {dealer} and a hidden card.')

    hs = input('Hit or stand? (h/s):')
    while (hs != 'h' and hs != 's'):
            print('Input can only be h or s.')
            hs = input('Hit or stand? (h/s):')

    # player moves
    while (player_sum < 21 and hs == 'h'):
        player = randint(1, 10)
        player_sum += player

        if player_sum > 21:
            print("Player loses.")
            return 0
        elif player_sum  == 21:
            hs = 's'
            print(f"Hit! You draw {player}. Your total sum is {player_sum}")
            break

        print(f'Hit! You draw a {player}. Your total is {player_sum}')

        hs = input('Hit or stand? (h/s):')

        # checking input
        while (hs != 'h' and hs != 's'):
            print('Input can only be h or s.')
            hs = input('Hit or stand? (h/s):')

    if hs == 's':
        print("You stand.")

    print(f"The dealer's hidden card is a {dealer_1}", end="")
    print(f" and has a total of {dealer_sum}.")

    while (dealer_sum < 17):
        dealer = randint(1, 10)
        dealer_sum += dealer
        print(f"The dealer is dealt a {dealer}.", end="")
        print(f"The dealer's total is {dealer_sum}.")

    print("The dealer stands.")
    print(f"You have a total of {player_sum} and the dealer has {dealer_sum}.")

    if player_sum > 21 and dealer_sum > 21:
        print("Dealer wins.")
    elif player_sum > 21 and dealer_sum <= 21:
        print("Dealer wins.")
    elif player_sum <= 21 and dealer_sum > 21:
        print('Player wins.')
    elif player_sum <= 21 and dealer_sum <= 21:
        if player_sum > dealer_sum:
            print('Player wins.')
        else:
            print('Dealer wins.')

def main():
    blackjack()

if __name__ == '__main__':
    main()
