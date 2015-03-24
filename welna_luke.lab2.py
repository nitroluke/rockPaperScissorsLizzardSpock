import random

class Element:              # parent class Element
    def __init__(self,name):          # innitialize
        self._name = name

    def compareTo(Element):
        raise NotImplementedError("Not yet implemented, Element class compare to method")

    def name(self):
        return self._name

class Rock(Element):        # Rock class
    def __init__(self, name):   #innitialize rock
        self.name = name
        self.winMove1 = 'rock'
        self.winMove2 = 'rock'

    def beats(self):            #returns what rock beats
        self.winMove1 = moves[2]        #scissors
        self.winMove2 =  moves[3]       #lizzard
        return [self.winMove1,self.winMove2]

    def compareTo(self, Element):             # over written comareTo method for Rock
    #dont think i need comments for the conditional statements, pretty straight forward
        if(Element.name == paper.name):
            return ('Paper covers Rock', 'Lose')
        elif(Element.name == lizzard.name):
            return ('Rock crushes Lizzard', 'Win')
        elif(Element.name == spock.name):
            return ('Spock vaporizes Rock', 'Lose')
        elif(Element.name == scissors.name):
            return ('Rock crushes Scissors', 'Win')
        elif(Element.name == self.name):                  # if the passed in element equals  Rock's instance of self,self, its a tie
            return ('Rock equals Rock', 'Tie')
        else:
            raise NotImplementedError("Not yet implemented, Unhandled Input in Rock")


class Paper(Element):           #Paper class
    def __init__(self, name):       #initializaton
        self.name = name
        self.winMove1 = 'paper'
        self.winMove2 = 'paper'

    def beats(self):    # returns what paper beats
        self.winMove1 = moves[0]        # rock
        self.winMove2 =  moves[4]       #spock
        return self.winMove1,self.winMove2

    def compareTo(self, Element):             # over written comareTo method for Paper
    #dont think i need comments for the conditional statements, pretty straight forward
        if(Element.name == rock.name):
            return ('Paper covers Rock','Win')
        elif(Element.name == lizzard.name):
            return ('Lizzard eats Paper', 'Lose')
        elif(Element.name == spock.name):
            return('Paper disproves Spock', 'Win')
        elif(Element.name == scissors.name):
            return('Scissors cut Paper', 'Lose')
        elif(Element.name == self.name):                          # compares the passed in element to self (Paper)
            return('Paper = Paper', 'Tie')
        else:                                                                   #this should never happen....
            raise NotImplementedError("Not yet implemented, Unhandled Input in Paper")


class Lizzard(Element):         # Lizzard class
    def __init__(self, name):       #initialization
        self.name = name
        self.winMove1 = 'lizzard'
        self.winMove2 = 'lizzard'

    def beats(self):        #returns what Lizzard Beats
        self.winMove1 = moves[1]        #paper
        self.winMove2 =  moves[4]       #spock
        return self.winMove1,self.winMove2

    #dont think i need comments for the conditional statements, pretty straight forward
    def compareTo(self,Element):         #overwritten compare to Method for Lizzard
        if(Element.name == rock.name):
            return ('Rock crushes Lizzard','Lose')
        elif(Element.name == self.name):               # compares passed in element to self (Lizzard)
            return ('Lizzard equals Lizzard', 'Tie')
        elif(Element.name == spock.name):
            return('Lizzard poisons Spock', 'Win')
        elif(Element.name == scissors.name):
            return('Scissors decapitate Lizzard', 'Lose')
        elif(Element.name == paper.name):
            return('Lizzard eats Paper', 'Win')
        else:                       # should never happen
            raise NotImplementedError("Not yet implemented, Unhandled Input in Lizzard")


class Scissors(Element):            #Scissors class
    def __init__(self, name):           #Scissors initialization
        self.name = name
        self.winMove1 = 'scissors'
        self.winMove2 = 'scissors'

    def beats(self):        #returns what Scissors beats
        self.winMove1 = moves[1]        #paper
        self.winMove2 =  moves[3]       #lizzard
        return self.winMove1,self.winMove2

    #dont think i need comments for the conditional statements, pretty straight forward
    def compareTo(self, Element):         #over written compare to method  for Scissors
        if(Element.name == rock.name):
            return ('Rock crushes Scissors','Lose')
        elif(Element.name == lizzard.name):
            return ('Scissors decapitate Lizzard', 'Win')
        elif(Element.name == spock.name):
            return('Spock smashes Scissors', 'Lose')
        elif(Element.name == self.name):          # compares passed in element to self (scissors)
            return('Scissors equals Scissors', 'Tie')
        elif(Element.name == paper.name):
            return('Scissors cut Paper', 'Win')
        else:               #shouldnt happen
            raise NotImplementedError("Not yet implemented, Unhandled Input in Scissors")


