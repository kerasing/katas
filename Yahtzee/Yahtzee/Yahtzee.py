
def scoreNumber(dice, matching_die_face):
    return (countNumberOfDiceOfAParticularNumber(dice,matching_die_face)*matching_die_face)

def scorePair(dice):
    listOfPairs = createListOfPairs(dice)
    if len(listOfPairs) > 0:
        return 2*listOfPairs.pop()
    return 0

def scoreTwoPair(dice):
    listOfPairs = createListOfPairs(dice)
    if len(listOfPairs) == 2:
        return 2*sum(listOfPairs)
    return 0

def scoreSmallStraight(dice):
    diceCount = []
    for i in list(range(6)):
        diceCount.append(countNumberOfDiceOfAParticularNumber(dice, i+1))

    all_straights = ((diceCount[2] > 0) & (diceCount[3] >0))
    straight1 = ((diceCount[0] > 0) & (diceCount[1] > 0))
    straight2 = ((diceCount[1] > 0) & (diceCount[4] > 0))
    straight3 = ((diceCount[4] > 0) & (diceCount[5] > 0))

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

def countNumberOfDiceOfAParticularNumber(dice, number):
    return  len([d for d in dice if d==number])

def createListOfPairs(dice):
    listOfPairs = []
    for i in list(range(6)):
        checking_die = i+1
        count = countNumberOfDiceOfAParticularNumber(dice, checking_die)
        if count > 1:
            listOfPairs.append(checking_die)
    return listOfPairs
