from game.card import Card


class Director:
    """A person who directs the game. 
    """

    def __init__(self):
          """
       new Director.
        """
        self.playagain = True
        self.totalscore = 300
        self.card1 = 0       
        self.card2 = 0
        self.hilo = ""

    def start(self):
          """
        Starts the game by running the main game loop.
        """
        while self.playagain:
            self.userinput()
            self.gameout()
            self.keepplaying()

    def userinput(self):
         """
        Gets the input of the user for higher or lower.
        """
        if not self.playagain:
            return
        self.card1 = Card.firstcardflip()
        print(f'This card is {self.card1}')
        self.hilo = input('Is this card higher or lower? [high/low]')
        if self.hilo == "high" or self.hilo == "low":
            return
        else:
            print('Please enter a high or low')
            self.userinput()
            return
    def gameout(self):
          """
        Flips a second card and updates the player's score accordingly.
        """
        if not self.playagain:
            return
        score = Card.secondcardflip(self.card1,self.hilo)
        self.totalscore = self.totalscore + score
        print(f'the score is {self.totalscore}')
        return
    def keepplaying(self):
         """
        Asks the player if they want to continue. 
        """
        if not self.playagain:
            return
        if self.totalscore <= 0:
            print('You\'ve lost, please try again')
            self.playagain = False
            return
        askagain = input('Would you like to play again? (y/n)')
        if askagain == "y":
            return
        elif askagain == "n":
            self.playagain = False
            return
        else:
            print('Please enter (y/n)')
            self.keepplaying()
            return


