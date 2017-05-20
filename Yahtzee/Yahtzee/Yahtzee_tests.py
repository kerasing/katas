import unittest
import Yahtzee

class Test_YahtzeeScoring(unittest.TestCase):
#tests for rule 1: individual dice faces
    def test_Ones(self):
        dice = roll(1,1,1,1,1)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Ones),   5)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Twos),   0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Threes), 0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Fours),  0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Fives),  0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Sixes),  0)
        
    def test_Roll2(self):
        dice = roll(1,1,2,4,4)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Ones),   2)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Twos),   2)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Threes), 0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Fours),  8)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Fives),  0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Sixes),  0)
        
    def test_Roll3(self):
        dice = roll(3,3,5,5,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Ones),   0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Twos),   0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Threes), 6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Fours),  0)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Fives),  10)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Sixes),  6)

#tests for rule 2: Pair      
    def test_PairWithTwoPair(self):
        dice = roll(3,3,3,4,4)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Pair),   8)
        
    def test_PairWithNoPairs(self):
        dice = roll(1,3,5,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Pair),   0)
        
# tests for rule 3: Two Pair
    def test_TwoPairWithNoPairs(self):
        dice = roll(1,3,5,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.TwoPair),   0)
        
    def test_TwoPairWithOnePair(self):
        dice = roll(1,1,5,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.TwoPair),   0)
        
    def test_TwoPairWithTwoPairs(self):
        dice = roll(1,1,2,3,3)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.TwoPair),   8)

# tests for rule 4: Three of a kind
    def test_ThreeOAK(self):
        dice = roll(1,1,1,2,3)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.ThreeOfAKind),   3)
        
    def test_ThreeOAKNoMatches(self):
        dice = roll(1,1,2,2,3)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.ThreeOfAKind),   0)

# tests for rule 5: Four of a kind
    def test_FourOAK(self):
        dice = roll(1,1,1,2,1)
        self.assertEqual(Yahtzee.scoreFourOfAKind(dice), 4)
        
    def test_FourOAKNoMatches(self):
        dice = roll(1,1,2,2,3)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.FourOfAKind),    0)

# tests for rule 6: small straight
    def test_smallStraightOne(self):
        dice = roll(5,2,3,4,1)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.SmallStraight),  30)
        
    def test_smallStraightTwo(self):
        dice = roll(5,2,3,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.SmallStraight),   30)

    def test_smallStraightThree(self):
        dice = roll(5,1,3,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.SmallStraight),   30)

    def test_smallStraightNone(self):
        dice = roll(5,5,1,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.SmallStraight),   0)

# tests for rule 7: large straight
    def test_largeStraightOne(self):
        dice = roll(5,2,3,4,1)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.LargeStraight),   40)

    def test_largeStraightTwo(self):
        dice = roll(5,2,3,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.LargeStraight),   40)

    def test_largeStraightNone(self):
        dice = roll(5,5,1,4,6)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.LargeStraight),   0)


# tests for rule 8: full house
    def test_FullHouse(self):
        dice = roll(1,1,1,2,2)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.FullHouse),   7)
       
    def test_NotFullHouse(self):
        dice = roll(1,1,2,2,3)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.FullHouse),   0)

# tests for rule 9: yahtzee (five of a kind)
    def test_FiveOAK(self):
        dice = roll(1,1,1,1,1)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Yahtzee),   5)
       
    def test_FiveOAKNoMatches(self):
        dice = roll(1,1,2,2,3)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Yahtzee),   0)

# tests for rule 10: chance
    def test_Chance(self):
        dice = roll(1,2,3,4,5)
        self.assertEqual(Yahtzee.score(dice,Yahtzee.YahtzeeScore.Chance),   15)

def roll(d1, d2, d3, d4, d5):
    return [d1, d2, d3, d4, d5]

if __name__ == '__main__':
    unittest.main()
    