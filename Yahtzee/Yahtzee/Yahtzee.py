from enum import Enum
class YahtzeeScore(Enum):
    Ones = 1
    Twos = 2
    Threes = 3
    Fours = 4
    Fives = 5
    Sixes = 6
    Pair = 7
    TwoPair = 8
    ThreeOfAKind = 9
    FourOfAKind = 10
    SmallStraight = 11
    LargeStraight = 12
    FullHouse = 13
    Yahtzee = 14
    Chance = 15

def score(dice, method):    
    if method == YahtzeeScore.Ones:
        return scoreNumber(dice,1)    
    if method == YahtzeeScore.Twos:
        return scoreNumber(dice,2)    
    if method == YahtzeeScore.Threes:
        return scoreNumber(dice,3)    
    if method == YahtzeeScore.Fours:
        return scoreNumber(dice,4)    
    if method == YahtzeeScore.Fives:
        return scoreNumber(dice,5)    
    if method == YahtzeeScore.Sixes:
        return scoreNumber(dice,6)
    if method == YahtzeeScore.Pair:
        return scorePair(dice)
    if method == YahtzeeScore.TwoPair:
        return scoreTwoPair(dice)
    if method == YahtzeeScore.ThreeOfAKind:
        return scoreThreeOfAKind(dice)
    if method == YahtzeeScore.FourOfAKind:
        return scoreFourOfAKind(dice)
    if method == YahtzeeScore.Yahtzee:
        return scoreFiveOfAKind(dice)
    if method == YahtzeeScore.SmallStraight:
        return scoreSmallStraight(dice)
    if method == YahtzeeScore.LargeStraight:
        return scoreLargeStraight(dice)
    if method == YahtzeeScore.FullHouse:
        return scoreFullHouse(dice)
    if method == YahtzeeScore.Chance:
        return scoreChance(dice)
    return 0

def scoreNumber(dice, matching_die_face):
    return (dice.count(matching_die_face)*matching_die_face)


def scoreNMatches(dice, N):
    listOfNMatches = createListOfDiceThatHaveAtLeastNMatches(dice,N)
    if len(listOfNMatches) > 0:
        return N*listOfNMatches.pop()
    return 0

def scorePair(dice):
    return scoreNMatches(dice,2)

def scoreThreeOfAKind(dice):
    return scoreNMatches(dice,3)

def scoreFourOfAKind(dice):
    return scoreNMatches(dice,4)

def scoreFiveOfAKind(dice):
    return scoreNMatches(dice,5)


def scoreTwoPair(dice):
    listOfPairs = createListOfDiceThatHaveAtLeastNMatches(dice,2)
    if len(listOfPairs) == 2:
        return 2*sum(listOfPairs)
    return 0


def scoreFullHouse(dice):
    diceCounts = findMatches(dice)
    if ((diceCounts.count(2) > 0) & (diceCounts.count(3) > 0)):
        return sum(dice)
    return 0


def scoreSmallStraight(dice):
    diceCount = findMatches(dice)

    all_straights = ((diceCount[2] > 0) & (diceCount[3] > 0))   #all straights have 3 & 4
    straight1     = ((diceCount[0] > 0) & (diceCount[1] > 0))   #  combo1: 1,2,3,4
    straight2     = ((diceCount[1] > 0) & (diceCount[4] > 0))   #  combo2: 2,3,4,5
    straight3     = ((diceCount[4] > 0) & (diceCount[5] > 0))   #  combo3: 3,4,5,6

    if all_straights & (straight1 | straight2 | straight3):
        return 30
    return 0


def scoreLargeStraight(dice):
    dice.sort()
    straight1 = ((dice[0]==1) & (dice[1]==2) & (dice[2]==3) & (dice[3]==4) & (dice[4]==5))
    straight2 = ((dice[0]==2) & (dice[1]==3) & (dice[2]==4) & (dice[3]==5) & (dice[4]==6))
    if (straight1 | straight2):
        return 40
    return 0

def scoreChance(dice):
    return sum(dice)

def createListOfDiceThatHaveAtLeastNMatches(dice,numberOfMatches):
    listOfDiceCounts = findMatches(dice)
    return [i+1 for i in list(range(6)) if listOfDiceCounts[i]>=numberOfMatches]

def findMatches(dice): 
    return [dice.count(i+1) for i in list(range(6))]