class Spock(Element):                   #class Spock
    #print('RIP Leonard')
    def __init__(self, name):           #spock initialization
        self.name = name
        self.winMove1 = 'spock'
        self.winMove2 = 'spock'

    def beats(self):        #returns what Spock Beats
        self.winMove1 = moves[0]        #rock
        self.winMove2 =  moves[2]       #scissors
        return self.winMove1,self.winMove2

    def compareTo(self, Element):    #over written compareTo method for Spock

    #dont think i need comments for the conditional statements, pretty straight forward
        if(Element.name == rock.name):
            return ('Spock vaporizes Rock', 'Win')
        elif(Element.name == paper.name):
            return ('Paper disproves Spock', 'Lose')
        elif(Element.name == scissors.name):
            return('Spock crushes Scissors', 'Win')
        elif(Element.name == lizzard.name):
            return ('Lizzard poisons Spock', 'Lose')
        elif(Element.name == spock.name):                 # compares passed in element to self(Spock)
            return('Spock equals Spock', 'Tie')
        else:                   #nope
            raise NotImplementedError("Not yet implemented, unhandled Input in Spock")

# Element innitializations
rock = Rock('rock')
paper = Paper('paper')
lizzard = Lizzard('lizzard')
scissors = Scissors('scissors')
spock = Spock('spock')
global moves                        # global varialbe called moves
moves = [rock, paper, scissors, lizzard, spock]  #which contains the previously created instances

#beats inittializations
rock.beats()
paper.beats()
lizzard.beats()
scissors.beats()
spock.beats()

class Player:       # Parent Player class
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

        def play():
            raise NotImplementedError('play not yet implemented in class player')

class StupidBot(Player):            # StupidBot inherits Player class
    def __init__(self, name):           #Scissors initialization
        self.name = name

    def play(self):
        return moves[4]         # returns moves[4] (spock) everytime

class RandomBot(Player):        #RandomBot inherits Player class
    def __init__(self, name):           #Scissors initialization
        self.name = name

    def play(self):
            rand = random.randrange(0,moves.__len__())
            return moves[rand]          # returns a random object everytime

class IterativeBot(Player):

    def __init__(self, name, counter):   # takes in a name and a counter @override Player
        self.name = name
        self.counter = counter

## fix  the multiple rock returns.....
    def play(self):        # takes in a counter to iterate through moves[] to grab a different object each time this method is called
        if (self.counter == moves.__len__()):         # if counter == 5, reset the counter and return the value
            self.counter = 0
            return moves[self.counter]
        else:                                                       #otherwise i
            temp = self.counter                     # saves the counter before it is incremented
            self.counter = self.counter + 1         # increment the counter
            return moves[temp]                          # return the counter


#implement LastPlayBot
class LastPlayBot(Player):
    def __init__(self, name):           #Scissors initialization
        self.name = name
    def play(self,player,lastPlayList):
        if(lastPlayList[0] == 0 or lastPlayList[1] == 0):
            return playersList[2].play()               # if its the first  round, return randomBot.play()
        if(player == lastPlayList[0]):  # if player equals player 1
            return lastPlayList[3]      # return player2's move
        elif(player == lastPlayList[2]): #else if player equals player2
            return lastPlayList[1]      #return player1's move
        else:
            raise NotImplementedError("Not yet implemented, Unhandled condition in LastPlayBot")
            print()

#implement myBot  will be unbeatable if player2 otherwise picks randomly
class MyBot(Player):
    def __init__(self, name):           #Scissors initialization
        self.name = name

    def play(self,playerMove,ID):
        winOptions = [None, None]
        if(ID == 1):                # if myBot is player 1, just make random plays
            return playersList[2].play()
        elif(ID == 2):              # if myBot is player2, we can win everytime
            rand = random.randrange(0,2)
            winOptions = playerMove.beats()
            return winOptions[rand]
        else:
            print("playerMove when exception=", playerMove)
            raise NotImplementedError("Not yet implemented, Unhandled playerType in MyBot")

class Human(Player):
    def __init__(self, name):           #Scissors initialization
        self.name = name

    def play(self):
        while(1):
            print("""
Human, please choose a move:
    (1) : Rock
    (2) : Paper
    (3) : Scissors
    (4) : Lizzard
    (5) : Spock
""")
            userInput = input("Enter your move:  ")                 #ask user for input
            try:        # begginning of try clause, if int(userInput) throws an error(is a non integer)
                userInput = int(userInput)          # cast userinput to an int
                if(userInput < (moves.__len__()+1) and userInput > 0):            # bounds for userInput
                    return moves[userInput-1]               # return moves[userInput - 1] to offset for the array
                else:           #otherwise it is outside of our bounds
                    print('invalid move, please try again')
            except ValueError:          # will execute if casting userinput to an int throws an error
                print("Invalid move, please try again")

#  player Innitializations
randomBot = RandomBot('randomBot')
iterativeBot = IterativeBot('iterativeBot',0)
human = Human('human')
stupidBot = StupidBot('stupidBot')
lastPlayBot = LastPlayBot('lastPlayBot')
myBot = MyBot('myBot')

