import unittest

from theatre import SeatFinder

class SeatFinderTest(unittest.TestCase):
    def test_prefer_near_front_seat(self):
        finder = SeatFinder(available_seats={"A6","B6","C7"})
        seats = finder.find_seats(1)
        assert seats == {"A6"}

    def test_finds_adjacent_seats_when_more_than_one_requested(self):
        finder = SeatFinder(available_seats={"A6","A8","C6","C7"})
        seats = finder.find_seats(2)
        assert seats == {"C6","C7"}

    def test_finds_seperate_seats_adjacent_not_available(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(2)
        assert seats =={"B6","A6"}

    def test_find_seats_fails_when_not_available(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(5)
        assert seats == {}

    def test_find_seats_for_wheelchair_users_on_front_row(self):
        finder = SeatFinder(available_seats={"A1W", "A6", "C7"})
        seats = finder.find_seats(1,wheelchair_count=1)
        assert seats == {"A1W"}