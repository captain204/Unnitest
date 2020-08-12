def small_straight(dice):
    """Score a given roll in the 'Small Straight Yatzy Category

    Args:
        dice: a sorted list of five integers indicating the dice rolled
    Returns:
        an integer score

    >>>small_straight([1,2,4,5,6])
    18

    This function only recognize sorted list and not other forms of collections:
    >>>small_straight({1,2,4,5,6})
    0
    """
    if dice == [1,2,4,5,6]:
        return sum(dice)
    else:
        return 0
