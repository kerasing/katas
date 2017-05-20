import unittest
import Yahtzee

class Test_Yahtzee_tests(unittest.TestCase):
#tests for rule 1: individual dice faces
    def test_Ones(self):
        ones = roll(1,1,1,1,1)
        self.assertEqual(Yahtzee.scoreNumber(ones,1), 5)
        self.assertEqual(Yahtzee.scoreNumber(ones,2), 0)
        self.assertEqual(Yahtzee.scoreNumber(ones,3), 0)
        self.assertEqual(Yahtzee.scoreNumber(ones,4), 0)
        self.assertEqual(Yahtzee.scoreNumber(ones,5), 0)
        self.assertEqual(Yahtzee.scoreNumber(ones,6), 0)
        
    def test_dojoExample(self):
        dice = roll(1,1,2,4,4)
        self.assertEqual(Yahtzee.scoreNumber(dice,1), 2)
        self.assertEqual(Yahtzee.scoreNumber(dice,2), 2)
        self.assertEqual(Yahtzee.scoreNumber(dice,3), 0)
        self.assertEqual(Yahtzee.scoreNumber(dice,4), 8)
        self.assertEqual(Yahtzee.scoreNumber(dice,5), 0)
        self.assertEqual(Yahtzee.scoreNumber(dice,6), 0)

#tests for rule 2: Pair      
    def test_PairWithTwoPair(self):
        dice = roll(3,3,3,4,4)
        self.assertEqual(Yahtzee.scorePair(dice), 8)    
        
    def test_PairWithNoPairs(self):
        dice = roll(1,3,5,4,6)
        self.assertEqual(Yahtzee.scorePair(dice), 0)
        
# tests for rule 3: Two Pair
    def test_TwoPairWithNoPairs(self):
        dice = roll(1,3,5,4,6)
        self.assertEqual(Yahtzee.scoreTwoPair(dice), 0)
        
    def test_TwoPairWithOnePair(self):
        dice = roll(1,1,5,4,6)
        self.assertEqual(Yahtzee.scoreTwoPair(dice), 0)
        
    def test_TwoPairWithTwoPairs(self):
        dice = roll(1,1,2,3,3)
        self.assertEqual(Yahtzee.scoreTwoPair(dice), 8)

# tests for rule 4: Three of a kind

# tests for rule 5: Four of a kind

# tests for rule 6: small straight
    def test_smallStraightOne(self):
        dice = roll(5,2,3,4,1)
        self.assertEqual(Yahtzee.scoreSmallStraight(dice),30)
        
    def test_smallStraightTwo(self):
        dice = roll(5,2,3,4,6)
        self.assertEqual(Yahtzee.scoreSmallStraight(dice),30)

    def test_smallStraightThree(self):
        dice = roll(5,1,3,4,6)
        self.assertEqual(Yahtzee.scoreSmallStraight(dice),30)

    def test_smallStraightNone(self):
        dice = roll(5,5,1,4,6)
        self.assertEqual(Yahtzee.scoreSmallStraight(dice),0)

# tests for rule 7: large straight
    def test_largeStraightOne(self):
        dice = roll(5,2,3,4,1)
        self.assertEqual(Yahtzee.scoreLargeStraight(dice),40)

    def test_largeStraightTwo(self):
        dice = roll(5,2,3,4,6)
        self.assertEqual(Yahtzee.scoreLargeStraight(dice),40)

    def test_largeStraightNone(self):
        dice = roll(5,5,1,4,6)
        self.assertEqual(Yahtzee.scoreLargeStraight(dice),0)


# tests for rule 8: full house

# tests for rule 9: yahtzee (five of a kind)

# tests for rule 10: chance
    def test_Chance(self):
        dice = roll(1,2,3,4,5)
        self.assertEqual(Yahtzee.scoreChance(dice),15)

def roll(d1, d2, d3, d4, d5):
    return [d1, d2, d3, d4, d5]

if __name__ == '__main__':
    unittest.main()
    