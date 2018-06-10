import random


class Game:

    def __init__(self, userName):
        self.userName = userName
        self.userHand = 'NA'
        self.botHand = "NA"
        self.winner = 'No Winner Yet!'
        print("New instance of Game Class for " + self.userName)

    def runGame(self):
        self.botHand = random.randint(1, 3)

        self.userHand = input("Pick rock, paper or scissors ")
        print("You pick " + self.userHand)
        if (self.botHand == 1):
            print("Computer picks Rock")
        elif (self.botHand == 2):
            print("Computer picks Paper")
        elif (self.botHand == 3):
            print("Computer picks Scissor")

        if ((self.userHand == 'rock' or self.userHand == 'Rock') and self.botHand == 1):
            self.winner = 'You Tie'
        elif ((self.userHand == 'rock' or self.userHand == 'Rock') and self.botHand == 2):
            self.winner = 'You Loose.'
        elif ((self.userHand == 'rock' or self.userHand == 'Rock') and self.botHand == 3):
            self.winner = 'You Win.'
        elif ((self.userHand == 'paper' or self.userHand == 'Paper') and self.botHand == 1):
            self.winner = 'You Win.'
        elif ((self.userHand == 'paper' or self.userHand == 'Paper') and self.botHand == 2):
            self.winner = 'You Tie!'
        elif ((self.userHand == 'paper' or self.userHand == 'Paper') and self.botHand == 3):
            self.winner = 'You Loose.'
        elif ((self.userHand == 'scissors' or self.userHand == 'Scissors') and self.botHand == 1):
            self.winner = 'You Loose.'
        elif ((self.userHand == 'scissors' or self.userHand == 'Scissors') and self.botHand == 2):
            self.winner = 'You Win.'
        elif ((self.userHand == 'scissors' or self.userHand == 'Scissors') and self.botHand == 3):
            self.winner = 'You Tie!'
        else:
            self.winner = 'INVALID input, try again'


def main():
    myGame = Game("Divyansh")
    myGame.runGame()
    print(myGame.winner)

main()