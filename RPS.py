import math
import random

# define n choose r
def choose(n ,r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

def expected(n):
    """ 
    Returns the expected number of rounds required to find a winner in an RPS game with
    n players.
    """  
    list = [0,0,1.5]
    i = 2
    while i < n :
        # calculate i+1 value
        sum = 0
        for j in range(2, i+1): 
            # loop through list
            sum += choose(i+1,j) * list[j]
        list.append( (3**(i) + sum) * ( 1.0/(2**(i+1) - 2) ) )
        i += 1  
    return list[int(n)]

def play(n):
    """
    returns the number of rounds required to find the winner in a random simulation of
    a game starting with n players. 
    """
    ret = 0
    if n == 1:
        return ret
    else:
        ret += 1
        # choices is list of n choices of 0, 1 or 2 (corresponding arbitrarily to R, P, S)
        choices = [ random.randint(0,2) for _ in range(int(n)) ]
        # stalemate if all 3 options appear or only 1 does
        while (0 in choices) + (1 in choices) + (2 in choices) != 2:
            ret += 1
            choices = [ random.randint(0,2) for _ in range(int(n)) ]
        # can pick random winner out of the 2 which appear
        # i.e. randomly assign 0, 1, 2 to R, P, S
        # either 1 or 2 for indexing of sorted tally array
        winner_index = random.randint(1,2)
        new_n = sorted([choices.count(x) for x in range(3)])[winner_index]
        return ret + play(new_n)

def recursive_play(n):  
    """
    returns the number of rounds required to find the winner in a random simulation of
    a game starting with n players. Uses recursion though so doesn't work for high n.
    """
    if n==1:
        return 0    
    else:
        list = []
        for i in range(int(n)):
            #assign 1,2,3 to R,P,S
            list.append( random.randint(1,3) )      
        # if all of R,P,S appear or only one appears
        if (1 in list) + (2 in list) + (3 in list) != 2 :
            return 1 + play(n)          
        elif not (1 in list):
            return 1 + play( list.count(3) )        
        elif not (2 in list):
            return 1 + play( list.count(1) )
        else: # 3 not in list
            return 1 + play( list.count(2) )
            
def iterate(t,n):
    """
    Simulates t games of n players, returning the mean number of rounds required to find
    a winner
    """
    sum = 0;
    for i in range(t):
        sum += play(n)
    return sum/float(t)
            
n = int(raw_input("Enter the number of players in the RPS game: "))
print ("Expected number of rounds to find a winner: " + str(expected(n)) )
t = int(raw_input("Enter number of trial games to randomly run: "))
print ("Average number of rounds to find a winner from " + str(t) + " trials: " + str (iterate(t,n)) +"\n")
            