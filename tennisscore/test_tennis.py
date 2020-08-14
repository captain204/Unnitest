import  unittest
from tennis.tennis import tennis_score
class TennisTest(unittest.TestCase):
    def test_even_scores_zero_points(self):
        self.assertEqual("Love-all", tennis_score(0,0))

    def test_even_scores_zero_points(self):
        self.assertEqual("Love-All",tennis_score(0,0))

    def test_even_score_one_points(self):
        self.assertEqual("Fifteen-All",tennis_score(1,1))

    def test_even_score_two_points(self):
        self.assertEqual("Fifteen-All",tennis_score(2,2))


