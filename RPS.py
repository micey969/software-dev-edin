import random

class Game:
    def __init__(self):
        self.start = self.opponent()


    def opponent(self):
        option = int(input("\nWho would like to play against? 1 - Player, 2 - Computer: "))
        
        if (option != 1 and option != 2):
            print("\nInvalid option. Must choose either '1' or '2'. Please try again.")
            self.opponent()

        rounds = int(input("\nHow many rounds would you like to play? 1, 3 or 5? "))
        
        if (rounds != 1 and rounds != 3 and rounds != 5):
            print("\nInvalid option. Must choose either '1' or '3' or '5'. Please try again.")
            self.opponent()

        self.player(rounds) if (option == 1) else self.computer(rounds)


    def computer(self, rounds):
        player = robot = 0
        while rounds != 0:
            choice = int(input("\nPlease enter your choice. Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
            comp = random.randint(0,2)
           
            win = self.check_win(choice, comp)
            if(win == 0):
                print("\nDraw!")
            elif(win==1):
                print("\nYou win!")
                player+=1
            else:
                print("\nComputer wins!")
                robot+=1
            rounds-=1

        print(f"\nYou win: {player} - {robot}") if (player > robot) else print(f"\nComputer wins: {robot} - {player}")
        self.replay()


    def player(self, rounds):
        player1 = player2 = 0
        while rounds != 0:
            choice1 = int(input("\nPlayer1 enter your choice. Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
            choice2 = int(input("\nPlayer2 enter your choice. Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
           
            win = self.check_win(choice1, choice2)
            if(win == 0):
                print("\nDraw!")
            elif(win==1):
                print("\nPlayer1 win!")
                player1+=1
            else:
                print("\nPlayer2 wins!")
                player2+=1
            rounds-=1

        print(f"\nPlayer1 win: {player1} - {player2}") if (player1 > player2) else print(f"\nPlayer2 wins: {player2} - {player1}")
        self.replay()

   
    def check_win(self, opt1, opt2):
        if (opt1 == opt2):
            return 0
        if ((opt1 and opt2 < 2) and (opt1 > opt2)):
            return 1
        if ((opt1 and opt2 > 0) and (opt1 > opt2)):
            return 1
        if ((1 < opt1 and opt2 < 1) and (opt1 < opt2)):
            return 1
        return 2


    def replay(self):
        print("\nGood game.")
        choice = input("Would you like to play again? 'Y' or 'N':  ")

        if(choice == 'Y'):
            main()
        
        print("Thanks for playing. Good bye.")


def main():
    print("Welcome to Rock, Paper, Scissors")
    game_play = Game()


if __name__ == "__main__":
    main()
