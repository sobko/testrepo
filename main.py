from random import randint

def main():
    item_order = ["rock", "scissors", "paper"]
    computer_wins = 0
    player_wins = 0
    print("Time for an RPS throwdown!")
    print("Type r for rock, p for paper, or s for scissors.  We'll play until someone wins 5.")
    name = input("What is your name?")
    while True:
        move = input("Your choice: ").lower().strip()[0]
        if move not in ['r','p','s']:
            print("Not a valid move.")
            continue
        computer_move = randint(0,2)
        print(f"I choose {item_order[computer_move]}")
        result = check_move(move, computer_move)
        if result == 'tie':
            print("Its a tie")
        elif result == 'player':
            player_wins += 1
            print(f"{name} wins.")
        else:
            computer_wins += 1
            print("I win.")
        print(f"The score is {name}: {player_wins}, computer: {computer_wins}")
        if computer_wins >= 5 or player_wins >= 5:
            break

    if computer_wins > player_wins:
        print("I win the game!")
    else:
        print(f"{name} wins the game. Maybe next time.")

def check_move(move, computer_move):
    if move == 'r':
        m = 0
    elif move == 's':
        m = 1
    else:
        m = 2
    result = (m - computer_move) % 3
    if result == 0:
        return 'tie'
    elif result == 1:
        return 'computer'
    else:
        return 'player'

main()