playersList = [human, stupidBot, randomBot, iterativeBot, lastPlayBot, myBot]         # global list of playersList
class main():
    def getPlayer(usrInput):
        return playersList[usrInput - 1]

    def checkInput(usrInput):           # there is a little bug where It only prints the last error thrown.  Could fix this by having seperate try excepts for each unput, but i dont feel like it.
        try:        # begginning of try clause, if int(userInput) throws an error(is a non integer)
            usrInput = int(usrInput)          # cast userinput to an int
            if(usrInput < (playersList.__len__() + 1) and usrInput > 0):            # bounds for userInput
                return 1
            else:           #otherwise it is outside of our bounds
                print("'{}' is an invalid option, please try again".format(usrInput))
                return 0
        except ValueError:          # will execute if casting userinput to an int throws an error
            print("'{}' is an invalid option, please try again".format(usrInput))
            return 0

    print("Welcome to Rock, Paper, Scissors, Lizzard, Nemoy(Spock), implemented by Luke Welna")
    while(1):
        print("""
Please choose two players:
    (1)  Human
    (2)  StupidBot
    (3)  RandomBot
    (4)  IterativeBot
    (5)  LastPlayBot
    (6)  MyBot
            """)
        userInput1 = input("Select Player 1:  ")                 #ask user for input for player 1
        userInput2 = input("Select Player 2:  ")
        lastPlay = [0,0,0,0]            #list initialization for lastPlayBot implementation
        player1Move = 1;        #innitialistion for player1Move
        print()
        if(checkInput(userInput1) and checkInput(userInput2)):                  # if the user enters valid inputs
            player1 = getPlayer(int(userInput1))            # cast inputs to an int
            player2 = getPlayer(int(userInput2))
            print("{} vs {}. Go!\n".format(player1.name,player2.name))
            player1Counter = 0              #innitialize counters to keep track of winner
            player2Counter = 0
            for i in range(0,5):                # Play 5 rounds
                print("Round {}:".format(i+1))
                if((player1 == lastPlayBot and player2 == lastPlayBot)):            #if both players are lastPlayBot (there is a bug here, it should switch between both players moves but it doesnt)
                    move1 = player1.play(player1,lastPlay)      # move1 = player2's last move
                    move2 = player2.play(player2,lastPlay)      # move2 - player1's last move
                    lastPlay = [player1,move1,player2,move2]    #update lastPlay with the players and their last moves
                elif(player1 == lastPlayBot and player2 == myBot):              #if player1 = lastPlayBot and plyaer2 = myBot
                    move1 = player1.play(player1,lastPlay)                  #move1 = lastPlayBot (will just return a random move)
                    move2 = player2.play(move1,2)                               #move2 = the move to lose against lastPlayBot's Move
                elif(player1 == myBot and player2 == lastPlayBot):          #oposite condiitions to the one directly above
                    move1 = player1.play(None,1)
                    move2 = player2.play(player2,lastPlay)
                elif(player1 == lastPlayBot ):                          #if player1 = last playBot
                    move1 = player1.play(player1,lastPlay)      #will just return a random move since player1 is last playBot
                    move2 = player2.play()
                    lastPlay = [player1,move1,player2,move2]        #update both players and their move is LastPlay
                elif(player2 == lastPlayBot ):
                    move1 = player1.play()
                    move2 = player2.play(player2,lastPlay)      #will play player1's last move
                    lastPlay = [player1,move1,player2,move2]        #update lastPlay with both players and their move
                elif(player1 == myBot and player2 == myBot):            #if both players are my bot, player2 will always lose
                    move1 = player1.play(player1Move,1)
                    move2 = player2.play(move1,2)
                elif(player1 == myBot):         #if player 1 = myBot, will just return a random move
                    move1 = player1.play(None,1)
                    move2 = player2.play()
                elif(player2 == myBot):      # if player2 = myBot, player2 will always lose.
                    move1 = player1.play()
                    move2 = player2.play(move1,2)
                else:
                    move1 = player1.play()          # move1 is player1's move
                    move2 = player2.play()          #  move2 is player2'c move
                print("   player 1 chose", move1.name)
                print("   player 2 chose", move2.name)
                result = move1.compareTo(move2)             # comparing player1's move to player2's move and sets it to result
                print("  ",result[0])            # the first argument returned from the compareTo fuction
                if(result[1] == 'Win'):         # conditional statements checking if Win, Tie, or Lose
                    print('   Player 1 won the round\n')
                    player1Counter = player1Counter + 1   # if player wins, incement player1Counter
                elif(result[1] == 'Tie'):
                    print("   Round was a tie\n")
                elif(result[1] == 'Lose'):
                    print("   Player 2 won the round\n")
                    player2Counter = player2Counter + 1# if player2 wins, incement player2Counter
                else:
                    print("   Unhandled condition getting result of round\n")
            print("The score is", player1Counter, "to", player2Counter)
            if(player1Counter > player2Counter):            #conditional statement for getting the winner.
                print("Player 1 wins the game\n")
            elif(player2Counter == player1Counter):
                print("Game was a draw\n")
            else:
                print("Player 2 wins the game\n")
        else:
            pass
